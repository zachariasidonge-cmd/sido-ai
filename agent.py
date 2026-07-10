# agent.py - Simplified version without langchain.agents (works on Render)
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

# Initialize the LLM with Groq
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile",
    temperature=0.7
)

# Simple memory - store chat history
chat_history = []

# Import tool functions directly for use in responses
from tools import (
    business_plan_tool,
    cv_writer_tool,
    invoice_generator_tool,
    proposal_writer_tool,
    marketing_writer_tool,
    tender_finder_tool,
    job_finder_tool,
    web_search_tool,
    business_registration_tool,
    kra_tax_tool,
    market_prices_tool,
    county_permit_tool
)

# Map keywords to tool functions
TOOL_MAP = {
    "business plan": business_plan_tool,
    "cv": cv_writer_tool,
    "invoice": invoice_generator_tool,
    "proposal": proposal_writer_tool,
    "marketing": marketing_writer_tool,
    "tender": tender_finder_tool,
    "job": job_finder_tool,
    "search": web_search_tool,
    "register": business_registration_tool,
    "registration": business_registration_tool,
    "tax": kra_tax_tool,
    "calculate tax": kra_tax_tool,
    "price": market_prices_tool,
    "market": market_prices_tool,
    "permit": county_permit_tool,
    "county": county_permit_tool
}

def detect_tool(user_input: str):
    """Detect which tool to use based on keywords"""
    input_lower = user_input.lower()
    for keyword, tool_func in TOOL_MAP.items():
        if keyword in input_lower:
            return tool_func
    return None

def get_response(user_input: str) -> str:
    """Main entry point for Sido AI"""
    try:
        # Check if we should use a specific tool
        tool_func = detect_tool(user_input)
        
        if tool_func:
            # Use the tool directly
            return tool_func(user_input)
        
        # Otherwise, use the LLM for general conversation
        messages = [
            {"role": "system", "content": """You are Sido AI, Kenya's smartest digital business assistant.
Your mission: Help Kenyans start, run, and grow businesses.

Guidelines:
- Always use Kenyan examples (M-Pesa, KSh, Kenyan counties, local businesses)
- Be practical and action-oriented
- Suggest the next step after every response
- Use Swahili phrases occasionally (like 'Habari', 'Karibu', 'Sawa', 'Asante')
- Be concise but thorough
- If someone asks for a business plan, CV, invoice, proposal, tax calculation, market prices, county permits, or business registration - provide a comprehensive Kenyan-focused response
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