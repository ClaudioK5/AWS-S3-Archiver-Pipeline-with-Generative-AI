from aws_archive_tools import s3_files_archiver
from AI_report_maker import AI_report_maker
from datetime import datetime, timedelta
from aws_filetextretriever_tools import get_files_for_current_month
import time
import os

bucket_name = os.getenv("BUCKET_NAME")

#the archiviation operation will take place once everyday, meanwhile the
#generative AI report will be made on the last day of each month.

while True:

    today = datetime.today()


    s3_files_archiver(bucket_name)


    if (today + timedelta(days=1)).day == 1:

        files = get_files_for_current_month(bucket_name)

        AI_report_maker(files, bucket_name)

    time.sleep(86400)





