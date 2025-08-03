import boto3
import botocore
import re
from regex_patterns import credential_patterns

def scan_s3_bucket(bucket_name, delete_flag=False):
    s3 = boto3.client('s3')
    findings = []

    try:
        # List all objects in the bucket
        objects = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' not in objects:
            print(f" No objects found in bucket: {bucket_name}")
            return findings

        for obj in objects['Contents']:
            key = obj['Key']
            # Skip files that are likely too large or binary
            if not key.lower().endswith(('.txt', '.json', '.py', '.env', '.cfg', '.ini', '.yaml')):
                continue

            try:
                content_obj = s3.get_object(Bucket=bucket_name, Key=key)
                content = content_obj['Body'].read().decode('utf-8', errors='ignore')

                for pattern_name, pattern in credential_patterns.items():
                    match = re.search(pattern, content)
                    if match:
                        findings.append({
                            'key': key,
                            'match': pattern_name,
                            'snippet': match.group(0)[:100]
                        })
                        if delete_flag:
                            s3.delete_object(Bucket=bucket_name, Key=key)
                            print(f" Deleted flagged object: {key}")
                        break  # Only one match per file for now

            except botocore.exceptions.ClientError as e:
                print(f" Could not read object {key}: {e}")

    except Exception as e:
        print(f" Error scanning bucket: {e}")

    return findings
