import boto3
ec2_client = boto3.client('ec2')

def lambda_handler(event,context):
    response = ec2_client.describe_vpcs()
    vpcs_id = []
    for res in response['Vpcs']:
        vpcs_id.append(res['VpcId'])
    print(maximum_sgs(vpcs_id))

def maximum_sgs(vpcs_id):
    max_size = 0
    max_sg_vpc=""
    for id in vpcs_id:
        res = helper_func(id)
        if res[0] > max_size:
            max_size = res[0]
            max_sg_vpc = res[1]
    return max_size, max_sg_vpc

def helper_func(vpc_id):
    sg_response = ec2_client.describe_security_groups(
            Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}]
        )
    return len(sg_response["SecurityGroups"]), vpc_id
