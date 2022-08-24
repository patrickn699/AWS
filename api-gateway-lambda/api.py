import json

print('Loading function')

def lambda_handler(event, context):
	#1. Parse out query string params
	name = event['queryStringParameters']['name']
	city = event['queryStringParameters']['city']
	age = event['queryStringParameters']['age']

	print('name =' + name)
	print('city = ' + city)
	print('age =' + age)

	#2. Construct the body of the response object
	transactionResponse = {}
	transactionResponse['name'] = name
	transactionResponse['city'] = city
	transactionResponse['age'] = age
	transactionResponse['message'] = 'Hello from Lambda land'

	#3. Construct http response object
	responseObject = {}
	responseObject['statusCode'] = 200
	responseObject['headers'] = {}
	responseObject['headers']['Content-Type'] = 'application/json'
	responseObject['body'] = json.dumps(transactionResponse)

	#4. Return the response object
	return responseObject

#GetStartedLambdaProxyIntegration
