from google import genai
API_KEY="Your_API_Key"
client=genai.Client( api_key=API_KEY)
print("simple AI Agent")
print("Type 'exit' to quit.\n")
while True:
    user=input("you:")
    if user.lower()=="exit":
        break
    response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents=user
)
    print("AI:",response.text)