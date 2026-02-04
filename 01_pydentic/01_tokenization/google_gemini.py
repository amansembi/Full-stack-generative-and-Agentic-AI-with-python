from dotenv import load_dotenv

from google import genai
load_dotenv()

client = genai.Client(
    api_key="AIzaSyBOGZQAyjqxnTGQTvXbQf_hy0TpcQmbJ9E"
)

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="i want to kanow weather today of punjab"
)
print(response.text)