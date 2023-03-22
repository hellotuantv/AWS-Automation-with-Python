import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

# Create a security group and allow SSH access from everywhere
response = ec2.create_security_group(
    Description='ssh SG',
    GroupName='ssh SG',
    VpcId='vpc-0c49deac2c9175c89',
)

# Get the ID of the new security group
security_group_id = response['GroupId']

# Add an inbound rule to allow SSH access from everywhere
ec2.authorize_security_group_ingress(
    GroupId=security_group_id,
    IpPermissions=[
        {
            'IpProtocol': 'tcp',
            'FromPort': 22,
            'ToPort': 22,
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0'
                },
            ],
        },
    ],
)


print('Security group created: {}'.format(security_group_id))
