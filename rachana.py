import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI රචනා ලේඛකයා", page_icon="📝")

# ඔයාගේ API Key එක
API_KEY = "AIzaSyB5WdS4puKG7P1TL58Drk7zZcEsCAmAkog"

try:
    genai.configure(api_key=API_KEY)
    # මෙතන අපි gemini-pro පාවිච්චි කරමු, එවිට error එක එන්නේ නැහැ
    model = genai.GenerativeModel('gemini-pro')
    
    st.title("📝 AI රචනා සහ ලිපි ලේඛකයා")
    topic = st.text_input("රචනාවේ මාතෘකාව මෙතන ලියන්න:", placeholder="උදා: මගේ මව")
    
    language = st.selectbox("භාෂාව තෝරන්න:", ["Sinhala", "English"])

    if st.button("රචනාව ලියන්න ✨"):
        if topic:
            with st.spinner("AI රචනාව ලියමින් පවතී..."):
                prompt = f"Write a creative essay about '{topic}' in {language}. Use clear paragraphs."
                response = model.generate_content(prompt)
                st.divider()
                st.markdown(response.text)
        else:
            st.warning("කරුණාකර මාතෘකාවක් ඇතුළත් කරන්න.")

except Exception as e:
    st.error(f"දෝෂයක් සිදු විය: {e}")
