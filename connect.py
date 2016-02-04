import boto3

__author__ = 'He Li'

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
    DryRun=False,
    ImageId='ami-f0091d91',
    MinCount=1,
    MaxCount=1,
    KeyName='MAC',
    SecurityGroups=[
        'default',
    ],
    SecurityGroupIds=[
        'sg-b7f802d0',
    ],
    # UserData='string',
    InstanceType='t2.micro',
    # Placement={
    #     'AvailabilityZone': 'string',
    #     'GroupName': 'string',
    #     'Tenancy': 'default'|'dedicated'|'host',
    #     'HostId': 'string',
    #     'Affinity': 'string'
    # },
    # KernelId='string',
    # RamdiskId='string',
    # BlockDeviceMappings=[
    #     {
    #         'VirtualName': 'string',
    #         'DeviceName': 'string',
    #         'Ebs': {
    #             'SnapshotId': 'string',
    #             'VolumeSize': 123,
    #             'DeleteOnTermination': True|False,
    #             'VolumeType': 'standard'|'io1'|'gp2',
    #             'Iops': 123,
    #             'Encrypted': True|False
    #         },
    #         'NoDevice': 'string'
    #     },
    # ],
    Monitoring={
        'Enabled': True
    },
    # SubnetId='string',
    DisableApiTermination=False,
    InstanceInitiatedShutdownBehavior='stop',
    # PrivateIpAddress='string',
    # ClientToken='string',
    # AdditionalInfo='string',
    # NetworkInterfaces=[
    #     {
    #         'NetworkInterfaceId': 'string',
    #         'DeviceIndex': 123,
    #         'SubnetId': 'string',
    #         'Description': 'string',
    #         'PrivateIpAddress': 'string',
    #         'Groups': [
    #             'string',
    #         ],
    #         'DeleteOnTermination': True|False,
    #         'PrivateIpAddresses': [
    #             {
    #                 'PrivateIpAddress': 'string',
    #                 'Primary': True|False
    #             },
    #         ],
    #         'SecondaryPrivateIpAddressCount': 123,
    #         'AssociatePublicIpAddress': True|False
    #     },
    # ],
    # IamInstanceProfile={
    #     'Arn': 'string',
    #     'Name': 'string'
    # },
    EbsOptimized=False
)
