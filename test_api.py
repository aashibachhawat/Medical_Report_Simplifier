import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv("C:\\Users\\MailA\\OneDrive\\VIIT\\DIVYANI\\MEDICAL_REPORT_SIMPLIFIER\\med-report-genai-starter\\.env")

# Debug: Print the API key to verify
print("API Key:", os.getenv("GEMINI_API_KEY"))

# Configure with the Gemini API key from .env
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# pick a model
model = genai.GenerativeModel('gemini-1.5-flash')

# test call
response = model.generate_content("Give me a short 2 line motivational quote")
print("Response:", response.text)