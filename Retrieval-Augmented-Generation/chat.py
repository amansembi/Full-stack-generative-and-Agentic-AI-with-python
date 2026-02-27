from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

load_dotenv()
client = OpenAI()
embedding_model = OpenAIEmbeddings(
    model = "text-embedding-3-large"
)

vector_db = QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="nodejs_rag"
)
user_query = input("Ask something 🫴 ")
search_results = vector_db.similarity_search(query=user_query)

context = "\n\n\n".join([f"Page Content: {result.page_content} \n Page Number: {result.metadata['page_label']}\n File Location: {result.metadata['source']}"
                         for result in search_results])

SYSTEM_PROMPT = """
You are a helpfull ai assistant who answeres user query based on the available context retrieved from the pdf file along with page_contents ans page number.

You should only ans the user based on the following context and navigate the user to open the right page number to know more.

Context:
{context}

"""

response = client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role":"system", "content":SYSTEM_PROMPT},
        {"role":"user", "content":user_query}
    ]
)
print(f"🧁: {response.choices[0].message.content}")

# message_history = [
#     { "role": "system", "content": SYSTEM_PROMPT },
# ]