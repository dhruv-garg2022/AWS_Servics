import boto3

def list(access_id,secret_id):
    s3_client = boto3.client("s3",aws_access_key_id=access_id, aws_secret_access_key = secret_id)
# def list():
#     s3_client = boto3.client('s3')
    response = s3_client.list_buckets()

    return response

    # for bucket in response['Buckets']:
    #     print(bucket['Name'])

# list()
    