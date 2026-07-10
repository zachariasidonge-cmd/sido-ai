# mpesa.py - M-Pesa Integration for Sido AI
import os
import base64
import requests
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class MpesaAPI:
    def __init__(self):
        self.consumer_key = os.getenv("MPESA_CONSUMER_KEY")
        self.consumer_secret = os.getenv("MPESA_CONSUMER_SECRET")
        self.shortcode = os.getenv("MPESA_SHORTCODE", "9305680")  # Your till number
        self.passkey = os.getenv("MPESA_PASSKEY")
        self.base_url = "https://sandbox.safaricom.co.ke"  # Change to live for production
        
        # Determine if we're in production or sandbox
        if os.getenv("MPESA_ENVIRONMENT") == "production":
            self.base_url = "https://api.safaricom.co.ke"
    
    def get_access_token(self):
        """Get M-Pesa access token"""
        try:
            url = f"{self.base_url}/oauth/v1/generate?grant_type=client_credentials"
            
            # Encode credentials
            credentials = f"{self.consumer_key}:{self.consumer_secret}"
            encoded_credentials = base64.b64encode(credentials.encode()).decode()
            
            headers = {
                "Authorization": f"Basic {encoded_credentials}"
            }
            
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            result = response.json()
            return result.get("access_token")
        except Exception as e:
            return f"Error getting token: {str(e)}"
    
    def lipa_na_mpesa(self, phone_number: str, amount: float, account_reference: str = "SidoAI"):
        """Initiate a Lipa Na M-Pesa Online Payment"""
        try:
            access_token = self.get_access_token()
            if not access_token or "Error" in str(access_token):
                return {"error": "Failed to get access token"}
            
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            password = base64.b64encode(
                f"{self.shortcode}{self.passkey}{timestamp}".encode()
            ).decode("utf-8")
            
            url = f"{self.base_url}/mpesa/stkpush/v1/processrequest"
            headers = {
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json"
            }
            
            # Ensure phone number is in correct format (2547XXXXXXXX)
            if phone_number.startswith("0"):
                phone_number = "254" + phone_number[1:]
            elif not phone_number.startswith("254"):
                phone_number = "254" + phone_number
            
            payload = {
                "BusinessShortCode": self.shortcode,
                "Password": password,
                "Timestamp": timestamp,
                "TransactionType": "CustomerPayBillOnline",
                "Amount": amount,
                "PartyA": phone_number,
                "PartyB": self.shortcode,
                "PhoneNumber": phone_number,
                "CallBackURL": "https://sido-ai.onrender.com/mpesa/callback",
                "AccountReference": account_reference[:12],
                "TransactionDesc": f"Payment for {account_reference[:20]}"
            }
            
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            
            result = response.json()
            
            if result.get("ResponseCode") == "0":
                return {
                    "success": True,
                    "message": "Payment initiated successfully! Check your phone for M-Pesa prompt.",
                    "checkout_request_id": result.get("CheckoutRequestID"),
                    "amount": amount,
                    "phone": phone_number,
                    "reference": account_reference
                }
            else:
                return {
                    "success": False,
                    "error": result.get("ResponseDescription", "Payment failed")
                }
                
        except requests.exceptions.RequestException as e:
            return {"success": False, "error": f"Network error: {str(e)}"}
        except Exception as e:
            return {"success": False, "error": f"Payment error: {str(e)}"}
    
    def check_payment_status(self, checkout_request_id: str):
        """Check the status of an M-Pesa payment"""
        try:
            access_token = self.get_access_token()
            if not access_token or "Error" in str(access_token):
                return {"error": "Failed to get access token"}
            
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            password = base64.b64encode(
                f"{self.shortcode}{self.passkey}{timestamp}".encode()
            ).decode("utf-8")
            
            url = f"{self.base_url}/mpesa/stkpushquery/v1/query"
            headers = {
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "BusinessShortCode": self.shortcode,
                "Password": password,
                "Timestamp": timestamp,
                "CheckoutRequestID": checkout_request_id
            }
            
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            
            return response.json()
        except Exception as e:
            return {"error": f"Status check error: {str(e)}"}

# Initialize M-Pesa API
mpesa = MpesaAPI()

def process_payment(phone: str, amount: float, reference: str = "SidoAI"):
    """Process a payment using M-Pesa - Main function to call from Sido AI"""
    try:
        # Validate phone number
        if len(phone) < 10:
            return "❌ Please enter a valid phone number (e.g., 0712345678 or 254712345678)"
        
        # Validate amount
        if amount < 1:
            return "❌ Amount must be at least KSh 1"
        
        result = mpesa.lipa_na_mpesa(phone, amount, reference)
        
        if result.get("success"):
            return f"""
✅ **M-Pesa Payment Initiated Successfully!**

**Amount:** KSh {amount:,.2f}
**Reference:** {reference}
**Phone:** {result.get('phone')}
**Checkout ID:** {result.get('checkout_request_id')}

📱 **Please check your phone NOW:**
1. Enter your M-Pesa PIN
2. Confirm the payment
3. You will receive a confirmation SMS

💰 **Payment Status:** Pending Confirmation

*Note: The payment request expires in 2 minutes.*
"""
        else:
            error_msg = result.get("error", "Unknown error")
            return f"""
❌ **Payment Failed**

**Error:** {error_msg}

**Possible reasons:**
- Insufficient M-Pesa balance
- Wrong phone number
- M-Pesa service unavailable
- Network issues

💡 **Try again** or contact M-Pesa customer care.
"""
    except Exception as e:
        return f"⚠️ Payment error: {str(e)}"

def payment_history():
    """Return a summary of recent payments (simulated for now)"""
    return """
📊 **M-Pesa Payment History**

(Simulated - Connect to your database for real history)

**Recent Transactions:**
1. KSh 1,000 - SidoAI - 10/07/2026 - ✅ Completed
2. KSh 500 - SidoAI - 09/07/2026 - ✅ Completed
3. KSh 2,000 - SidoAI - 08/07/2026 - ⏳ Pending
4. KSh 1,500 - SidoAI - 07/07/2026 - ✅ Completed

**Total Collected:** KSh 5,000
**Pending:** KSh 2,000
"""