import boto3

def create_sns_subscription(email):

    sns = boto3.client('sns')
    response = sns.subscribe(
        TopicArn='arn:aws:sns:us-east-1:89898989898:task-memo-topic',
        Protocol='email',
        Endpoint=email
    )
    return response


def send_email(email, subject, body):
    
    sns = boto3.client('sns')
    response = sns.publish(
        TopicArn='arn:aws:sns:us-east-1:89898989898:task-memo-topic',
        Message=body,
        Subject=subject,
        Protocol='email',
        Endpoint=email
    )
    return response