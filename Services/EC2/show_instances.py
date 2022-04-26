import boto3

def get_all_instances(access_id,secret_id):
  ec2_client = boto3.client("ec2",aws_access_key_id=access_id, aws_secret_access_key = secret_id)

  #describe_insatnces() will give us all the information of the specified or all instances
  response = ec2_client.describe_instances()["Reservations"]
  return response
#   print("InstanceId\t\tState\tPublic Ip\tPrivate Ip")
  
#   for reservation in response:
#     for instance in reservation["Instances"]:
        # instance_id = instance["InstanceId"]
        
        # instance_state = instance["State"]["Name"]
        # print(instance_id,"\t",instance_state,"\t",end= "")
        # if instance_state == 'running':
        #     public_ip = instance["PublicIpAddress"]
        #     private_ip = instance["PrivateIpAddress"]
        #     print(public_ip,"\t",private_ip)
        # else:
        #     print('-\t-')


    #   print(instance_id,"\t",instance_state,"\t",public_ip,"\t",private_ip)
    