import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Retrieve information about all running EC2 instances
response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

# Extract relevant information from the response
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        instance_type = instance['InstanceType']
        instance_state = instance['State']['Name']
        instance_launch_time = instance['LaunchTime']
        instance_private_ip = instance['PrivateIpAddress']
        instance_public_ip = instance.get('PublicIpAddress', 'N/A')
        
        # Print the information for each running instance
        print(f'Instance ID: {instance_id}')
        print(f'Instance Type: {instance_type}')
        print(f'Instance State: {instance_state}')
        print(f'Launch Time: {instance_launch_time}')
        print(f'Private IP Address: {instance_private_ip}')
        print(f'Public IP Address: {instance_public_ip}')
        print('\n')
