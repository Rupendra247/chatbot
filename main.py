import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")

client = genai.Client(api_key=api_key)

# Updated model version
chat = client.chats.create(model="gemini-3.5-flash")

print("Gemini Chatbot Initialized! Type 'exit' or 'quit' to end.\n")

while True:
    try:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        
        if not user_input.strip():
            continue

        response = chat.send_message(user_input)
        print(f"\nGemini: {response.text}\n")
        
    except Exception as e:
        print(f"\nAn error occurred: {e}\nPlease try again.\n")