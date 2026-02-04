from dotenv import load_dotenv
# import tiktoken
from openai import OpenAI

load_dotenv()
# client = OpenAI()
client = OpenAI(
    api_key="AIzaSyBOGZQAyjqxnTGQTvXbQf_hy0TpcQmbJ9E",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)
# enc = tiktoken.encoding_for_model("gpt-4o")
# text = "hay there! my name is amrinder singh"
# text = "Hey There! My name is Piyush Garg"
# token = enc.encode(text)
# [39679, 1354, 0, 922, 1308, 382, 939, 81, 5508, 6211, 71]
# print("Token:= ",token)

# decode = enc.decode([25216, 3274, 0, 3673, 1308, 382, 398, 3403, 1776, 170676, 89])
# print("decode =: ", decode)

# response = client.chat.completions.create(
#     model="gemini-3-flash-preview",
#     input="Hey Amrinder singh this side tell me about you"
# )
result = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        { "role":"user","content":"Hey Amrinder singh this side tell me about you" }
    ]
)

print(result.choices[0].message)
