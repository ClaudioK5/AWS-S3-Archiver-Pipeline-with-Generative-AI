import boto3
from AI_report_sender import AI_report_sender
from aws_filetextretriever_tools import pdf_file_text_extractor, txt_file_text_extractor

s3 = boto3.client("s3")


def AI_report_maker(files, bucket_name):

    prompt = ""

    for key in files:

        response = s3.get_object(Bucket=bucket_name, Key=key)
        body = response["Body"].read()

        if key.endswith(".pdf"):

            title = f"\n\n File : {key}\n\n"

            prompt += title + pdf_file_text_extractor(bucket_name, key)

        else:

            title = f"\n\n File : {key}\n\n"

            prompt += title + txt_file_text_extractor(bucket_name, key)


    new_prompt = """Hello Deepseek, The following content includes extracted documents and text files related to the current month.\n Generate a structured monthly report for the company and summarize key information, insights, and any relevant patterns or decisions based on the data.\n"""

    prompt = new_prompt + prompt

    AI_report_sender(prompt)




