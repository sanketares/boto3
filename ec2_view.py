import boto3

def create_session(region_name):
    return boto3.Session(region_name=region_name)

def list_running_instances(ec2):
    filters = [{'Name': 'instance-state-name', 'Values': ['running']}]
    running_instances = ec2.instances.filter(Filters=filters)

    print("Running EC2 Instances:")
    for instance in running_instances:
        print(f"- Instance ID: {instance.id}, State: {instance.state['Name']}")

def list_stopped_instances(ec2):
    filters = [{'Name': 'instance-state-name', 'Values': ['stopped']}]  # Corrected spelling from 'stoped' to 'stopped'
    stopped_instances = ec2.instances.filter(Filters=filters)

    print("Stopped EC2 Instances:")
    for instance in stopped_instances:
        print(f"- Instance ID: {instance.id}, State: {instance.state['Name']}")

def start_first_stopped_instance(ec2_client, instance_ids):
    if instance_ids:
        ec2_client.start_instances(InstanceIds=[instance_ids[0]])
        print(f"Starting instance: {instance_ids[0]}")
    else:
        print("No stopped instances to start.")

def list_snapshots(ec2_client):
    response = ec2_client.describe_snapshots(OwnerIds=['self'])  # Use ['self'] for your own snapshots

    print("EBS Snapshots:")
    for snapshot in response['Snapshots']:
        print(f"- Snapshot ID: {snapshot['SnapshotId']}, State: {snapshot['State']}, Description: {snapshot.get('Description', 'No description')}")


def list_iam_users(iam_client):
    response = iam_client.list_users()
    print("IAM Users:")
    for user in response['Users']:
        print(f"- User Name: {user['UserName']}, User ID: {user['UserId']}")

if __name__ == "__main__":
    # Input for region
    region_name = input("Enter the AWS region (e.g., us-west-2): ")

    session = create_session(region_name)
    ec2_client = session.client('ec2')
    ec2 = session.resource('ec2')
    iam_client = session.client('iam')

    list_running_instances(ec2)
    stopped_instance_ids = list_stopped_instances(ec2)
    start_first_stopped_instance(ec2_client, stopped_instance_ids) 
    list_snapshots(ec2_client)
    list_iam_users(iam_client)
