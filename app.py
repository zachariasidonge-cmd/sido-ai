# app.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from agent import get_response  # This imports the function from agent.py
from agent import get_response
from datetime import datetime
from typing import Optional
import uvicorn

app = FastAPI(title="Sido AI - Kenyan Business Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    user_id: Optional[str] = "default"

class ChatResponse(BaseModel):
    response: str
    timestamp: str

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        response = get_response(request.message)
        return ChatResponse(
            response=response,
            timestamp=datetime.now().isoformat()
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "🇰🇪 Sido AI is running!", "status": "healthy"}

@app.get("/chat")
async def chat_ui():
    try:
        with open("templates/index.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        return HTMLResponse(content=html_content)
    except Exception as e:
        return HTMLResponse(content=f"<h1>Error loading template: {str(e)}</h1>", status_code=500)
<!DOCTYPE html>
<html>
<head>
    <title>Sido AI - Kenyan Business Assistant</title>
    <style>
        body { font-family: 'Segoe UI', Arial, sans-serif; background: #f5f5f5; margin: 0; padding: 0; }
        .chat-container { max-width: 800px; margin: 20px auto; background: white; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); overflow: hidden; }
        .header { background: linear-gradient(135deg, #006600, #009900); color: white; padding: 20px; text-align: center; }
        .header h1 { margin: 0; font-size: 28px; }
        .header p { margin: 5px 0 0; opacity: 0.9; }
        .messages { height: 450px; overflow-y: auto; padding: 20px; background: #fafafa; }
        .message { margin: 10px 0; padding: 12px 16px; border-radius: 8px; max-width: 80%; line-height: 1.5; }
        .user { background: #e3f2fd; margin-left: auto; text-align: right; border-bottom-right-radius: 4px; }
        .sido { background: #f1f8e9; border-left: 4px solid #006600; border-bottom-left-radius: 4px; }
        .sido strong { color: #006600; }
        .input-area { display: flex; padding: 16px 20px; background: white; border-top: 1px solid #e0e0e0; }
        input { flex: 1; padding: 12px; border: 2px solid #ddd; border-radius: 25px; font-size: 14px; outline: none; transition: border-color 0.3s; }
        input:focus { border-color: #009900; }
        button { padding: 12px 30px; background: #006600; color: white; border: none; border-radius: 25px; margin-left: 10px; cursor: pointer; font-weight: bold; transition: background 0.3s; }
        button:hover { background: #004d00; }
        .suggestions { display: flex; flex-wrap: wrap; gap: 8px; padding: 10px 20px; background: #f9f9f9; border-top: 1px solid #eee; }
        .suggestions button { padding: 8px 16px; background: #e8f5e9; color: #006600; border: 1px solid #a5d6a7; border-radius: 20px; font-size: 12px; margin: 0; cursor: pointer; }
        .suggestions button:hover { background: #c8e6c9; }
        @media (max-width: 600px) {
            .chat-container { margin: 10px; }
            .message { max-width: 95%; }
        }
    </style>
</head>
<body>
    <div class="chat-container">
        <div class="header">
            <h1>🇰🇪 Sido AI</h1>
            <p>Kenya's Smartest Business Assistant</p>
        </div>
        <div class="messages" id="messages">
            <div class="message sido"><strong>Sido AI:</strong> Habari! 👋 I'm Sido AI, your digital business assistant. How can I help you today?<br><small style="color:#888;">Try: "Create a business plan" or "Help me find a job"</small></div>
        </div>
        <div class="suggestions">
            <button onclick="quickQuestion('Create a business plan for a salon')">✏️ Business Plan</button>
            <button onclick="quickQuestion('Write my CV')">📄 CV Writer</button>
            <button onclick="quickQuestion('Find tenders in Kenya')">🔍 Tenders</button>
            <button onclick="quickQuestion('Generate an invoice')">🧾 Invoice</button>
            <button onclick="quickQuestion('Marketing content for Facebook')">📱 Marketing</button>
        </div>
        <div class="input-area">
            <input id="userInput" placeholder="Ask me anything about business..." />
            <button onclick="sendMessage()">Send 📤</button>
        </div>
    </div>

    <script>
        const messagesDiv = document.getElementById('messages');
        const userInput = document.getElementById('userInput');

        function quickQuestion(text) {
            userInput.value = text;
            sendMessage();
        }

        async function sendMessage() {
            const message = userInput.value.trim();
            if (!message) return;

            messagesDiv.innerHTML += `<div class="message user">${message}</div>`;
            userInput.value = '';
            messagesDiv.scrollTop = messagesDiv.scrollHeight;

            const typingDiv = document.createElement('div');
            typingDiv.className = 'message sido';
            typingDiv.innerHTML = '<em>Sido AI is thinking... 🤔</em>';
            typingDiv.id = 'typing';
            messagesDiv.appendChild(typingDiv);
            messagesDiv.scrollTop = messagesDiv.scrollHeight;

            try {
                const response = await fetch('/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: message })
                });
                
                if (!response.ok) throw new Error('Server error');
                const data = await response.json();
                
                document.getElementById('typing').remove();
                messagesDiv.innerHTML += `<div class="message sido"><strong>Sido AI:</strong> ${data.response.replace(/\\n/g, '<br>')}</div>`;
            } catch (error) {
                document.getElementById('typing').remove();
                messagesDiv.innerHTML += `<div class="message sido"><strong>Sido AI:</strong> ⚠️ Sorry, I'm having trouble connecting. Please try again.</div>`;
            }
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        }

        userInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') sendMessage();
        });
    </script>
</body>
</html>
    """
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)