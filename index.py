import json

def lambda_handler(event, context):
    print(f"Event received: {json.dumps(event)}")

    # Local dictionary of authorized users
    # Key: username, Value: password
    users = {
        "hamiltoncounty911": "P9x7!aQ2#Wd8@Lf3"
    }

    required_keys = ["username", "password", "serverId", "sourceIp"]
    for key in required_keys:
        if key not in event:
            raise ValueError(f"Missing required key: {key}")

    username = event["username"]
    password = event["password"]

    # Validate username and password
    if username not in users or users[username] != password:
        print("Invalid username or password")
        # Raise an exception to indicate authentication failure
        raise Exception("Unauthorized")

    # Construct the home directory details
    # IMPORTANT: Ensure the prefix ends with '/' to represent a directory
    home_directory_details = [
        {
            "Entry": "/",
            "Target": "arn:aws:s3:::ens-file-store/hamiltoncounty911/"
        }
    ]

    response = {
        "Role": "arn:aws:iam::527618457101:role/SFTPUserRole",
        "Policy": "",
        "HomeDirectoryType": "LOGICAL",
        "HomeDirectoryDetails": json.dumps(home_directory_details)
    }

    print(f"Returning response: {json.dumps(response)}")
    return response

