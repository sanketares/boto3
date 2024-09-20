import boto3


session = boto3.Session()

s3 = session.client('s3')

def list_buckets():
    response = s3.list_buckets()
    buckets = response.get('Buckets',[])

    print("s3 bucket:")
    for buckets in buckets:
        print(f"-{buckets['Name']}")


def create_buckets():
    response = s3.create_buckets(Buckets=bucket_name)
    print(f"Buckets '{bucket_name}' created successfully.")

        


if __name__ == "__main__":
    list_buckets()
    new_bucket_name = "your-new-bucket-names1"
    create_buckets(new_bucket_name)