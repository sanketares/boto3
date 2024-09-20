import boto3

def get_unused_snapshots():
    ec2 = boto3.client('ec2')
    
    # Retrieve all snapshots
    snapshots_response = ec2.describe_snapshots(OwnerIds=['self'])
    snapshots = snapshots_response['Snapshots']
    
    # Retrieve all volumes
    volumes_response = ec2.describe_volumes()
    volumes = volumes_response['Volumes']
    
    # Create a set of volume IDs to check against
    volume_ids = {volume['VolumeId'] for volume in volumes}

    unused_snapshots = []
    
    # Check each snapshot to see if it's attached to a volume
    for snapshot in snapshots:
        if 'VolumeId' in snapshot:
            if snapshot['VolumeId'] not in volume_ids:
                unused_snapshots.append(snapshot)
    
    return unused_snapshots

if __name__ == "__main__":
    unused_snapshots = get_unused_snapshots()
    if unused_snapshots:
        print("Unused Snapshots:")
        for snapshot in unused_snapshots:
            print(f"Snapshot ID: {snapshot['SnapshotId']}, Start Time: {snapshot['StartTime']}, Description: {snapshot.get('Description', 'N/A')}")
    else:
        print("No unused snapshots found.")
