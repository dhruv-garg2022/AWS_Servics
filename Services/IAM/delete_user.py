import boto3

def delete(name):
    iam_client = boto3.client('iam')
    iam_client.delete_user(UserName=name)

