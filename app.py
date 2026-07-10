# app.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from agent import get_response
from datetime import datetime
from typing import Optional
import uvicorn
import os

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
        # Check if templates/index.html exists
        if os.path.exists("templates/index.html"):
            with open("templates/index.html", "r", encoding="utf-8") as f:
                html_content = f.read()
            return HTMLResponse(content=html_content)
        else:
            return HTMLResponse(content="""
            <h1>🇰🇪 Sido AI</h1>
            <p>Template file not found. Please create templates/index.html</p>
            """, status_code=404)
    except Exception as e:
        return HTMLResponse(content=f"<h1>Error loading template: {str(e)}</h1>", status_code=500)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)