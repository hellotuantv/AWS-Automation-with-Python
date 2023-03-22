import boto3
import datetime

TOPIC_ARN = 'arn:aws:sns:ap-southeast-2:351003926708:aws-cost-topic'

# Define the SNS client
sns_client = boto3.client('sns')

# Define the Cost Explorer client
ce_client = boto3.client('ce')

# Get the current month
now = datetime.datetime.utcnow()
start_of_month = datetime.datetime(year=now.year, month=now.month, day=1).strftime('%Y-%m-%d')

# Define the cost explorer parameters
cost_params = {
    'TimePeriod': {
        'Start': start_of_month,
        'End': now.strftime('%Y-%m-%d')
    },
    'Granularity': 'MONTHLY',
    'Metrics': ['UnblendedCost']
}

# Get the current month's AWS costs
response = ce_client.get_cost_and_usage(**cost_params)

# Define the SNS parameters
if float(response['ResultsByTime'][0]['Total']['UnblendedCost']['Amount']) >= 5:
    message = f"Your current month AWS costs have reached ${response['ResultsByTime'][0]['Total']['UnblendedCost']['Amount']}."
    sns_params = {
        'TopicArn': TOPIC_ARN,
        'Message': message,
        'Subject': 'AWS Costs Alert'
    }

    # Send the SNS message
    sns_client.publish(**sns_params)


