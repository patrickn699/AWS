from PIL import Image


def handler(event, context):
    #print(event)
    #print(context)
    print('Hello from Lambda!','PIL version:')
    return {
        "statusCode": 200,
        "body": "Hello from Lambda!"
    }