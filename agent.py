# agent.py - Complete Sido AI Agent with All Tools
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain.tools import Tool
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
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

load_dotenv()

# Initialize the LLM with Groq
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile",
    temperature=0.7
)

# Define all available tools
tools = [
    Tool(name="BusinessPlanGenerator", func=business_plan_tool, description="Generate a complete business plan for any Kenyan business idea"),
    Tool(name="CVWriter", func=cv_writer_tool, description="Write or optimize a CV/Resume for Kenyan job market"),
    Tool(name="InvoiceGenerator", func=invoice_generator_tool, description="Create a professional invoice in KSh"),
    Tool(name="ProposalWriter", func=proposal_writer_tool, description="Write a business or tender proposal"),
    Tool(name="MarketingWriter", func=marketing_writer_tool, description="Create marketing content for social media, emails, or ads"),
    Tool(name="TenderFinder", func=tender_finder_tool, description="Find latest Kenyan government and corporate tenders"),
    Tool(name="JobFinder", func=job_finder_tool, description="Find job opportunities in Kenya"),
    Tool(name="WebSearch", func=web_search_tool, description="Search the web for general business information"),
    Tool(name="BusinessRegistration", func=business_registration_tool, description="Step-by-step guide to register a business in Kenya"),
    Tool(name="KRATaxCalculator", func=kra_tax_tool, description="Calculate PAYE, NHIF, NSSF, and other Kenyan taxes"),
    Tool(name="MarketPrices", func=market_prices_tool, description="Get current market prices for common goods in Kenya"),
    Tool(name="CountyPermits", func=county_permit_tool, description="Get business permit requirements for Kenyan counties")
]

# Memory - remember conversation
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# Custom prompt for Kenyan context
prompt = ChatPromptTemplate.from_messages([
    ("system", """You are Sido AI, Kenya's smartest digital business assistant.
Your mission: Help Kenyans start, run, and grow businesses.

Guidelines:
- Always use Kenyan examples (M-Pesa, KSh, Kenyan counties, local businesses)
- Be practical and action-oriented
- Suggest the next step after every response
- Use Swahili phrases occasionally (like 'Habari', 'Karibu', 'Sawa', 'Asante')
- Be concise but thorough
- If someone asks for a business plan, CV, invoice, proposal, tax calculation, market prices, county permits, or business registration - use the appropriate tool
- Be friendly and encouraging

Remember: You're helping Kenyan entrepreneurs, freelancers, and job seekers!"""),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

# Create the agent
agent = create_agent(llm, tools, prompt)

# Create the executor
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=5
)

def get_response(user_input: str) -> str:
    """Main entry point for Sido AI"""
    try:
        response = agent_executor.invoke({
            "input": user_input
        })
        return response.get("output", "Sorry, I couldn't process that.")
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