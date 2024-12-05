import boto3
ec2_client = boto3.client('ec2')
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
lambda_client = boto3.client('lambda')
client = boto3.client('resourcegroupstaggingapi')


ec2_list= []
ec2Volume_list = []
vpcs_list = []
s3_arns = []
lambdaFunc_arns = []
def get_resources():
    global ec2_list,ec2Volume_list,vpcs_list,lambdaFunc_arns
    # ec2_instances_ids
    ec2_response = ec2_client.describe_instances()
    for inst in ec2_response['Reservations']:
        ec2_list.append(inst['Instances'][0]['InstanceId'])
        
    # ec2_volumes_ids
    ec2Vloumes_response = ec2_client.describe_volumes()
    for volume in ec2Vloumes_response['Volumes']:
        ec2Volume_list.append(volume['VolumeId'])
        
    # s3 bucket arns
    s3_response = s3_client.list_buckets()
    bucket_name_list = [bucket['Name'] for bucket in s3_response['Buckets']]
    bucket_arns_list = [f"arn:aws:s3:::{bucket}" for bucket in bucket_name_list]
    for i in range(0,16):
        s3_arns.append(bucket_arns_list[i])
        
    # lambda function arns
    lambda_response = lambda_client.list_functions()
    samplelist= []
    for value in lambda_response["Functions"]:
        samplelist.append(value["FunctionArn"])
    for i in range(0,16):
        lambdaFunc_arns.append(samplelist[i])
    
    
    # vpc ids
    vpcs_response = ec2_client.describe_vpcs()
    for value in vpcs_response["Vpcs"]:
        vpcs_list.append(value["VpcId"])
    

    