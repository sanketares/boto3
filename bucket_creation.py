import boto3

# Specify the desired region
region = 'us-west-2'  # Change this to your desired region

client = boto3.client('s3', region_name=region)
response = client.create_bucket(
    Bucket='sanket123asd',
    CreateBucketConfiguration={
        'LocationConstraint': region
    }
)

print(response)
