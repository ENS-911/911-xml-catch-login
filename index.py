import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    # Example credentials stored in a dictionary for demonstration
    # Use a secure database like DynamoDB in production
    users = {
        "hamiltoncounty911": "P9x7!aQ2#Wd8@Lf3"
    }

    username = event['username']
    password = event['password']

    if username in users and users[username] == password:
        # Authentication successful
        return {
            "Role": "arn:aws:iam::account-id:role/SFTPUserRole",
            "Policy": "",
            "HomeDirectoryDetails": [
                {
                    "Entry": "/",
                    "Target": f"arn:aws:s3:::ens-file-store/{username}"
                }
            ],
            "HomeDirectoryType": "LOGICAL"
        }
    else:
        # Authentication failed
        raise Exception("Invalid username or password")
