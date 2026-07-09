# agent.py - Using Groq with current models
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

# Initialize the LLM with Groq - USING CURRENT MODELS
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile",  # ✅ Current, fast, and free!
    temperature=0.7
)

# Simple memory - store chat history
chat_history = []

def get_response(user_input: str) -> str:
    """Main entry point for Sido AI"""
    try:
        # Build messages with system prompt
        messages = [
            {"role": "system", "content": """You are Sido AI, Kenya's smartest digital business assistant.
Your mission: Help Kenyans start, run, and grow businesses.

Guidelines:
- Always use Kenyan examples (M-Pesa, KSh, Kenyan counties, local businesses like salons, restaurants, shops)
- Be practical and action-oriented
- Suggest the next step after every response
- Use Swahili phrases occasionally (like 'Habari', 'Karibu', 'Sawa', 'Asante')
- Be concise but thorough
- If someone asks for a business plan, CV, invoice, or proposal - create one for them!
- Be friendly and encouraging

Remember: You're helping Kenyan entrepreneurs, freelancers, and job seekers!"""}
        ]
        
        # Add chat history (last 10 messages)
        for msg in chat_history[-10:]:
            messages.append(msg)
        
        # Add current message
        messages.append({"role": "user", "content": user_input})
        
        # Get response from Groq
        response = llm.invoke(messages)
        
        # Save to history
        chat_history.append({"role": "user", "content": user_input})
        chat_history.append({"role": "assistant", "content": response.content})
        
        return response.content
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

if __name__ == "__main__":
    print("🤖 Sido AI: Habari! How can I help your business today?")
    print("Type 'exit' to quit\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Sido AI: Karibu tena! 🇰🇪")
            break
        response = get_response(user_input)
        print(f"\nSido AI: {response}\n")