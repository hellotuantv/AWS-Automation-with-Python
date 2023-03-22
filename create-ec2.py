import boto3

ec2 = boto3.resource('ec2')

# Set userdata
userdata = '''#!/bin/bash
'''

# Create EC2 instance
instance = ec2.create_instances(
    ImageId='ami-018c0195987eb63ee',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='Key',
    SecurityGroupIds= ['sg-04c06938e2855056d'],
    UserData=userdata
)

print("Instance created with ID:", instance[0].id)