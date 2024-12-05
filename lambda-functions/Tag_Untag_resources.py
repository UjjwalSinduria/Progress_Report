import boto3
from resource_list import get_resources,ec2_list,ec2Volume_list,vpcs_list,s3_arns,lambdaFunc_arns
ec2_client = boto3.client('ec2')
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
lambda_client = boto3.client('lambda')
client = boto3.client('resourcegroupstaggingapi')
get_resources()
def tag_resources(resource_name):
    tag = [{'Key':'ujjwal01','Value':'ujjwal-demmo-tag'}]
    if resource_name=='EC2':
        ec2_client.create_tags(
        Resources=ec2_list,
        Tags=tag)
    
    if resource_name == 'VPC':
        ec2_client.create_tags(
            Resources=vpcs_list,
            Tags=tag
        )
               
    if resource_name == 'EC2-Volume':
        ec2_client.create_tags(
            Resources=ec2Volume_list,
            Tags=tag
        )

    if resource_name == 'S3':
        ec2_client.create_tags(
            Resources=s3_arns,
            Tags=tag
        )
    
    if resource_name == 'Lambda':
        client.tag_resources(
            ResourceARNList=lambdaFunc_arns,
            Tags={
            'ujjwal01': 'ujjwal-demmo-tag'
            }
        )
    
    
        
        