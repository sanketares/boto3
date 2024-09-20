import boto3

# Create a session
session = boto3.Session()

# Create a CloudWatch client
cloudwatch = session.client('cloudwatch')

# Retrieve metrics
metrics = cloudwatch.list_metrics(DimensionName='InstanceId')

print("CloudWatch Metrics:")
for metric in metrics['Metrics']:
    print(f"  Metric Name: {metric['MetricName']}, Namespace: {metric['Namespace']}")
