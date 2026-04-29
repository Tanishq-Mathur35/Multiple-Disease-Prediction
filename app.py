import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import time

st.set_page_config(
    page_title="Smart Health Assistant",
    page_icon="🩺",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=IBM+Plex+Sans:wght@300;400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [class*="css"] {
    font-family: 'IBM Plex Sans', sans-serif;
    background: #f0f4f8;
}

.stApp {
    background: linear-gradient(160deg, #e8f0fe 0%, #f0f4f8 40%, #e6f4f1 100%);
    min-height: 100vh;
}

section[data-testid="stSidebar"] {
    background: #0d1b2a !important;
    border-right: none;
    padding-top: 1rem;
}
section[data-testid="stSidebar"] * { color: #c9d6e3 !important; }
section[data-testid="stSidebar"] h2 {
    font-family: 'Syne', sans-serif !important;
    font-size: 1.1rem !important;
    color: #ffffff !important;
    letter-spacing: 0.04em;
    padding: 1rem 1.2rem 0.4rem;
}

.block-container {
    padding: 2rem 2.5rem !important;
    max-width: 1100px !important;
}

.main-title {
    font-family: 'Syne', sans-serif !important;
    font-size: 2.6rem !important;
    font-weight: 800;
    color: #0d1b2a;
    letter-spacing: -0.03em;
    line-height: 1.1;
    margin-bottom: 0.3rem;
}

.sub-title {
    font-size: 1rem;
    font-weight: 400;
    color: #5a7fa8;
    margin-bottom: 2rem;
    letter-spacing: 0.02em;
}

.card {
    background: #ffffff;
    padding: 2rem 2.2rem;
    border-radius: 20px;
    border: 1px solid #e2eaf3;
    box-shadow: 0 4px 24px rgba(13,27,42,0.07);
    margin-bottom: 1.8rem;
}

label, .stTextInput label {
    font-size: 0.72rem !important;
    font-weight: 600 !important;
    color: #5a7fa8 !important;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}

input[type="text"], input[type="number"], input[type="password"] {
    background: #f5f8fc !important;
    border: 1.5px solid #dce8f5 !important;
    border-radius: 10px !important;
    color: #0d1b2a !important;
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-size: 0.95rem !important;
    padding: 0.6rem 0.9rem !important;
    transition: border-color 0.2s, box-shadow 0.2s;
}
input[type="text"]:focus, input[type="number"]:focus {
    border-color: #2563eb !important;
    box-shadow: 0 0 0 3px rgba(37,99,235,0.12) !important;
    background: #ffffff !important;
    outline: none !important;
}

.stButton > button {
    background: #0d1b2a !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.75rem 2.4rem !important;
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-size: 0.9rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.06em;
    transition: all 0.2s ease;
    box-shadow: 0 4px 16px rgba(13,27,42,0.18);
    margin-top: 0.8rem;
}
.stButton > button:hover {
    background: #1e3a5f !important;
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(13,27,42,0.22);
}
.stButton > button:active {
    transform: translateY(0);
}

.result-box {
    text-align: center;
    font-family: 'Syne', sans-serif;
    font-size: 1.7rem;
    font-weight: 700;
    margin-top: 1.5rem;
    padding: 1.2rem 2rem;
    border-radius: 14px;
    background: #f0f4f8;
    border: 1.5px solid #dce8f5;
    color: #0d1b2a;
    letter-spacing: -0.01em;
}

.stProgress > div > div {
    background: linear-gradient(90deg, #2563eb, #06b6d4) !important;
    border-radius: 999px !important;
}
.stProgress > div {
    background: #e2eaf3 !important;
    border-radius: 999px !important;
    height: 6px !important;
}

h1, h2, h3 {
    font-family: 'Syne', sans-serif !important;
    color: #0d1b2a !important;
}

.stSuccess {
    background: rgba(16,185,129,0.08) !important;
    border: 1px solid rgba(16,185,129,0.25) !important;
    border-radius: 10px !important;
    color: #065f46 !important;
}
.stError {
    background: rgba(239,68,68,0.08) !important;
    border: 1px solid rgba(239,68,68,0.25) !important;
    border-radius: 10px !important;
    color: #991b1b !important;
}
</style>
""", unsafe_allow_html=True)

diabetes_model = pickle.load(open("saved models/diabetes_model.sav", "rb"))
heart_model = pickle.load(open("saved models/heart_disease_model.sav", "rb"))
parkinsons_model = pickle.load(open("saved models/parkinsons_model.sav", "rb"))

with st.sidebar:
    st.markdown("## 🏥 Smart Health Assistant")
    menu = option_menu(
        "Select Diagnosis",
        ["Diabetes", "Heart Disease", "Parkinson's"],
        icons=["droplet", "heart-pulse", "brain"],
        menu_icon="clipboard2-pulse",
        default_index=0,
        styles={
            "container": {"background-color": "#0d1b2a", "padding": "0.5rem"},
            "icon": {"color": "#60a5fa", "font-size": "16px"},
            "nav-link": {
                "font-family": "'IBM Plex Sans', sans-serif",
                "font-size": "0.88rem",
                "color": "#c9d6e3",
                "border-radius": "10px",
                "margin": "3px 0",
            },
            "nav-link-selected": {
                "background-color": "#1e3a5f",
                "color": "#ffffff",
                "font-weight": "600",
            },
        }
    )

if menu == "Diabetes":
    st.markdown('<div class="main-title">🩸 Diabetes Prediction</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">AI-based health risk analysis</div>', unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)

        with c1:
            pregnancies = st.text_input("Pregnancies")
            skin = st.text_input("Skin Thickness")
            pedigree = st.text_input("Pedigree Function")

        with c2:
            glucose = st.text_input("Glucose Level")
            insulin = st.text_input("Insulin Level")
            age = st.text_input("Age")

        with c3:
            bp = st.text_input("Blood Pressure")
            bmi = st.text_input("BMI")

        st.markdown("</div>", unsafe_allow_html=True)

    diabetes_result = ""

    if st.button("Predict Diabetes", use_container_width=True):
        bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            bar.progress(i + 1)

        data = [pregnancies, glucose, bp, skin, insulin, bmi, pedigree, age]
        data = [float(i) for i in data]

        prediction = diabetes_model.predict([data])
        diabetes_result = "⚠️ Diabetes Detected" if prediction[0] == 1 else "✅ No Diabetes"

    st.markdown(f'<div class="result-box">{diabetes_result}</div>', unsafe_allow_html=True)

elif menu == "Heart Disease":
    st.markdown('<div class="main-title">❤️ Heart Disease Prediction</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Cardiac health assessment</div>', unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)

        with c1:
            age = st.text_input("Age")
            trestbps = st.text_input("Resting BP")
            restecg = st.text_input("ECG Result")

        with c2:
            sex = st.text_input("Sex (0/1)")
            chol = st.text_input("Cholesterol")
            thalach = st.text_input("Max Heart Rate")

        with c3:
            cp = st.text_input("Chest Pain Type")
            fbs = st.text_input("Fasting Blood Sugar")
            exang = st.text_input("Exercise Angina")

        c4, c5, c6 = st.columns(3)
        with c4:
            oldpeak = st.text_input("Oldpeak")
        with c5:
            slope = st.text_input("Slope")
        with c6:
            ca = st.text_input("CA")
            thal = st.text_input("Thal")

        st.markdown("</div>", unsafe_allow_html=True)

    heart_result = ""

    if st.button("Predict Heart Disease", use_container_width=True):
        bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            bar.progress(i + 1)

        values = [age, sex, cp, trestbps, chol, fbs, restecg,
                  thalach, exang, oldpeak, slope, ca, thal]
        values = [float(i) for i in values]

        prediction = heart_model.predict([values])
        heart_result = "⚠️ Heart Disease Detected" if prediction[0] == 1 else "✅ Healthy Heart"

    st.markdown(f'<div class="result-box">{heart_result}</div>', unsafe_allow_html=True)

elif menu == "Parkinson's":
    st.markdown('<div class="main-title">🧠 Parkinson\'s Prediction</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Voice signal analysis</div>', unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        cols = st.columns(4)
        features = []

        labels = [
            "Fo","Fhi","Flo","Jitter %","Jitter Abs",
            "RAP","PPQ","DDP","Shimmer","Shimmer dB",
            "APQ3","APQ5","APQ","DDA","NHR",
            "HNR","RPDE","DFA","Spread1","Spread2",
            "D2","PPE"
        ]

        for i, label in enumerate(labels):
            with cols[i % 4]:
                features.append(st.text_input(label))

        st.markdown("</div>", unsafe_allow_html=True)

    park_result = ""

    if st.button("Predict Parkinson's", use_container_width=True):
        bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            bar.progress(i + 1)

        features = [float(i) for i in features]
        prediction = parkinsons_model.predict([features])
        park_result = "⚠️ Parkinson's Detected" if prediction[0] == 1 else "✅ No Parkinson's"

    st.markdown(f'<div class="result-box">{park_result}</div>', unsafe_allow_html=True)
