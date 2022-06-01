import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    
    
    name = event['queryStringParameters']['name']
    age = event['queryStringParameters']['age']
    print(name,age)
    print(type(name),type(age))
    
    data = client.get_item(
    TableName='Msgtable',
    Key={
        "name": {
          "S": name
        },
        "age":{
          "N": str(age)
        }
    }
    )
    
    response = {
      'statusCode': 200,
      'body': json.dumps(data),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
    }
    
    return response