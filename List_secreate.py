import boto3
from botocore.exceptions import ClientError

def list_secrets(region_name):
    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region_name)

    try:
        # List secrets
        response = client.list_secrets()
        secrets = response['SecretList']

        # Print secret names and ARNs
        for secret in secrets:
            print(f"Name: {secret['Name']}, ARN: {secret['ARN']}")

    except ClientError as e:
        print(f"Error listing secrets: {e}")

# Example usage
if __name__ == "__main__":
    region_name = "us-ease-1"  # e.g., "us-west-2"
    list_secrets(region_name)
