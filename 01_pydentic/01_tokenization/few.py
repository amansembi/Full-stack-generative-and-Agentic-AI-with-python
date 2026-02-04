from dotenv import load_dotenv
# import tiktoken
from openai import OpenAI

load_dotenv()
# client = OpenAI()
client = OpenAI(
    api_key="AIzaSyBOGZQAyjqxnTGQTvXbQf_hy0TpcQmbJ9E",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)
SYSTEM_INTRO ="""
your name is aman and give the answer only related to python code otherwise just say sorry.

Q if ask the question out of python programming then give me the ans in json
A {{ "code":"null","isCoding":"false}}

Q if ask the python program then give the ans in json 
A {{"code":"write code here","isCoding":"true"}}
"""
result = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {"role": "system", "content": SYSTEM_INTRO},
        { "role":"user","content":"give me a good jok" }
    ]
)

print(result.choices[0].message.content)
