import time
import boto3

__author__ = "He Li"

"""
    1. EBS as storage disk: Create an EBS volume, attach to a VM, create the file system and then mount this disk.
    Once you do this, show that this disk appears in the VM.
"""

availabilityZone = 'us-west-2a'

# get ec2 client
client = boto3.client('ec2')

# create the volume
volume = client.create_volume(
    DryRun=False,
    Size=1,
    AvailabilityZone=availabilityZone,
    VolumeType='standard',
    Encrypted=False,
)
volumeId = volume['VolumeId']
print("Newly created volume:\n\tVolume ID: {volumeId}\n\tSize: {size} GB\n\t"
      "Availability Zone: {zone}\n\tVolume Type: {type}"
      .format(volumeId=volumeId, size=volume['Size'], zone=volume['AvailabilityZone'], type=volume['VolumeType']))

# get the volume object
resource = boto3.resource('ec2')
volume = resource.Volume(volumeId)
# wait until the volume is ready, then we can attach it
print("Wait for the Volume ready to be attached...")
time.sleep(3)
volume.reload()
while volume.state != 'available':
    time.sleep(3)
    volume.reload()

# get one instance to attach volume
instances = client.describe_instances(
    DryRun=False,
    Filters=[
        {
            'Name': 'availability-zone',
            'Values': [
                availabilityZone,
            ]
        },
    ],
    MaxResults=6
)

instanceId = instances['Reservations'][0]['Instances'][0]['InstanceId']
dnsName = instances['Reservations'][0]['Instances'][0]['PublicDnsName']

# attach the volume
response = client.attach_volume(
    DryRun=False,
    VolumeId=volumeId,
    InstanceId=instanceId,
    Device='xvdh'
)
print("Volume attached:\n\tInstance ID: {instanceId}\n\tPublic DNS:{dns}\n\tVolume ID: {volumeId}\n\tDevice: {device}"
      .format(instanceId=instanceId, dns=dnsName, volumeId=volumeId, device=response['Device']))

"""
    2. Create your own AMI: Take a look at the following link to understand how to create your own AMI.
"""


