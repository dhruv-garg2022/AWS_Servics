import boto3

def create_ec2instance(access_id,secret_id):
  try:

    # create object of ec2 and use client as it is a low level object to access AWS objects 
    # alternative of client is resource but it is a high level object
    ec2_client = boto3.client("ec2",aws_access_key_id=access_id, aws_secret_access_key = secret_id)
    
    # run_instances will create instance
    ec2_client.run_instances(
      ImageId="ami-04505e74c0741db8d",
      MinCount=1,
      MaxCount=1,
      InstanceType="t2.micro",
      
      # to check or create key pair 
      # aws searchbar -> key pairs (EC2 feature) -> create key pair -> Give name, select pem -> Create
      KeyName="Dhruv"
    )

    # ec2_client[0].wait_until_running()

  except Exception as e:
    print(e)
