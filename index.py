import json

def lambda_handler(event, context):
    # Simple credential check
    users = {
        "hamiltoncounty911": "P9x7!aQ2#Wd8@Lf3"
    }

    username = event.get("username")
    password = event.get("password")

    if username not in users or users[username] != password:
        raise Exception("Unauthorized")

    response = {
        "Role": "arn:aws:iam::527618457101:role/SFTPUserRole",
        "HomeDirectoryType": "PATH",
        "HomeDirectory": "/hamiltoncountytn/xml"
    }

    print(f"Returning response: {json.dumps(response)}")
    return response
