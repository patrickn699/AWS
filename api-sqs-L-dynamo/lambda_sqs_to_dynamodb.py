import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
  
  # Get the service resource
  
  #print(event)
  
  print(event["Records"][0]["body"])
  #name = event['queryStringParameters']['MessageBody']
  #age = event['queryStringParameters']['Age']
  
  #nom = event["Records"][0]["body"]
  #print(nom)
  
  nom = event["Records"][0]["body"].split()
  print(nom[0],nom[1])
  
  
  #print(event["Records"][0]["body"])
  
  try:
  
      data = client.put_item(
      TableName='Msgtable',
      Item={
          "name": {
            "S": nom[0]
          },
          "age": {
            "N": str(nom[1])
          }
      }
      )
      
  except Exception as e:
      print(e)

  response = {
    'statusCode': 200,
    'body': 'successfully created item!',
    'headers': {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*'
    },
  }
  
  print('Item created successfully')

  return response
  
  
  
  
  #return event