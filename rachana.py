import streamlit as st
import google.generativeai as genai

# --- පිටුවේ සැකසුම් (Page Settings) ---
st.set_page_config(page_title="AI රචනා ලේඛකයා", page_icon="📝", layout="centered")

# --- ඔයා එවපු API Key එක මෙතන තියෙනවා ---
API_KEY = "AIzaSyB5WdS4puKG7P1TL58Drk7zZcEsCAmAkog"

# AI එක සැකසීම
try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    st.title("📝 AI රචනා සහ ලිපි ලේඛකයා")
    st.write("ඕනෑම මාතෘකාවක් ලබා දී සිංහල හෝ ඉංග්‍රීසි භාෂාවෙන් රචනාවක් ලබාගන්න.")

    # --- පරිශීලකයා දත්ත ඇතුළත් කරන තැන ---
    topic = st.text_input("රචනාවේ මාතෘකාව මෙතන ලියන්න:", placeholder="උදා: පරිසර දූෂණය සහ එහි බලපෑම")
    
    col1, col2 = st.columns(2)
    with col1:
        language = st.selectbox("භාෂාව තෝරන්න:", ["Sinhala", "English"])
    with col2:
        length = st.select_slider("රචනාවේ දිග:", options=["කෙටි", "මධ්‍යම", "දිගු"])

    if st.button("රචනාව ලියන්න ✨"):
        if topic:
            with st.spinner("AI රචනාව ලියමින් පවතී... කරුණාකර තත්පර කිහිපයක් රැඳී සිටින්න."):
                # AI එකට දෙන නියෝගය
                prompt = f"Write a {length} creative essay about '{topic}' in {language}. Use a proper title and clear paragraphs."
                
                response = model.generate_content(prompt)
                
                st.divider()
                st.subheader(f"📖 රචනාව: {topic}")
                st.markdown(response.text)
                
                # Download Button එක
                st.download_button(
                    label="රචනාව භාගත කරන්න (Download TXT)",
                    data=response.text,
                    file_name=f"{topic}.txt",
                    mime="text/plain"
                )
        else:
            st.warning("කරුණාකර මාතෘකාවක් ඇතුළත් කරන්න.")

except Exception as e:
    st.error(f"දෝෂයක් සිදු විය: {e}")

st.markdown("---")
st.caption("මෙම App එක Google Gemini AI තාක්ෂණයෙන් ක්‍රියාත්මක වේ.")
