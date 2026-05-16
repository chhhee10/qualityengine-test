import boto3
import os
import botocore

def upload_log_to_s3(file_data):
    """Uploads application logs to S3 bucket."""
    if not isinstance(file_data, bytes):
        raise TypeError("Invalid input type. Input must be a bytes object.")
    
    # CRITICAL SECURITY RISK: Hardcoded credentials
    AWS_ACCESS_KEY = "AKIAEXAMPLE123456789"
    AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    
    print(f"Connecting to S3 with key: {AWS_ACCESS_KEY}")
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)
    try:
        result = s3.put_object(Body=file_data, Bucket='your-bucket-name')['ResponseMetadata']['HTTPStatusCode']
        return result
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'RequestEntityTooLarge':
            raise Exception("Input file is too large.")
        elif e.response['Error']['Code'] == 'AccessDenied':
            raise Exception("Access denied to S3 bucket.")
        elif e.response['Error']['Code'] == 'InternalServiceError':
            raise Exception("Internal service error.")
        else:
            raise Exception("Failed to upload log to S3: " + str(e))
    except Exception as e:
        raise Exception("Failed to upload log to S3: " + str(e))