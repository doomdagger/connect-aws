import boto3

__author__ = "He Li"

ec2 = boto3.client('ec2')

# images = ec2.describe_images(
#     ImageIds=[
#         'ami-f0091d91'
#     ]
# )

resource = boto3.resource('ec2')

# for k in resource.key_pairs.all():
#     print(k)
#
# groups = ec2.describe_security_groups()
#
# print(groups['SecurityGroups'][0]['GroupId'])

for k in resource.instances.all():
    print(k)


