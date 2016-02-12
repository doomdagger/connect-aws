aws ec2 create-security-group --group-name SecurityGroup#10 --description "security group created from aws cli"
aws ec2 authorize-security-group-ingress --group-name SecurityGroup#10 --protocol tcp --port 22 --cidr 0.0.0.0/0
aws ec2 create-key-pair --key-name KEY#10 --query 'KeyMaterial' --output text > KEY#10.pem
chmod 400 KEY#10.pem
aws ec2 run-instances --image-id ami-f0091d91 --security-group-ids sg-b018ced5 --count 1 --instance-type t2.micro --key-name KEY#10 --query 'Instances[0].InstanceId'
aws ec2 describe-instances --instance-ids i-ec3e1e2k --query 'Reservations[0].Instances[0].PublicIpAddress'
ssh -i devenv-key.pem ubuntu@54.183.22.255
