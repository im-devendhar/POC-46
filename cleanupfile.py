import boto3
import datetime

ec2 = boto3.client('ec2')

def cleanup_unattached_volumes():
    volumes = ec2.describe_volumes(Filters=[{'Name': 'status', 'Values': ['available']}])['Volumes']
    for vol in volumes:
        print(f"Unattached Volume: {vol['VolumeId']}")
        ec2.delete_volume(VolumeId=vol['VolumeId'])

def cleanup_stopped_instances():
    instances = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            try:
                ec2.terminate_instances(InstanceIds=[instance_id])
                print(f"Stopped Instance: {instance_id}")
            except:
                pass  # silently skip errors

def cleanup_unused_elastic_ips():
    addresses = ec2.describe_addresses()['Addresses']
    for addr in addresses:
        if 'InstanceId' not in addr:
            allocation_id = addr.get('AllocationId')
            try:
                ec2.release_address(AllocationId=allocation_id)
                print(f"Unused Elastic IP: {allocation_id}")
            except:
                pass  # silently skip errors

def cleanup_old_snapshots(days_old=30):
    snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']
    cutoff = datetime.datetime.utcnow() - datetime.timedelta(days=days_old)
    for snap in snapshots:
        start_time = snap['StartTime'].replace(tzinfo=None)
        if start_time < cutoff:
            ec2.delete_snapshot(SnapshotId=snap['SnapshotId'])
            print(f"Old Snapshot: {snap['SnapshotId']}")

if __name__ == "__main__":
    print("Starting AWS Cleanup PoC...")
    cleanup_unattached_volumes()
    cleanup_stopped_instances()
    cleanup_unused_elastic_ips()
    cleanup_old_snapshots()
    print("Cleanup scan completed.")
