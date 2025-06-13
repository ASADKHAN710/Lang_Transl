import streamlit as st
import google.generativeai as genai

# import google.generativai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
genai_api_key = os.getenv("GEMINI_API_KEY")

# API Key check
if not genai_api_key:
    st.error("❌ Error: GEMINI_API_KEY not found in environment variables.")
    st.stop()

# Configure Gemini
genai.configure(api_key=genai_api_key)

# Language options
languages = ["English", "Urdu", "Arabic", "French", "Chinese", "Spanish", "German", "Pashto"]

# Streamlit UI
st.set_page_config(page_title="Language Translator by Asad Khan", layout="centered")
st.title("🌐 Language Translator")
st.subheader("🤑 Made By Asad_Ullah 🤑") 
st.write("📌 Translate text from any language to any other using Google Gemini AI")

# User input
source_lang = st.selectbox("🗣️ Select Source Language", languages)
target_lang = st.selectbox("🌍 Select Target Language", languages)
text = st.text_area(f"🔤 Enter Text in {source_lang}:", height=150)
btn = st.button("🔄 Translate")

# Translation logic
if btn and text:
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"Translate the following text from {source_lang} to {target_lang}:\n\n{text}"
        response = model.generate_content(prompt)
        st.success(f"✅ Translated to {target_lang}:")
        st.markdown(f"**{response.text.strip()}**")
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
