import boto3

TOPIC_ARN = 'arn:aws:sns:ap-southeast-2:351003926708:aws-cost-topic'
PROTOCOL='email'
ENDPOINT='hellotuantv@gmail.com'

sns_client = boto3.client('sns')

response = sns_client.subscribe(
    TopicArn=TOPIC_ARN,
    Protocol=PROTOCOL,
    Endpoint=ENDPOINT   
)   