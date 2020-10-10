import boto3
def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-east-1')
    ec2.stop_instances(InstanceIds=['i-***'])
    print('stopped your instances: ' + str('i-***'))
    return
    
    
    
import boto3
def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-east-1')
    ec2.start_instances(InstanceIds=['i-***'])
    print('started your instances: ' + str('i-***'))
    return
