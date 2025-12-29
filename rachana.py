import streamlit as st
import google.generativeai as genai

# පිටුවේ සැකසුම්
st.set_page_config(page_title="AI රචනා ලේඛකයා", page_icon="📝")

# ඔබේ API Key එක
API_KEY = "AIzaSyB5WdS4puKG7P1TL58Drk7zZcEsCAmAkog"

try:
    genai.configure(api_key=API_KEY)
    
    # 404 Error එක මගහැරීමට වඩාත් ස්ථාවර මාදිලියක් තෝරා ගනිමු
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    
    st.title("📝 AI රචනා සහ ලිපි ලේඛකයා")
    st.write("ඕනෑම මාතෘකාවක් ලබා දී සිංහල හෝ ඉංග්‍රීසි භාෂාවෙන් රචනාවක් ලබාගන්න.")

    topic = st.text_input("රචනාවේ මාතෘකාව මෙතන ලියන්න:", placeholder="උදා: මගේ මව")
    
    col1, col2 = st.columns(2)
    with col1:
        language = st.selectbox("භාෂාව තෝරන්න:", ["Sinhala", "English"])
    with col2:
        length = st.select_slider("රචනාවේ දිග:", options=["කෙටි", "මධ්‍යම", "දිගු"])

    if st.button("රචනාව ලියන්න ✨"):
        if topic:
            with st.spinner("AI රචනාව ලියමින් පවතී..."):
                try:
                    # AI එකට උපදෙස් ලබාදීම
                    prompt = f"Write a {length} creative essay about '{topic}' in {language}. Use clear paragraphs and a good title."
                    response = model.generate_content(prompt)
                    
                    st.divider()
                    st.subheader(f"📖 රචනාව: {topic}")
                    st.markdown(response.text)
                except Exception as api_error:
                    # මාදිලිය සොයාගත නොහැකි නම් gemini-pro උත්සාහ කරන්න
                    st.warning("Flash model එකේ ගැටලුවක් පවතී. Pro model එකෙන් උත්සාහ කරමු...")
                    model_alt = genai.GenerativeModel('gemini-pro')
                    response = model_alt.generate_content(f"Write a short essay about {topic} in {language}")
                    st.markdown(response.text)
        else:
            st.warning("කරුණාකර මාතෘකාවක් ඇතුළත් කරන්න.")

except Exception as e:
    st.error(f"දෝෂයක් සිදු විය: {e}")

st.markdown("---")
st.caption("Powered by Google Gemini AI")
