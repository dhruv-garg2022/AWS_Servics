import boto3

def list():
    iam_client = boto3.client('iam')
    list_users = iam_client.list_users()['Users']
    users=[]
    for user in list_users:
        users.append([user['UserName'],user['UserId'],user['Arn'],user['CreateDate']])
    return users
# list()
