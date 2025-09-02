import io
import boto3
from pdfminer.high_level import extract_text
from datetime import datetime

s3 = boto3.client("s3")


def pdf_file_text_extractor(bucket_name: str, key: str):

    try:

        obj = s3.get_object(Bucket=bucket_name, Key=key)
        pdf_bytes = obj['Body'].read()

        return extract_text(io.BytesIO(pdf_bytes))

    except Exception as e:

        print(f"Error reading PDF {key}: {e}")

        return ""



def txt_file_text_extractor(bucket_name: str, key: str):
    try:
        obj = s3.get_object(Bucket=bucket_name, Key=key)
        body = obj['Body'].read()

        return body.decode("utf-8", errors="ignore")

    except Exception as e:

        print(f"Error reading {key}: {e}")

        return ""



def get_files_for_current_month(bucket_name: str):

    s3 = boto3.client("s3")

    now = datetime.now()
    year = now.year
    month = now.month

    prefix = f"{year}/{month:02d}"

    paginator = s3.get_paginator("list_objects_v2")

    files = []

    for page in paginator.paginate(Bucket=bucket_name, Prefix=prefix):

        for obj in page.get("Contents", []):

            key = obj["Key"]

            if not key.endswith("/"):

                files.append(key)

    return files





