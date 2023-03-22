import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Define the ID of the security group to delete
security_group_id = 'sg-008083625302d5ece'

# Delete the security group
response = ec2.delete_security_group(GroupId=security_group_id)

# Print the response
print(response)
