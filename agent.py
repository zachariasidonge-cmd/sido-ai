# agent.py - Updated with better payment detection
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import re

load_dotenv()

# Initialize the LLM with Groq
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile",
    temperature=0.7
)

# Simple memory - store chat history
chat_history = []

# Import tool functions
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
    county_permit_tool,
    mpesa_payment_tool,  # Import M-Pesa tool
    pdf_export_tool,     # Import PDF tool
    voice_input_tool     # Import Voice tool
)

# Map keywords to tool functions - IMPROVED
TOOL_MAP = {
    # Business tools
    "business plan": business_plan_tool,
    "plan for": business_plan_tool,
    "create a business": business_plan_tool,
    
    # CV tools
    "cv": cv_writer_tool,
    "resume": cv_writer_tool,
    "write my cv": cv_writer_tool,
    
    # Invoice tools
    "invoice": invoice_generator_tool,
    "generate an invoice": invoice_generator_tool,
    
    # Proposal tools
    "proposal": proposal_writer_tool,
    "write a proposal": proposal_writer_tool,
    
    # Marketing tools
    "marketing": marketing_writer_tool,
    "social media": marketing_writer_tool,
    "facebook": marketing_writer_tool,
    "instagram": marketing_writer_tool,
    "tiktok": marketing_writer_tool,
    
    # Tender tools
    "tender": tender_finder_tool,
    "find tenders": tender_finder_tool,
    
    # Job tools
    "job": job_finder_tool,
    "find jobs": job_finder_tool,
    "job search": job_finder_tool,
    
    # Search tools
    "search": web_search_tool,
    "find": web_search_tool,
    
    # Registration tools
    "register": business_registration_tool,
    "registration": business_registration_tool,
    "business registration": business_registration_tool,
    
    # Tax tools
    "tax": kra_tax_tool,
    "calculate tax": kra_tax_tool,
    "paye": kra_tax_tool,
    "nhif": kra_tax_tool,
    "nssf": kra_tax_tool,
    
    # Market price tools
    "price": market_prices_tool,
    "market": market_prices_tool,
    "cost of": market_prices_tool,
    
    # County permit tools
    "permit": county_permit_tool,
    "county": county_permit_tool,
    
    # M-Pesa Payment tools - NEW AND IMPROVED
    "pay": mpesa_payment_tool,
    "payment": mpesa_payment_tool,
    "mpesa": mpesa_payment_tool,
    "lipa": mpesa_payment_tool,
    "send money": mpesa_payment_tool,
    "transfer": mpesa_payment_tool,
    "till": mpesa_payment_tool,
    "paybill": mpesa_payment_tool,
    
    # PDF tools
    "pdf": pdf_export_tool,
    "generate pdf": pdf_export_tool,
    "download": pdf_export_tool,
    
    # Voice tools
    "speak": voice_input_tool,
    "voice": voice_input_tool,
    "listen": voice_input_tool,
    "say": voice_input_tool
}

def detect_tool(user_input: str):
    """Detect which tool to use based on keywords - IMPROVED for payments"""
    input_lower = user_input.lower()
    
    # Special detection for payment keywords
    payment_keywords = ["pay", "payment", "mpesa", "lipa", "till", "send money", "transfer"]
    for keyword in payment_keywords:
        if keyword in input_lower:
            return mpesa_payment_tool
    
    # Check for PDF keywords
    pdf_keywords = ["pdf", "generate pdf", "download"]
    for keyword in pdf_keywords:
        if keyword in input_lower:
            return pdf_export_tool
    
    # Check for voice keywords
    voice_keywords = ["speak", "voice", "listen", "say"]
    for keyword in voice_keywords:
        if keyword in input_lower:
            return voice_input_tool
    
    # Regular tool detection
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