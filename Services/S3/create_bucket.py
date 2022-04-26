import boto3 

def create(name, access_id,secret_id):
    s3_client = boto3.client("s3",aws_access_key_id=access_id, aws_secret_access_key = secret_id)
# def create(name):
    # s3_client = boto3.client('s3')
    s3_client.create_bucket(Bucket=name)

# create('dhruv1234567garg')

# s3 = boto3.resource('s3')


# def create_bucket(name):
#     s3.create_bucket(Bucket=name)

# create_bucket('dhruv123456garg')