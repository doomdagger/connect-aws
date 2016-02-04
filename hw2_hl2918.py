import time
import boto3

__author__ = "He Li"

# get service resource
ec2_res = boto3.resource('ec2')

# create new key-pair
key_pool = {'KEY#' + str(num) for num in list(range(100))}

avail_key = (key_pool - {key.key_name for key in ec2_res.key_pairs.all()}).pop()

key_pair = ec2_res.create_key_pair(
    DryRun=False,
    KeyName=avail_key
)

print("The newly created key pair\n\tname: {name}\n\tfinger print: {fingerPrint}"
      .format(name=key_pair.key_name, fingerPrint=key_pair.key_fingerprint))

# persist the pem
with open(key_pair.key_name + '.pem', mode='w') as f:
    f.write(key_pair.key_material)

# create new security-group
group_pool = {'SecurityGroup#' + str(num) for num in list(range(100))}

avail_group = (group_pool - {group.group_name for group in ec2_res.security_groups.all()}).pop()

security_group = ec2_res.create_security_group(
    DryRun=False,
    GroupName=avail_group,
    Description='Created by boto3, all default rules'
)

print("The newly created security group\n\tname: {name}\n\tid: {id}"
      .format(name=security_group.group_name, id=security_group.group_id))

security_group.authorize_ingress(
    DryRun=False,
    GroupName=security_group.group_name,
    IpProtocol='-1',
    FromPort=0,
    ToPort=65535,
    CidrIp='0.0.0.0/0',
)

security_group.reload()

# create new instance
instances = ec2_res.create_instances(
    DryRun=False,
    ImageId='ami-f0091d91',
    MinCount=1,
    MaxCount=1,
    KeyName=key_pair.key_name,
    SecurityGroups=[
        security_group.group_name,
    ],
    SecurityGroupIds=[
        security_group.group_id,
    ],
    InstanceType='t2.micro',
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/sdb',
            'Ebs': {
                'VolumeSize': 30,
                'DeleteOnTermination': True,
                'VolumeType': 'gp2',
                'Encrypted': False
            }
        }
    ],
    Monitoring={
        'Enabled': True
    },
    DisableApiTermination=False,
    InstanceInitiatedShutdownBehavior='stop',
    EbsOptimized=False
)

instance = instances[0]

# wait until the instance is running, then we can get public dns name.
time.sleep(5)
instance.reload()
while instance.state['Name'] != 'running':
    time.sleep(5)
    instance.reload()

print("The newly created instance\n\tid: {id}\n\tkey name: {keyName}\n\t"
      "security group name: {groupName}\n\tpublic DNS: {dns}"
      .format(id=instance.instance_id, keyName=instance.key_name,
              groupName=instance.security_groups[0]["GroupName"], dns=instance.public_dns_name))
