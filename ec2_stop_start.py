import boto3
def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-east-1')
    ec2.stop_instances(InstanceIds=['i-034d80e0dbd354089'])
    print('stopped your instances: ' + str('i-034d80e0dbd354089'))
    return
    
    
    
import boto3
def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-east-1')
    ec2.start_instances(InstanceIds=['i-034d80e0dbd354089'])
    print('started your instances: ' + str('i-034d80e0dbd354089'))
    return
