import boto3
ec2_client = boto3.client('ec2')
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
lambda_client = boto3.client('lambda')
def lambda_handler(event, context):
    ec2_instances_list = list_ec2_instance()  # All EC2 instance ids available
    s3_bucket_names = list_s3_bucksts()  # All S3 bucket names available
    lambda_function_arns = list_lambda_functions()  # All Lambda function ARNs available
    vpc_ids_list = list_vpcs()  # All VPC IDs available
    
   
    if ec2_instances_list:
        ec2_client.create_tags(
            Resources=ec2_instances_list,
            Tags=[{'Key': 'ujjwal', 'Value': 'ujjwal-tag-ec2'}]
        )
        print("Tagged EC2 Instances successfully")


    if s3_bucket_names:
        for bucket in s3_bucket_names:
            s3_client.put_bucket_tagging(
                Bucket=bucket,
                Tagging={
                    'TagSet': [{'Key': 'ujjwal', 'Value': 'ujjwal-tag-s3'}]
                }
            )
        print("Tagged S3 Buckets successfully")

    
    if lambda_function_arns:
        for arn in lambda_function_arns:
            lambda_client.add_tags(
                Resource=arn,
                Tags={'ujjwal': 'ujjwal-tag-lambda'}
            )
        print("Tagged Lambda Functions successfully")

   
    if vpc_ids_list:
        ec2_client.create_tags(
            Resources=vpc_ids_list,
            Tags=[{'Key': 'ujjwal', 'Value': 'ujjwal-tag-vpc'}]
        )
        print("Tagged VPCs successfully")
    
def list_ec2_instance():
    responses = ec2_client.describe_instances()
    print(responses)
    instances = []
    for response in responses["Reservations"]:
        instances.append(response["Instances"][0]["InstanceId"])
    # print(instances)
    return instances

def list_s3_bucksts():
    s3_response = s3_client.list_buckets()
    s3_list = []
    for lists in s3_response["Buckets"]:
        s3_list.append(lists["Name"])
        
    return s3_list

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


# def remove_ec2




# import json
# import boto3
# s3_client = boto3.client('s3')

# s3 = boto3.resource('s3')
# def lambda_handler(event, context):
#     bucket_tagging = s3.BucketTagging('ujjwal-testing-tag-bucket')
#     response1=s3_client.get_bucket_tagging(
#         Bucket='ujjwal-testing-tag-bucket')['TagSet']   #Directly getting the lis of available tags
#     print(response1)

#     response1.append({  #Appending new tag in existing tag list
#         'Key': 'Ujjwal-Check',
#         'Value': 'Ujjwal-tag-s3-testing'
#     })

#     response = bucket_tagging.put( #Updating the tags of the s3 bucket
#     Tagging={
#         'TagSet': response1
#     })
#     print(response)