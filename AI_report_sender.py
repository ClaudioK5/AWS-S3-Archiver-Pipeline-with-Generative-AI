from openai import OpenAI
from email_sender import send_email
import os

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1"
)


def AI_report_sender(prompt):


    try:
        response = client.chat.completions.create(model="deepseek-chat",
                                              messages=[{'role': 'user', 'content': prompt}],
                                              max_tokens=300)

        ai_output = response.choices[0].message.content.strip()

        subject = 'AI AWS report for the current month'

        send_email('insert here your email', subject, ai_output)

    except Exception as e:

        return {"error": str(e)}

