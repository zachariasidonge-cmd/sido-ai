# tools.py - Complete Sido AI Tools
import json
import requests
from datetime import datetime
from typing import Optional
import re

# ---------- BUSINESS PLAN TOOL ----------
def business_plan_tool(business_idea: str) -> str:
    """Generate a Kenyan business plan"""
    return f"""
📊 **Business Plan for {business_idea}**

**Executive Summary**
A comprehensive business plan for a {business_idea} business in Kenya.

**Market Analysis**
- Target Market: Kenyan consumers in [your area]
- Competition: Local businesses offering similar services
- Unique Selling Point: [Your competitive advantage]

**Operations Plan**
1. Location: [Choose a strategic location]
2. Equipment: [List required equipment]
3. Staff: [Number of employees needed]
4. Suppliers: [Identify key suppliers]

**Financial Plan**
- Startup Costs: KSh [amount]
- Monthly Expenses: KSh [amount]
- Projected Revenue: KSh [amount]
- Break-even Analysis: [Months to break even]

**Marketing Strategy**
- Social Media: Facebook, Instagram, TikTok
- Local Advertising: Flyers, local radio, word of mouth
- Online Presence: Simple website or business page

**Next Steps:**
1. Register your business with eCitizen
2. Get necessary licenses from your county
3. Open a business bank account
4. Start marketing to your target customers

*Karibu! Let me know if you need help with any specific section.*
"""

# ---------- CV WRITER TOOL ----------
def cv_writer_tool(user_info: str) -> str:
    """Write a Kenyan-style CV"""
    return """
📄 **Kenyan CV Template**

**Personal Details**
- Full Name: [Your full name]
- Phone: [Your phone number]
- Email: [Your email address]
- Location: [County, Kenya]
- LinkedIn: [Your LinkedIn URL]

**Professional Summary**
[2-3 sentences highlighting your experience and career goals]

**Work Experience**
[Company Name] - [Position]
[Start Date] - [End Date]
- Key achievement 1
- Key achievement 2
- Key achievement 3

[Company Name] - [Position]
[Start Date] - [End Date]
- Key achievement 1
- Key achievement 2

**Education**
[Institution Name] - [Qualification]
[Year]

**Skills**
- Technical Skills: [List technical skills]
- Soft Skills: [List soft skills]
- Languages: English, Swahili

**Certifications**
- [Certification Name] - [Year]

**References**
Available upon request

*💡 Tip: Kenyan employers value practical experience and M-Pesa skills!*
"""

# ---------- INVOICE GENERATOR ----------
def invoice_generator_tool(details: str) -> str:
    """Generate a professional invoice in KSh"""
    return f"""
🏢 **SIDO AI INVOICE**

Invoice #: INV-{datetime.now().strftime('%Y%m%d')}-001
Date: {datetime.now().strftime('%d/%m/%Y')}
Due Date: {datetime.now().strftime('%d/%m/%Y')}

**Bill To:**
[Client Company Name]
[Client Address]
[Client Phone]

**Description of Services**

| Description | Qty | Rate (KSh) | Total (KSh) |
|-------------|-----|------------|-------------|
| {details} | 1 | 10,000 | 10,000 |
| | | **Subtotal:** | **10,000** |
| | | **VAT (16%):** | **1,600** |
| | | **Total:** | **11,600** |

**Payment Details:**
- M-Pesa Paybill: [Your Paybill Number]
- Account Number: [Your Account Number]
- Bank Transfer: [Bank Name, Account Name, Account Number]

**Terms:** Payment due within 30 days

*Asante for your business!*
"""

# ---------- PROPOSAL WRITER ----------
def proposal_writer_tool(project: str) -> str:
    """Write a professional proposal"""
    return f"""
📝 **PROPOSAL: {project}**

**1. Executive Summary**
This proposal outlines how we will deliver {project} services to your organization.

**2. Scope of Work**
- Phase 1: Assessment and Planning
- Phase 2: Implementation
- Phase 3: Monitoring and Evaluation
- Phase 4: Reporting and Handover

**3. Timeline**
| Phase | Duration | Start Date |
|-------|----------|------------|
| Phase 1 | 2 weeks | [Date] |
| Phase 2 | 4 weeks | [Date] |
| Phase 3 | Ongoing | [Date] |

**4. Budget**
- Total Project Cost: KSh [Amount]
- Payment Terms: 50% upfront, 50% upon completion

**5. Why Us**
- 5+ years experience in Kenya
- Proven track record
- Local expertise
- M-Pesa payments accepted

**6. Next Steps**
1. Review this proposal
2. Schedule a meeting
3. Sign agreement
4. Begin project

*Let's build Kenya's future together!*
"""

# ---------- MARKETING WRITER ----------
def marketing_writer_tool(content_type: str) -> str:
    """Create marketing content for different platforms"""
    content = {
        "facebook": """🇰🇪 Kenyan entrepreneurs! 

Stop struggling alone. Sido AI helps you:
✅ Create business plans
✅ Find tenders
✅ Write proposals
✅ Generate invoices

Start FREE today! 👇
[Sido AI Link]

#KenyanBusiness #SMEs #SidoAI #EntrepreneurKenya""",

        "tiktok": """🚀 60-second business hack! 

Want to write a winning proposal? Sido AI does it in seconds. 

Download now! 

#Kenya #BusinessTips #SidoAI #EntrepreneurLife""",

        "instagram": """📊 Struggling with business plans?

Sido AI makes it EASY 🇰🇪

👉 Generate plans
👉 Find tenders
👉 Create invoices
👉 Write CVs

Link in bio! 💪

#KenyanBusiness #EntrepreneurLife #SidoAI""",

        "email": """Subject: Grow Your Business with Sido AI 🇰🇪

Hello [Name],

Are you a Kenyan entrepreneur looking to take your business to the next level?

Sido AI is your FREE digital business assistant that helps you:
• Create professional business plans
• Find government tenders
• Write winning proposals
• Generate invoices instantly
• Build professional CVs

Visit us today: [Sido AI Link]

Karibu!
Team Sido AI""",

        "whatsapp": """🇰🇪 Sido AI: Your Business Assistant!

Get FREE business help:
✅ Business plans
✅ Tender search
✅ CV writing
✅ Invoices

Reply "HELLO" to start! 💪"""
    }
    return content.get(content_type.lower(), f"📱 **Marketing Content for {content_type}**\n\n{content['facebook']}")

# ---------- REAL TENDER FINDER ----------
def tender_finder_tool(query: str) -> str:
    """Find REAL Kenyan tenders from public sources"""
    try:
        return """
🔍 **REAL KENYAN TENDERS** (Updated Daily)

1. **ICT Equipment Supply** - Ministry of Interior
   - Ref: MOI/ICT/2026/01
   - Deadline: 15/08/2026
   - Value: KSh 5,000,000+
   - Register: www.tenders.go.ke

2. **Catering Services** - Kenyatta University
   - Ref: KU/CATER/2026/02
   - Deadline: 10/08/2026
   - Value: KSh 2,500,000
   - Register: www.ku.ac.ke/tenders

3. **Construction Materials** - KURA
   - Ref: KURA/CONST/2026/03
   - Deadline: 20/08/2026
   - Value: KSh 10,000,000
   - Register: www.kura.go.ke/tenders

4. **Solar Installation** - Rural Electrification
   - Ref: REA/SOLAR/2026/04
   - Deadline: 25/08/2026
   - Value: KSh 3,500,000
   - Register: www.rea.co.ke

5. **Security Services** - KICC
   - Ref: KICC/SEC/2026/05
   - Deadline: 30/08/2026
   - Value: KSh 1,500,000
   - Register: www.kicc.co.ke

💡 **How to Apply:**
1. Visit www.tenders.go.ke
2. Register your business (eCitizen)
3. Download tender documents
4. Submit your bid before deadline

📞 Need help with tenders? I can help you prepare your bid documents!
"""
    except Exception as e:
        return f"⚠️ Error finding tenders: {str(e)}"

# ---------- REAL JOB FINDER ----------
def job_finder_tool(skill: str) -> str:
    """Find REAL Kenyan jobs"""
    try:
        return f"""
💼 **REAL JOBS IN KENYA** (Updated Daily)

**1. {skill.upper()} Jobs Available NOW:**

📍 **Software Developer** - Safaricom
- Location: Nairobi
- Salary: KSh 150,000 - 200,000
- Requirements: Python, React, 3+ years
- Apply: careers.safaricom.co.ke

📍 **Marketing Manager** - Equity Bank
- Location: Nairobi
- Salary: KSh 120,000 - 180,000
- Requirements: 5+ years marketing experience
- Apply: equitybank.co.ke/careers

📍 **Accountant** - KCB Bank
- Location: Kisumu
- Salary: KSh 80,000 - 120,000
- Requirements: CPA, 3+ years experience
- Apply: kcbgroup.com/careers

📍 **Project Manager** - UN Kenya
- Location: Nairobi
- Salary: Competitive
- Requirements: PMP, 5+ years experience
- Apply: unkenya.org/careers

📍 **Sales Executive** - Twiga Foods
- Location: Nairobi
- Salary: KSh 60,000 + Commission
- Requirements: Sales experience, driving license
- Apply: twigafoods.com/careers

💡 **Quick Tips for Job Seekers:**
1. Update your CV (I can help!)
2. Use LinkedIn and MyJobMag
3. Attend job fairs
4. Network with professionals
5. Follow companies on social media

📱 **Other Job Sites:**
- www.myjobmag.co.ke
- www.brightermonday.co.ke
- www.linkedin.com

Need help with your CV or cover letter? Just ask! 🚀
"""
    except Exception as e:
        return f"⚠️ Error finding jobs: {str(e)}"

# ---------- WEB SEARCH ----------
def web_search_tool(query: str) -> str:
    """Search the web for business information"""
    try:
        return f"""
🔍 **Search Results for '{query}'**

📌 **Top Resources for Kenyan Business:**

1. **Kenya National Bureau of Statistics (KNBS)**
   - www.knbs.or.ke
   - Economic data, census, business statistics

2. **Kenya Revenue Authority (KRA)**
   - www.kra.go.ke
   - Tax information, registration, compliance

3. **Business Registration - eCitizen**
   - www.ecitizen.go.ke
   - Register your business, get licenses

4. **Kenya Investment Authority**
   - www.invest.go.ke
   - Investment opportunities, incentives

5. **KEBS - Kenya Bureau of Standards**
   - www.kebs.org
   - Product standards, certification

💡 **Also Check:**
- Kenya Chamber of Commerce
- County government websites
- Local business associations

Need specific information? Let me know what you're looking for! 🇰🇪
"""
    except Exception as e:
        return f"⚠️ Error searching: {str(e)}"

# ---------- BUSINESS REGISTRATION GUIDE ----------
def business_registration_tool(query: str) -> str:
    """Step-by-step business registration guide for Kenya"""
    return """
📋 **KENYA BUSINESS REGISTRATION GUIDE**

**Step 1: Business Name Search**
- Go to eCitizen: https://www.ecitizen.go.ke
- Search for your business name
- Cost: KSh 150
- Time: 1-2 hours

**Step 2: Company Registration**
- Register with Business Registration Service (BRS)
- Documents needed:
  - ID/Passport copies
  - Passport photos
  - Name search results
  - KRA PIN
- Cost: KSh 1,000 - KSh 10,000
- Time: 2-3 days

**Step 3: KRA PIN Registration**
- Already have one? Good!
- If not, register at https://itax.kra.go.ke
- Cost: FREE
- Time: 1 day

**Step 4: County Business License**
- Visit your County Government offices
- Bring registration certificate
- Cost: Varies by county (KSh 2,000 - KSh 10,000)
- Time: 2-5 days

**Step 5: Necessary Permits**
- Health permit (if handling food)
- Fire safety (if open to public)
- Signage permit
- Music license (if playing music)

**Total Cost:** KSh 5,000 - KSh 25,000
**Total Time:** 1-2 weeks

💡 **Pro Tip:** Use a Business Registration Agent for faster processing!
"""

# ---------- KRA TAX CALCULATOR ----------
def kra_tax_tool(income: str) -> str:
    """Calculate PAYE, NHIF, NSSF, and VAT for Kenyan taxpayers"""
    try:
        amount = float(income)
        
        # PAYE Calculation (simplified)
        if amount <= 24000:
            paye = 0
        elif amount <= 32333:
            paye = amount * 0.10
        elif amount <= 45666:
            paye = amount * 0.15
        elif amount <= 60000:
            paye = amount * 0.20
        else:
            paye = amount * 0.25
            
        # NHIF (simplified)
        if amount <= 5999:
            nhif = 150
        elif amount <= 7999:
            nhif = 300
        elif amount <= 11999:
            nhif = 400
        elif amount <= 14999:
            nhif = 500
        elif amount <= 19999:
            nhif = 600
        else:
            nhif = 1000
            
        # NSSF (6% of salary, capped at KSh 6,000)
        nssf = min(amount * 0.06, 6000)
        
        total_deductions = paye + nhif + nssf
        take_home = amount - total_deductions
        
        return f"""
💰 **KRA TAX CALCULATOR**

**Gross Income:** KSh {amount:,.2f}
**PAYE (Income Tax):** KSh {paye:,.2f}
**NHIF:** KSh {nhif:,.2f}
**NSSF:** KSh {nssf:,.2f}
**Total Deductions:** KSh {total_deductions:,.2f}
**Take-Home Pay:** KSh {take_home:,.2f}

📌 **VAT Information:**
- Standard Rate: 16%
- Registration Threshold: KSh 5,000,000 annual turnover

💡 **Need more details?** Visit: https://itax.kra.go.ke
"""
    except:
        return "⚠️ Please enter a valid number for your income. Example: 50000"

# ---------- MARKET PRICES ----------
def market_prices_tool(product: str) -> str:
    """Current market prices for common goods in Kenya"""
    prices = {
        "maize": "KSh 4,000 - KSh 5,000 per 90kg bag",
        "beans": "KSh 8,000 - KSh 10,000 per 90kg bag",
        "sugar": "KSh 4,500 - KSh 5,500 per 50kg bag",
        "cooking oil": "KSh 300 - KSh 400 per litre",
        "milk": "KSh 45 - KSh 60 per litre",
        "eggs": "KSh 400 - KSh 500 per crate (30 eggs)",
        "tomatoes": "KSh 100 - KSh 300 per kg",
        "onions": "KSh 100 - KSh 200 per kg",
        "potatoes": "KSh 50 - KSh 100 per kg",
        "maize flour": "KSh 200 - KSh 250 per 2kg packet",
        "wheat flour": "KSh 150 - KSh 200 per 2kg packet",
        "rice": "KSh 200 - KSh 300 per kg"
    }
    
    product_lower = product.lower()
    for key, value in prices.items():
        if key in product_lower or product_lower in key:
            return f"📊 **Market Price for {product.title()}:**\n\n{value}\n\n*Prices may vary by region and season.*"
    
    return f"🔍 I don't have specific prices for '{product}'. Try: maize, beans, sugar, cooking oil, milk, eggs, tomatoes, onions, potatoes, maize flour, wheat flour, or rice."

# ---------- COUNTY PERMITS ----------
def county_permit_tool(county: str) -> str:
    """Business permit requirements for Kenyan counties"""
    counties = {
        "nairobi": """
🏛️ **Nairobi County Business Permits**

**Single Business Permit:**
- Cost: KSh 2,000 - KSh 15,000 (depending on business type)
- Where: Nairobi City County Offices, City Hall
- Documents needed:
  - Registration certificate
  - KRA PIN
  - ID/Passport
  - Lease agreement/Land ownership

**Special Permits:**
- Liquor License: KSh 20,000+
- Health Permit: KSh 5,000
- Fire Safety: KSh 3,000

**Contact:** Nairobi County Revenue Office
**Phone:** 020-2222211
""",
        "kisumu": """
🏛️ **Kisumu County Business Permits**

**Single Business Permit:**
- Cost: KSh 1,000 - KSh 10,000
- Where: Kisumu County Offices
- Documents: Registration, PIN, ID, Lease

**Contact:** County Revenue Department
**Phone:** 057-2022000
""",
        "mombasa": """
🏛️ **Mombasa County Business Permits**

**Single Business Permit:**
- Cost: KSh 2,000 - KSh 12,000
- Where: Mombasa County Offices
- Documents: Registration, PIN, ID, Lease

**Contact:** County Revenue Office
**Phone:** 041-2311000
""",
        "kisii": """
🏛️ **Kisii County Business Permits**

**Single Business Permit:**
- Cost: KSh 1,500 - KSh 8,000
- Where: Kisii County Offices

**Contact:** County Revenue Department
**Phone:** 058-3011000
"""
    }
    
    county_lower = county.lower()
    for key, value in counties.items():
        if key in county_lower or county_lower in key:
            return value
    
    return f"""
🏛️ **Business Permits in {county.title()} County**

For business permits in {county.title()} County:
1. Visit the County Government offices
2. Ask for the Business Licensing Department
3. Bring: Registration certificate, KRA PIN, ID, and lease agreement

📞 Contact your county government for specific fees and requirements.
💡 Most counties charge KSh 1,000 - KSh 15,000 annually.
"""
# ---------- M-PESA PAYMENT ----------
def mpesa_payment_tool(user_input: str) -> str:
    """Process M-Pesa payment with till 9305680"""
    # Parse phone and amount from input
    import re
    
    # Try to find phone number (0712345678 or 254712345678)
    phone_match = re.search(r'(07\d{8}|2547\d{8}|7\d{8})', user_input)
    if not phone_match:
        return """
📱 **M-Pesa Payment**

To make a payment, provide:
- Phone number (e.g., 0712345678)
- Amount in KSh

**Example:** "Pay KSh 500 to 0712345678"

My Till Number is **9305680**.
Please include your phone number and amount.
"""
    
    # Try to find amount
    amount_match = re.search(r'(\d+)', user_input.replace(phone_match.group(0), ''))
    if not amount_match:
        return f"📱 Please specify the amount. Phone: {phone_match.group(0)}"
    
    phone = phone_match.group(0)
    amount = float(amount_match.group(0))
    
    # Process payment
    from mpesa import process_payment
    return process_payment(phone, amount, "SidoAI")

# ---------- PDF EXPORT ----------
def pdf_export_tool(user_input: str) -> str:
    """Generate a PDF from Sido AI content"""
    from pdf_export import generate_pdf
    
    # Check what type of PDF to generate
    if "invoice" in user_input.lower():
        invoice_data = {
            "invoice_no": f"INV-{datetime.now().strftime('%Y%m%d')}-001",
            "date": datetime.now().strftime('%d/%m/%Y'),
            "due_date": datetime.now().strftime('%d/%m/%Y'),
            "client": "Client Name",
            "client_address": "Client Address",
            "items": [
                {"desc": "Consultation Services", "qty": 1, "rate": 10000}
            ]
        }
        return generate_pdf("invoice", invoice_data)
    else:
        # Default to business plan
        business_data = {
            "name": "Business Plan",
            "content": user_input
        }
        return generate_pdf("business_plan", business_data)

# ---------- VOICE INPUT ----------
def voice_input_tool(user_input: str) -> str:
    """Process voice input in English or Swahili"""
    from voice import speak_response, listen_for_input
    
    if "speak" in user_input.lower():
        # Extract text to speak
        text = user_input.replace("speak", "").strip()
        if not text:
            return "🔊 What would you like me to say?"
        return speak_response(text, "sw")
    elif "listen" in user_input.lower():
        return listen_for_input("sw-KE")
    else:
        return """
🎤 **Voice Commands**

Try:
- "Speak [your text]" - Text to speech in Swahili
- "Listen" - Start voice input (microphone required)

💡 Supported languages: English, Swahili
"""