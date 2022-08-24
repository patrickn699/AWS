
# POC for invoking Lambda when an object is uploaded to S3

A brief description of what this project does and who it's for


1. Create S3 buckets and upload a demo object.

    * Create two S3 buckets, The target bucket must be named source-resized, where source is the name of the source bucket. 
        For example, a source bucket named mybucket and a target bucket named mybucket-resized.

      2.   In the source bucket, upload a .jpg object, for example, pic.jpg.

        3. You must create this sample object before you test your Lambda function. 
            When you test the function manually using the Lambda invoke command, you pass sample event data to the function that specifies the source bucket name and pic.jpg as the newly created object.



2. Create the IAM policy

    * Create an IAM policy that defines the permissions for the Lambda function. The function must have permissions to:

        2. Get the object from the source S3 bucket.

       3.  Put the resized object into the target S3 bucket.

       4.  Write logs to Amazon CloudWatch Logs.

       5. To create an IAM policy

        6. Open the Policies page in the IAM console.

       7.  Choose Create policy.

        8. Choose the JSON tab, and then paste the following policy. Be sure to replace mybucket with the name of the source bucket that you created previously.


                {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Action": [
                                "logs:PutLogEvents",
                                "logs:CreateLogGroup",
                                "logs:CreateLogStream"
                            ],
                            "Resource": "arn:aws:logs:*:*:*"
                        },
                        {
                            "Effect": "Allow",
                            "Action": [
                                "s3:GetObject"
                            ],
                            "Resource": "arn:aws:s3:::mybucket/*"
                        },
                        {
                            "Effect": "Allow",
                            "Action": [
                                "s3:PutObject"
                            ],
                            "Resource": "arn:aws:s3:::mybucket-resized/*"
                        }
                    ]
                }



        9. Choose Next: Tags.

       10. Choose Next: Review.

        11. Under Review policy, for Name, enter AWSLambdaS3Policy.

        12. Choose Create policy.


        

3. Create the deployment package

    create a deployment package using SAM or Docker or uploading a zip file.


4. Create the lambda function

    Use the above code and paste it in the inline lambda editor.



5.  Test the Lambda function


    To test the function use the below json file

         {
            "Records":[
                {
                "eventVersion":"2.0",
                "eventSource":"aws:s3",
                "awsRegion":"us-west-2",
                "eventTime":"1970-01-01T00:00:00.000Z",
                "eventName":"ObjectCreated:Put",
                "userIdentity":{
                    "principalId":"AIDAJDPLRKLG7UEXAMPLE"
                },
                "requestParameters":{
                    "sourceIPAddress":"127.0.0.1"
                },
                "responseElements":{
                    "x-amz-request-id":"C3D13FE58DE4C810",
                    "x-amz-id-2":"FMyUVURIY8/IgAtTv8xRjskZQpcIZ9KG4V5Wp6S7S/JRWeUWerMUE5JgHvANOjpD"
                },
                "s3":{
                    "s3SchemaVersion":"1.0",
                    "configurationId":"testConfigRule",
                    "bucket":{
                    "name":"sourcebucket",
                    "ownerIdentity":{
                        "principalId":"A3NL1KOZZKExample"
                    },
                    "arn":"arn:aws:s3:::sourcebucket"
                    },
                    "object":{
                    "key":"yourimg.jpg",
                    "size":1024,
                    "eTag":"d41d8cd98f00b204e9800998ecf8427e",
                    "versionId":"096fKKXTRTtl3on89fVO.nfljtsv6qko"
                    }
                }
                }
            ]
            }


    Now, click on save and Test!.

