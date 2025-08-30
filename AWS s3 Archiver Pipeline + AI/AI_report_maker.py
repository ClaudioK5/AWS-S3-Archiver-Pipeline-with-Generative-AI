import boto3
from generate_Report import generate_AIreport
from aws_filetextretriever_tools import get_files_for_current_month, extract_text_from_pdf_stream, scanx3_grab_all_text

s3 = boto3.client("s3")

files = get_files_for_current_month("bucketname")


def AI_report_maker(files):

    prompt = ""

    for key in files:

        response = s3.get_object(Bucket="bucketname", Key=key)
        body = response["Body"].read()

        if key.endswith(".pdf"):

            title = f"\n\n File : {key}\n\n"

            prompt += title + extract_text_from_pdf_stream("bucketname", key)

        else:

            title = f"\n\n File : {key}\n\n"

            prompt += title + scanx3_grab_all_text("bucketname", key)



    new_prompt = """Hello Deepseek, The following content includes extracted documents and text files related to the current month.\n Generate a structured monthly report for the company and summarize key information, insights, and any relevant patterns or decisions based on the data.\n"""

    prompt = new_prompt + prompt

    print(prompt)

    generate_AIreport(prompt)


AI_report_maker(files)

