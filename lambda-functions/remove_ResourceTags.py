import boto3
ec2_client = boto3.client('ec2')
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
lambda_client = boto3.client('lambda')
client = boto3.client('resourcegroupstaggingapi')
def lambda_handler(event, context):
    # Ec2 tag removing space
    ec2_instance_list = list_ec2_instance()
    remove_ec2_tag(ec2_instance_list,[{'Key':'ujjwal'}])

    # removing vpc tags
    vpc_ids_list = list_vpcs()  # All VPC IDs available
    remove_vpc_tag(vpc_ids_list,[{'Key':'ujjwal','Value':'ujjwal-tag-vpc'}])


    # Lambda funtion tags removing space
    lambda_function_arns= list_lambda_functions()
    print(lambda_function_arns)
    newlist = []
    for i in range(0,16):
        newlist.append(lambda_function_arns[i])
    for val in newlist:
        remove_lambda_tags(val,['Ujjwal-test-1'])
        
    
    

    
    # S3 remove tags
    s3_arn_list = s3_arns_list()
    newS3List = []
    for val in range(0,16):
        newS3List.append(s3_arn_list[val])
    remove_s3_tag(newS3List,'Ujjwal')
    
    #remove func call for volumes
    volume_ids = ec2_volume_list()
    remove_volume_tag(volume_ids,[{'Key':'ujjwal'}])
    
def remove_s3_tag(s3_arn,key_value):
    client.untag_resources(
    ResourceARNList=s3_arn,
    TagKeys=[
        key_value,
    ])     
      
      
# Remove vpc tags
def remove_vpc_tag(vpcIds,key_value):
    ec2_client.delete_tags(
        Resources=vpcIds,
        Tags=key_value
    )  
    
# Removing given tag from all the ec2 instances
def remove_ec2_tag(ec2_ids,key_value):
    ec2_client.delete_tags(
        Resources=ec2_ids,
        Tags=key_value
    )
    print('successfully deleted ec2 tags')
# Getting all the ec2 instances ids
def list_ec2_instance():
    responses = ec2_client.describe_instances()
    print(responses)
    instances = []
    for response in responses["Reservations"]:
        instances.append(response["Instances"][0]["InstanceId"])
    return instances



def ec2_volume_list():
    response = ec2_client.describe_volumes()
    volume_ids = []
    for volume in response['Volumes']:
        volume_ids.append(volume['VolumeId'])
    # print(volume_ids)
    return volume_ids




# Getting all the lambda function arns
def list_lambda_functions():
    lambda_response = lambda_client.list_functions()
    functions_list = []
    for value in lambda_response["Functions"]:
        functions_list.append(value["FunctionArn"])
    return functions_list
# Removing given tag from all lambda functions
def remove_lambda_tags(lambda_arns,key_value):
    lambda_client.untag_resource(
                Resource=lambda_arns,
                TagKeys=key_value
            )
    print('removed the given tag from all the lambda function')



def s3_arns_list():
    response = s3_client.list_buckets()
    bucket_name_list = [bucket['Name'] for bucket in response['Buckets']]
    bucket_arns_list = [f"arn:aws:s3:::{bucket}" for bucket in bucket_name_list]
    return bucket_arns_list



# Listing vpc
def list_vpcs():
    vpcs_response = ec2_client.describe_vpcs()
    vpcs_id_list = []
    for value in vpcs_response["Vpcs"]:
        vpcs_id_list.append(value["VpcId"])
    return vpcs_id_list


# Remove volume
def remove_volume_tag(volume_ids,key_value):
    ec2_client.delete_tags(
        Resources=volume_ids,
        Tags=key_value
        )
