import sys
import smtplib
from email.message import EmailMessage
import os

bot_email = os.getenv("BOT_EMAIL")
bot_email_password = os.getenv("BOT_EMAIL_PASSWORD")

def send_email(to_email, subject, body):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = bot_email
    msg['To'] = to_email
    msg.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(bot_email,bot_email_password)
        smtp.send_message(msg)

