import boto3

ec2 = boto3.resource('ec2')

instance = ec2.Instance('i-039e31ca09f235a82')

print(instance.state['Name'])

if instance.state['Name']=='stopped':
    instance.start()

elif instance.state['Name']=='running':
    instance.stop()
