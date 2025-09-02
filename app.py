import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("⚠️ API key not found! Please add it to your .env file.")
else:
    client = OpenAI(api_key=api_key)

    st.title("AI Code Explainer (Reverse Compiler)")

    # File uploader
    uploaded_file = st.file_uploader("Upload a C file", type=["c", "txt"])

    if uploaded_file is not None:
        code = uploaded_file.read().decode("utf-8")

        st.subheader("Uploaded Code")
        st.code(code, language="c")

        if st.button("Explain Code"):
            with st.spinner("Analyzing..."):
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are an AI code explainer."},
                        {"role": "user", "content": f"Explain the following C code in simple words:\n{code}"}
                    ]
                )
                explanation = response.choices[0].message.content
                st.subheader("Explanation")
                st.write(explanation)
