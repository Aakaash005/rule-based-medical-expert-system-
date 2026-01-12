import streamlit as st
from rules import rules
from inference import forward_chaining

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="Medical Expert System",
    page_icon="🧠",
    layout="wide"
)

# ==============================
# CUSTOM CSS (IMPROVED READABILITY)
# ==============================
st.markdown("""
<style>
/* Lighter premium background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #020617, #020617);
    color: #f8fafc;
}

/* Glass cards */
.glass {
    background: rgba(255, 255, 255, 0.10);
    backdrop-filter: blur(14px);
    border-radius: 20px;
    padding: 25px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.4);
    border: 1px solid rgba(255,255,255,0.18);
}

/* Top empty bars fix */
.topbar {
    background: rgba(255,255,255,0.08);
    border-radius: 20px;
    height: 60px;
}

/* Big title */
.hero-title {
    font-size: 52px;
    font-weight: 800;
    text-align: center;
    background: linear-gradient(90deg, #38bdf8, #a78bfa, #f472b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Subtitle */
.hero-sub {
    text-align: center;
    font-size: 20px;
    color: #e5e7eb;
}

/* Feature cards */
.feature {
    background: rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 20px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.15);
}

/* Fix selectbox + input */
div[data-baseweb="select"] > div {
    background-color: #020617 !important;
    color: white !important;
    border-radius: 10px;
}

/* Fix "Choose all that apply" label */
label {
    color: #e5e7eb !important;
    font-size: 16px !important;
}

/* Fix diagnose button */
.stButton > button {
    background: linear-gradient(90deg, #38bdf8, #a78bfa);
    color: black;
    font-weight: bold;
    border-radius: 10px;
    padding: 10px 20px;
}

/* Diagnosis success box */
.success-box {
    background: linear-gradient(90deg, #022c22, #064e3b);
    color: #ecfdf5;
    padding: 18px;
    border-radius: 12px;
    font-size: 20px;
    font-weight: bold;
    border: 1px solid #10b981;
}

/* Footer */
.footer {
    text-align: center;
    color: #cbd5f5;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# HERO SECTION
# ==============================
st.markdown("""
<div class="glass">
    <div class="hero-title">🧠 Rule-Based Medical Expert System</div>
    <p class="hero-sub">
        An AI-powered expert system using <b>Forward Chaining</b> and <b>IF–THEN Rules</b><br>
        to provide transparent and explainable medical reasoning.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==============================
# DISCLAIMER
# ==============================
st.markdown("""
<div class="glass">
⚠️ <b>Disclaimer:</b> This system is for educational purposes only and should not be used
as a substitute for professional medical advice.
</div>
""", unsafe_allow_html=True)

# ==============================
# FEATURE CARDS
# ==============================
st.markdown("<br>", unsafe_allow_html=True)

colf1, colf2, colf3 = st.columns(3)

with colf1:
    st.markdown("""
    <div class="feature">
    🧠 <h3>Explainable AI</h3>
    Shows exactly how each decision is made using rule chaining.
    </div>
    """, unsafe_allow_html=True)

with colf2:
    st.markdown("""
    <div class="feature">
    ⚙️ <h3>Forward Chaining</h3>
    Multi-step logical inference from facts to conclusions.
    </div>
    """, unsafe_allow_html=True)

with colf3:
    st.markdown("""
    <div class="feature">
    🏥 <h3>Medical Knowledge Base</h3>
    Rule-driven diagnosis system built on expert knowledge.
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ==============================
# INPUT / OUTPUT SECTION
# ==============================
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.subheader("🧾 Select Symptoms")
    symptoms = st.multiselect(
        "Choose all that apply:",
        ["Fever", "Cough", "HIV-AIDS", "Stress", "Headache", "Nausea", "Severe fever", "Normal fever", "ADHD", "Anxiety", 
        ]
    )
    diagnose_btn = st.button("🔍 Diagnose")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.subheader("📊 Diagnosis Result")

    if diagnose_btn:
        if not symptoms:
            st.warning("Please select at least one symptom.")
        else:
            facts = set(symptoms)
            final_facts, log = forward_chaining(facts, rules)
            conclusions = final_facts - set(symptoms)

            if conclusions:
                for c in conclusions:
                    st.markdown(
                        f'<div class="success-box">🩺 {c.replace("_", " ").title()}</div>',
                        unsafe_allow_html=True
                    )
            else:
                st.info("No diagnosis could be inferred.")

    st.markdown('</div>', unsafe_allow_html=True)

# ==============================
# REASONING PATH
# ==============================
if 'diagnose_btn' in locals() and diagnose_btn and 'log' in locals() and log:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.subheader("🧠 Reasoning Path (Explainable AI)")
    for step in log:
        st.code(step)
    st.markdown('</div>', unsafe_allow_html=True)

# ==============================
# FOOTER
# ==============================
st.markdown("""
<br><br>
<div class="footer">
Built as part of Syntecxhub Internship Project — Rule-Based Expert System<br>
Developed using Python & Streamlit
</div>
""", unsafe_allow_html=True)