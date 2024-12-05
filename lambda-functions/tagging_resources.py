import boto3
ec2_client = boto3.client('ec2')
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
lambda_client = boto3.client('lambda')
client = boto3.client('resourcegroupstaggingapi')
def lambda_handler(event, context):
    ec2_instances_list = list_ec2_instance()  # All EC2 instance ids available
    lambda_function_arns = list_lambda_functions()  # All Lambda function ARNs available
    vpc_ids_list = list_vpcs()  # All VPC IDs available
    s3_arn_list = s3_arns_list() #Getting s3 arns list
    volume_ids = ec2_volume_list()
    if ec2_instances_list:
        ec2_client.create_tags(
        Resources=ec2_instances_list,
        Tags=[{'Key': 'ujjwal', 'Value': 'ujjwal-ec2-tag'}]
    )
        
    if vpc_ids_list:
        ec2_client.create_tags(
            Resources=vpc_ids_list,
            Tags=[{'Key': 'ujjwal', 'Value': 'ujjwal-tag-vpc'}]
        )
        print("Tagged VPCs successfully")
        
    if lambda_function_arns:
        lambda_function_arns = list_lambda_functions()
        print()
        newlist = []
        for i in range(0,16):
            newlist.append(lambda_function_arns[i])
        client.tag_resources(
            ResourceARNList=newlist,
            Tags={
            'Ujjwal-test-1': 'ujjwal-lambda-tag123'
            }
        )
    
    if s3_arn_list:
        
        newS3List = []
        for val in range(0,16):
            newS3List.append(s3_arn_list[val])

        client.tag_resources(
                ResourceARNList=newS3List,
                Tags={
                'Ujjwal': 'ujjwal-s3-tag'
                }
            )
        
    if volume_ids:
        ec2_client.create_tags(
            Resources=volume_ids,
            Tags=[{'Key': 'ujjwal', 'Value': 'ujjwal-volume-tag'}]
        )

# def list_ec2_volumes():
#     response = ec2_client.
    
def list_ec2_instance():
    responses = ec2_client.describe_instances()
    print(responses)
    instances = []
    for response in responses["Reservations"]:
        instances.append(response["Instances"][0]["InstanceId"])
    # print(instances)
    return instances



def list_lambda_functions():
    lambda_response = lambda_client.list_functions()
    functions_list = []
    for value in lambda_response["Functions"]:
        functions_list.append(value["FunctionArn"])
    return functions_list

def list_vpcs():
    vpcs_response = ec2_client.describe_vpcs()
    vpcs_id_list = []
    for value in vpcs_response["Vpcs"]:
        vpcs_id_list.append(value["VpcId"])
    return vpcs_id_list


def s3_arns_list():
    response = s3_client.list_buckets()
    bucket_name_list = [bucket['Name'] for bucket in response['Buckets']]
    bucket_arns_list = [f"arn:aws:s3:::{bucket}" for bucket in bucket_name_list]
    return bucket_arns_list



def ec2_volume_list():
    response = ec2_client.describe_volumes()
    volume_ids = []
    for volume in response['Volumes']:
        volume_ids.append(volume['VolumeId'])
    # print(volume_ids)
    return volume_ids