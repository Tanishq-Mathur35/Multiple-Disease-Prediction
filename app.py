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
body {
    background-color: #f5f7fb;
}
.main-title {
    text-align: center;
    font-size: 44px;
    font-weight: 800;
    color: #1f2937;
}
.sub-title {
    text-align: center;
    font-size: 20px;
    color: #4f46e5;
    margin-bottom: 30px;
}
.card {
    background: white;
    padding: 30px;
    border-radius: 18px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.08);
    margin-bottom: 25px;
}
.result-box {
    text-align: center;
    font-size: 24px;
    font-weight: 700;
    margin-top: 20px;
}
input {
    border-radius: 10px !important;
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
        ["Diabetes", "Heart Disease", "Parkinson’s"],
        icons=["droplet", "heart-pulse", "brain"],
        menu_icon="clipboard2-pulse",
        default_index=0
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



elif menu == "Parkinson’s":

    st.markdown('<div class="main-title">🧠 Parkinson’s Prediction</div>', unsafe_allow_html=True)
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

    if st.button("Predict Parkinson’s", use_container_width=True):
        bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            bar.progress(i + 1)

        features = [float(i) for i in features]
        prediction = parkinsons_model.predict([features])
        park_result = "⚠️ Parkinson’s Detected" if prediction[0] == 1 else "✅ No Parkinson’s"

    st.markdown(f'<div class="result-box">{park_result}</div>', unsafe_allow_html=True)

