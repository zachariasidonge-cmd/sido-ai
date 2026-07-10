# whatsapp.py - WhatsApp Bot Integration for Sido AI
import os
from dotenv import load_dotenv
from agent import get_response

load_dotenv()

# Twilio credentials (get from https://www.twilio.com)
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")

def send_whatsapp_message(to_number: str, message: str):
    """Send a WhatsApp message using Twilio"""
    try:
        from twilio.rest import Client
        
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        
        message = client.messages.create(
            body=message,
            from_=f'whatsapp:{TWILIO_WHATSAPP_NUMBER}',
            to=f'whatsapp:{to_number}'
        )
        return f"✅ Message sent! SID: {message.sid}"
    except ImportError:
        return "⚠️ Twilio not installed. Run: pip install twilio"
    except Exception as e:
        return f"❌ Error sending message: {str(e)}"

def handle_whatsapp_message(message: str, from_number: str):
    """Process a WhatsApp message and return Sido AI's response"""
    try:
        response = get_response(message)
        send_whatsapp_message(from_number, response)
        return response
    except Exception as e:
        error_msg = f"⚠️ Sorry, I encountered an error: {str(e)}"
        send_whatsapp_message(from_number, error_msg)
        return error_msg

# For testing
if __name__ == "__main__":
    print("📱 WhatsApp Bot for Sido AI")
    print("Configure your Twilio credentials first!")
    print("Add these to your .env file:")
    print("TWILIO_ACCOUNT_SID=your_account_sid")
    print("TWILIO_AUTH_TOKEN=your_auth_token")
    print("TWILIO_WHATSAPP_NUMBER=+14155238886")