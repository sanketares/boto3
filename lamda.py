import boto3

# Create a session
session = boto3.Session()

# Create a Lambda client
lambda_client = session.client('lambda')

# List Lambda functions
response = lambda_client.list_functions()


print("Lambda Functions:")
for function in response['Functions']:
    function_name = function['FunctionName']
    # Get detailed information about the function
    function_details = lambda_client.get_function(FunctionName=function_name)
    print(f"  Function Name: {function['FunctionName']}, Runtime: {function['Runtime']}")
    print(f"  Function Name: {function_details['Configuration']['FunctionName']}")
    print(f"  Runtime: {function_details['Configuration']['Runtime']}")
    print(f"  Handler: {function_details['Configuration']['Handler']}")
    print(f"  Role: {function_details['Configuration']['Role']}")
    print(f"  Description: {function_details['Configuration'].get('Description', 'No description')}")
    print(f"  Timeout: {function_details['Configuration']['Timeout']} seconds")
    print(f"  Memory Size: {function_details['Configuration']['MemorySize']} MB")
    print(f"  Last Modified: {function_details['Configuration']['LastModified']}")
    print(f"  State: {function_details['Configuration']['State']}")
    print("  ---")
