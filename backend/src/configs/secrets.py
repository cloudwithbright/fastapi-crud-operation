import os
import json
import boto3
from botocore.exceptions import ClientError

SECRETS_NAME=os.getenv("SECRETS_NAME")
REGION_NAME=os.getenv("REGION_NAME")

def get_secret():

    secret_name = SECRETS_NAME
    region_name = REGION_NAME

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )

        return json.loads(get_secret_value_response['SecretString'])
    
    except ClientError as e:
        print(e)