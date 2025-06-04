import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def ask_gpt(text, question):
    messages = [
        {"role": "system", "content": "你是资深网络安全顾问，善于分析渗透测试结果。"},
        {"role": "user", "content": f"{question}\n\n{text}"}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )
    return response.choices[0].message.content.strip()

