import boto3

def create(name):
    iam_client = boto3.client('iam')
    iam_client.create_user(UserName=name)
