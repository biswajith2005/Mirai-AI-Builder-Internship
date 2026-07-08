from google import genai

client = genai.Client(api_key="Enter your API")
response=client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain to me how does a redis work in one sentence"
)
print(response)