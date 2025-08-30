from openai import OpenAI
from email_sender import send_email

client = OpenAI(
    api_key="insert your deepseek api key here",
    base_url="https://api.deepseek.com/v1"
)

def generate_AIreport(prompt):


    try:
        response = client.chat.completions.create(model="deepseek-chat",
                                              messages=[{'role': 'user', 'content': prompt}],
                                              max_tokens=300)

        ai_output = response.choices[0].message.content.strip()

        print(ai_output)

        subject = 'AI AWS report for the current month '

        send_email('insert your email', subject, ai_output)

        print("email sent successfully!")

    except Exception as e:

        return {"error": str(e)}