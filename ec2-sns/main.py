import streamlit as st
import boto3
import json

sns = boto3.client('sns')

def publish_to_sns(topic_name, message):

    try:
        response = sns.publish(
            TopicArn=topic_name,
            Message=message
        )
        return response
    except Exception as e:
        return e


def subscribe_to_sns(topic_name, email_id):
    
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
    
    st.title('Publishing to SNS')
    st.subheader('This is a simple app to send a message to an SNS topic')
    st.write()
    st.write()
    mail_id = st.text_input('Enter your email id to subscribe to the topic')
    #message = st.text_input('Enter the message')

    if st.button('Send'):

        sub,success = subscribe_to_sns(arn, mail_id)

        if success:
            msg = 'To confirm your subscription, please check your email and click the link to confirm.' 
            res = publish_to_sns(topic_name=arn,message=msg)
            st.success(msg)
            #st.write(res)
            subscribers = sns.list_subscriptions_by_topic(TopicArn=arn)
            st.write(subscribers['Subscriptions'][0]['Endpoint'])

        else:
            st.error('Please enter a valid email id')
            st.write(sub)

    else:
        st.write('You cancelled')



if __name__ == '__main__':

    arn = 'arn:aws:sns:us-west-2:384076122328:Mytopic'
    main(arn)
