from dotenv import load_dotenv
# import tiktoken
from openai import OpenAI

load_dotenv()
# client = OpenAI()
client = OpenAI(
    api_key="AIzaSyBOGZQAyjqxnTGQTvXbQf_hy0TpcQmbJ9E",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

result = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {"role": "system", "content": "your name is aman and give the answer only related to python code otherwise just say sorry."},
        { "role":"user","content":"coroutine' object has no attribute 'text' what is this error" }
    ]
)

print(result.choices[0].message.content)
