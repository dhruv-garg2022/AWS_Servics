# import boto3
from Services.EC2 import create_instance 
from Services.EC2 import show_instances
from Services.EC2 import stop_instance
from Services.EC2 import start_instance
from Services.EC2 import terminate_instance
from Services.S3 import create_bucket
from Services.S3 import list_bucket
from Services.S3 import delete_bucket
from Services.IAM import create_user
from Services.IAM import list_user
from Services.IAM import delete_user
from flask import Flask, render_template, request, redirect, url_for
app= Flask(__name__)

access_id=""
secret_key=""

#home routes 

@app.route('/login')
def login_aws_page():
    return render_template('login.html')

@app.route('/setcreds', methods=["POST"])
def creds():
    if request.method == "POST":
        global access_id, secret_key
        access_id = request.form['aci']
        secret_key = request.form['sak']
        return redirect(url_for('index'))

@app.route("/")
def index():
    return render_template('index.html')


#ec2 Routes

@app.route("/ec2")
def ec2():
    return render_template('ec2.html')

@app.route('/create')
def create():
    create_instance.create_ec2instance(access_id,secret_key)
    return redirect(url_for('list'))

@app.route('/list')
def list():
    all_instances=[]
    response = show_instances.get_all_instances(access_id,secret_key)
    # print("Response",response)
    for reservation in response:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_state = instance['State']['Name']
            if instance_state == 'running':
                public_ip = instance["PublicIpAddress"]
                private_ip = instance["PrivateIpAddress"]
            else:
                public_ip = '-'
                private_ip = '-'
            all_instances.append([instance_id,instance_state,public_ip,private_ip])
    return render_template('list.html',instances=all_instances)

@app.route('/stop')
def stop():
    return render_template('stop.html')

@app.route('/stop_inst', methods=["POST"])
def stop_inst():
    if request.method=="POST":
        id = request.form['id']
        stop_instance.stop(id,access_id, secret_key)
        return redirect(url_for('list'))

@app.route('/start')
def start():
    return render_template('start.html')

@app.route('/start_inst', methods=["POST"])
def start_inst():
    if request.method=="POST":
        id = request.form['id']
        start_instance.start(id,access_id, secret_key)
        return redirect(url_for('list'))

@app.route('/terminate')
def terminate():
    return render_template('terminate.html')

@app.route('/terminate_inst', methods=["POST"])
def terminate_inst():
    if request.method=="POST":
        id = request.form['id']
        terminate_instance.terminate(id,access_id, secret_key)
        return redirect(url_for('list'))

#s3 Routes

@app.route("/s3bucket")
def s3bucket():
    return render_template('s3bucket.html')

@app.route('/createbucket')
def createbucket():
    return render_template('createbucket.html')

@app.route('/cbucket', methods=["POST"])
def cbucket():
    if request.method=="POST":
        name = request.form['bn']
        create_bucket.create(name, access_id, secret_key)
        return redirect(url_for('listbucket'))

@app.route('/listbucket')
def listbucket():
    response = list_bucket.list(access_id, secret_key)
    return render_template('listbucket.html',response = response)
    # for bucket in response['Buckets']:
    #     print(bucket['Name'])

@app.route('/deletebucket')
def deletebucket():
    return render_template('deletebucket.html')

@app.route('/dbucket', methods=["POST"])
def dbucket():
    if request.method=="POST":
        name = request.form['bn']
        delete_bucket.delete(name, access_id, secret_key)
        return redirect(url_for('listbucket')) 

# IAM routes

@app.route('/iam')
def iam():
    return render_template('iam.html')

@app.route('/createuser')
def createuser():
    return render_template('create_user.html')

@app.route('/createduser', methods=["POST"])
def cuser():
    if request.method=="POST":
        name = request.form["username"]
        create_user.create(name)
        return redirect(url_for('listuser'))

@app.route('/listuser')
def listuser():
    users = list_user.list()
    return render_template('list_user.html',users=users)
    
@app.route('/deleteuser')
def deleteuser():
    return render_template('delete_user.html')

@app.route('/deleteduser', methods=["POST"])
def duser():
    if request.method=="POST":
        name = request.form["username"]
        delete_user.delete(name)
        return redirect(url_for('listuser'))

#progress routes

@app.route("/inprogress")
def progress():
    return render_template('inprogress.html')

if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host="",port="",debug=True)