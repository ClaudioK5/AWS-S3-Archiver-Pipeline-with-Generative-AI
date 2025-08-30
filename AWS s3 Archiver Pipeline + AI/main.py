from aws_archive_tools import normalize_bucket
from AI_report_maker import AI_report_maker

bucket_name = "bucketname"

print(f"Running normalization on bucket: {'bucketname'}")

normalize_bucket(bucket_name)

print("Normalization successfully completed.")
