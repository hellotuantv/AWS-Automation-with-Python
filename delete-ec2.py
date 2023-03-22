import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Define the ID of the instance to delete
instance_id = 'i-0cbb0ec6d66a75e41'

# Terminate the instance
response = ec2.terminate_instances(InstanceIds=[instance_id])

# Print the response
print(response)