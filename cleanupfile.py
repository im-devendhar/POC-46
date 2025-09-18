import boto3 
import datetime 
ec2 = boto3.client('ec2') 
 def cleanup_unattached_volumes(): 
    volumes = ec2.describe_volumes(Filters=[{'Name': 'status', 'Values': ['available']}])['Volumes'] 
    for vol in volumes: 
        print(f"Unattached Volume: {vol['VolumeId']}") 
        ec2.delete_volume(VolumeId=vol['VolumeId']) 
 def cleanup_stopped_instances(): 
    instances = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}]) 
    for reservation in instances['Reservations']: 
        for instance in reservation['Instances']: 
            print(f"Stopped Instance: {instance['InstanceId']}") 
            ec2.terminate_instances(InstanceIds=[instance['InstanceId']]) 
 def cleanup_unused_elastic_ips(): 
    addresses = ec2.describe_addresses()['Addresses'] 
    for addr in addresses: 
        if 'InstanceId' not in addr: 
            print(f"Unused Elastic IP: {addr['AllocationId']}") 
            ec2.release_address(AllocationId=addr['AllocationId']) 
 def cleanup_old_snapshots(days_old=30): 
    snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots'] 
    cutoff = datetime.datetime.utcnow() - datetime.timedelta(days=days_old) 
    for snap in snapshots: 
        start_time = snap['StartTime'].replace(tzinfo=None) 
        if start_time < cutoff: 
            print(f"Old Snapshot: {snap['SnapshotId']} from {start_time}") 
            ec2.delete_snapshot(SnapshotId=snap['SnapshotId']) 
 if __name__ == "__main__": 
    print("Starting AWS Cleanup PoC...") 
    cleanup_unattached_volumes() 
    cleanup_stopped_instances() 
    cleanup_unused_elastic_ips() 
    cleanup_old_snapshots() 
    print("Cleanup scan completed.") 
