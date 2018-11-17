#!/usr/bin/env python
# deploy services to local k8s cluster
import os
import subprocess
import time

from boto3.session import Session


def get_client():
    session = Session(
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_DEFAULT_REGION')
    )
    return session.client('sqs')

def get_queue_url(client):
    response = client.get_queue_url(
        QueueName='DevFest'
    )
    return response['QueueUrl']

def delete_msg(client, queue_url, receipt):
    response = client.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt
    )

def deploy_services():
    # I don't feel like walking trees for a demo
    subprocess.run(['bash', 'deploy.sh']) # or checking errors lol
    print('[+] Services deployed!')
    return True

def listen_and_respond(client, queue_url):
    while True:
        message = client.receive_message(
            QueueUrl=queue_url,
            AttributeNames=['All'],
            MaxNumberOfMessages=1,
            VisibilityTimeout=10,
            WaitTimeSeconds=5
        )
        if message.get('Messages'):
            msg = message.get('Messages')[0]
            receipt = msg['ReceiptHandle']
            if deploy_services():
                delete_msg(client, queue_url, receipt)

if __name__ == '__main__':
    client = get_client()
    queue_url = get_queue_url(client)
    listen_and_respond(client, queue_url)
