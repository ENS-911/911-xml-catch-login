import json

def lambda_handler(event, context):
    try:
        print("Received event:", event)

        users = {
            "hamiltoncounty911": "P9x7!aQ2#Wd8@Lf3"
        }
        print("User dictionary loaded.")

        username = event.get('username')
        password = event.get('password')

        print(f"Username: {username}")
        print(f"Password: {password}")

        if username in users and users[username] == password:
            print(f"Authentication successful for user: {username}")
            response = {
                "Role": "arn:aws:iam::527618457101:role/SFTPUserRole",
                "Policy": "",
                "HomeDirectoryDetails": [
                    {
                        "Entry": "/",
                        "Target": "arn:aws:s3:::ens-file-store/hamiltoncounty911"
                    }
                ],
                "HomeDirectoryType": "LOGICAL"
            }
            print("Preparing to return response.")
            print("Returning response:", json.dumps(response))  # Log the response
            return response
        else:
            print(f"Authentication failed for user: {username}")
            raise Exception("Invalid username or password")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise
