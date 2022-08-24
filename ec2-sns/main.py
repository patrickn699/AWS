import streamlit as st
import boto3
import json

sns = boto3.client('sns', region_name = 'us-west-2')
msg = "Hellow from SNS, you received this message because you subscribed to this topic"

def publish_to_sns(topic_name : str, message: str)-> dict:

    try:
        response = sns.publish(
            TopicArn=topic_name,
            Message=message
        )
        return response
    except Exception as e:
        return e


def subscribe_to_sns(topic_name: str, email_id: str)-> dict:
    
    try:
        response = sns.subscribe(
            TopicArn=topic_name,
            Protocol='email',
            Endpoint=email_id
        )
        return response, True
    except Exception as e:
        return e, False


def main(arn):
    
    st.title('Publishing to AWS SNS')
    st.subheader('This is a simple app to send a message to a SNS topic')
    st.write()
    st.write()
    subscribers = sns.list_subscriptions_by_topic(TopicArn=arn)
    #st.write(subscribers)
    
    option = st.selectbox('select an option', ['publish', 'subscribe', 'unsbscribe'])
    

    if st.button('submit') and option == 'publish' and subscribers['Subscriptions'][0]['Endpoint'] != '':
        response = publish_to_sns(arn, message = msg)
        st.write(response)

    elif option == 'subscribe':

        mail_id = st.text_input('Enter your email id to subscribe to the topic')


        if st.button('Subscribe') and subscribers['Subscriptions'][0]['Endpoint'] != mail_id:

            sub,success = subscribe_to_sns(arn, mail_id)

            if success:
                msg = 'To confirm your subscription, please check your email and click the link to confirm.' 
                res = publish_to_sns(topic_name=arn,message=msg)
                st.success(msg)
                #st.write(subscribers)
                st.write(subscribers['Subscriptions'][0]['Endpoint'])

            else:
                st.error('Please enter a valid email id')
                st.write(sub)

        else:
            st.write('You are already subscribed to the topic')

    elif option == 'unsbscribe' and subscribers['Subscriptions'] != []:  

        st.write('Unsubscribing from the topic')
        unsub = sns.unsubscribe(SubscriptionArn=subscribers['Subscriptions'][0]['SubscriptionArn'])
        st.write('You have been unsubscribed from the topic')

    else:
        st.write('Please subscribe/select and option first')



if __name__ == '__main__':

    arn = 'arn:aws:sns:us-west-2:384076122328:Mytopic'
    main(arn)
