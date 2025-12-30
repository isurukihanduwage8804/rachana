import streamlit as st
import numpy as np
import plotly.graph_objects as go
import google.generativeai as genai

# 1. පිටුවේ මූලික සැකසුම්
st.set_page_config(page_title="අධ්‍යාපන සහායක | වර්ගජ ප්‍රස්ථාර", page_icon="📈", layout="wide")

# 2. Gemini AI සැකසුම (මෙහි gemini-1.5-flash භාවිතා කර ඇත - 404 Error එක නිවැරදි කර ඇත)
# ඔබේ API Key එක Streamlit Secrets වල ඇති බව උපකල්පනය කෙරේ
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.warning("Google API Key එක හමු නොවීය. AI විශේෂාංග අක්‍රීයයි.")

# 3. ලස්සන CSS පෙනුම (TypeError එක නිවැරදි කර ඇත)
st.markdown("""
    <style>
    .main-title {
        color: #6c5ce7;
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        padding-bottom: 20px;
    }
    .stNumberInput {
        border: 2px solid #6c5ce7;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="main-title">📈 වර්ගජ ප්‍රස්ථාර ගවේෂකය</p>', unsafe_allow_html=True)

# 4. Sidebar හරහා අගයන් ලබා ගැනීම (Text Box ක්‍රමයට)
st.sidebar.header("⚙️ පරාමිතීන් ඇතුළත් කරන්න")
st.sidebar.write("සමීකරණය: $y = ax^2 + bx + c$")

a = st.sidebar.number_input("a හි අගය (x² සංගුණකය):", value=1.0, step=0.1)
b = st.sidebar.number_input("b හි අගය (x සංගුණකය):", value=0.0, step=0.1)
c = st.sidebar.number_input("c හි අගය (නියතය):", value=0.0, step=0.1)

# 5. ප්‍රස්ථාර දත්ත ගණනය කිරීම
x = np.linspace(-10, 10, 400)
y = a * x**2 + b * x + c

# 6. Plotly ප්‍රස්ථාරය නිර්මාණය
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', 
                         line=dict(color='#6c5ce7', width=4),
                         name=f'y = {a}x² + {b}x + {c}',
                         fill='tozeroy', fillcolor='rgba(108, 92, 231, 0.1)'))

fig.update_layout(
    title=f"සජීවී ප්‍රස්ථාරය: $y = {a}x^2 + {b}x + {c}$",
    xaxis_title="x අක්ෂය",
    yaxis_title="y අක්ෂය",
    template="plotly_white",
    xaxis=dict(zeroline=True, zerolinewidth=2, zerolinecolor='black', gridcolor='lightgray'),
    yaxis=dict(zeroline=True, zerolinewidth=2, zerolinecolor='black', gridcolor='lightgray', range=[-20, 20]),
    height=600
)

# 7. තීරු 2කට බෙදා පෙන්වීම
col1, col2 = st.columns([2, 1])

with col1:
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("🔍 විශ්ලේෂණය")
    if a > 0:
        st.success("✅ මෙය **අවම අගයක්** සහිත උඩුකුරු (Upward) ප්‍රස්ථාරයකි.")
    elif a < 0:
        st.error("✅ මෙය **උපරිම අගයක්** සහිත යටිකුරු (Downward) ප්‍රස්ථාරයකි.")
    else:
        st.warning("⚠️ a = 0 නිසා මෙය සරල රේඛාවකි.")

    if a != 0:
        vx = -b / (2 * a)
        vy = a * vx**2 + b * vx + c
        st.info(f"📍 **ශීර්ෂය (Vertex):**\n\n ({vx:.2f}, {vy:.2f})")

st.markdown("<br><hr><center><small>නිර්මාණය: ඔබේ අධ්‍යාපන පියස | QR පද්ධතිය හරහා ක්‍රියාත්මකයි</small></center>", unsafe_allow_html=True)
