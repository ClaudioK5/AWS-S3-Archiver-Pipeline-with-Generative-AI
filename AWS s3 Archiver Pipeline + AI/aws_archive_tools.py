import os
import boto3
from datetime import timezone
from botocore.exceptions import ClientError

s3 = boto3.client("s3")

def key_exists(bucket, key):

    try:
        s3.head_object(Bucket=bucket, Key=key)

        return True

    except ClientError as e:

        if e.response['Error']['Code'] == "404":

            return False

def safe_key(bucket, target_key):

    if key_exists(bucket, target_key) == False:

        return target_key

    base, ext = os.path.splitext(target_key)

    i = 1

    while True:

        new_key = f"{base}_{i}{ext}"

        if not key_exists(bucket, new_key):

            return new_key

        i += 1

def normalize_bucket(bucket_name):

    paginator = s3.get_paginator("list_objects_v2")

    changes = []

    for page in paginator.paginate(Bucket=bucket_name):

        for obj in page.get("Contents", []):

            key = obj["Key"]

            if key.endswith("/"):

                continue

            last_modified = obj["LastModified"].astimezone(timezone.utc)

            year = last_modified.year
            month = last_modified.month
            filename = os.path.basename(key)
            new_key = f"{year}/{month:02d}/{filename}"

            if key == new_key:

                continue

            safe_new_key = safe_key(bucket_name, new_key)

            changes.append((key, safe_new_key))


            s3.copy_object(Bucket=bucket_name, CopySource = {"Bucket": bucket_name, "Key": key}, Key=safe_new_key)

            s3.delete_object(Bucket=bucket_name, Key=key)

    return changes

def list_files_for_month(bucket_name, year, month):

    prefix = f"{year}/{month:02d}/"

    paginator = s3.get_paginator("list_objects_v2")

    files = []

    for page in paginator.paginate(Bucket=bucket_name, Prefix=prefix):

        for obj in page.get("Contents", []):

            key = obj["Key"]

            if not key.endswith("/"):

                files.append(key)

    return files