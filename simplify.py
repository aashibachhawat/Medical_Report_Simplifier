import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def simplify_report(report_text):
    prompt = f"""
    You are a medical assistant. Simplify the following medical report 
    into plain, patient-friendly language without losing important details.
    
    Report:
    {report_text}
    """
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    with open("reports/sample.txt", "r") as f:
        report = f.read()
    
    simplified = simplify_report(report)

    with open("outputs/simplified.txt", "w") as f:
        f.write(simplified)

    print("Simplified report saved in outputs/simplified.txt")
