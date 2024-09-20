import boto3



def create_ec2_instance():
    # Create EC2 resource
    ec2 = boto3.resource('ec2', region_name='us-west-2')  # Replace with your desired region

    # Create a new EC2 instance
    instances = ec2.create_instances(
        ImageId='ami-0a4a1990563b69037',  # Replace with a valid AMI ID
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
      # Replace with your subnet ID
    )

    print("EC2 Instance created:", instances[0].id)

if __name__ == "__main__":
    create_ec2_instance()
