import streamlit as st
import joblib
import numpy as np
from pathlib import Path

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Placement Prediction",
    page_icon="🎯",
    layout="wide"
)

# ---------------------------------------------------
# Load Model
# ---------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

model = joblib.load(BASE_DIR / "models" / "placement_model.pkl")
scaler = joblib.load(BASE_DIR / "models" / "placement_scaler.pkl")

# ---------------------------------------------------
# Title
# ---------------------------------------------------

st.title("🎯 Placement Prediction")

st.write(
    "Fill in the student's details below to predict whether the student is likely to be placed."
)

st.divider()

# ---------------------------------------------------
# Input Form
# ---------------------------------------------------

with st.form("placement_form"):

    col1, col2 = st.columns(2)

    with col1:

        cgpa = st.number_input(
            "CGPA",
            min_value=6.5,
            max_value=9.1,
            value=7.5,
            step=0.1,
        )

        internships = st.number_input(
            "Internships",
            min_value=0,
            max_value=2,
            value=1,
            step=1,
        )

        projects = st.number_input(
            "Projects",
            min_value=0,
            max_value=3,
            value=1,
            step=1,
        )

        workshops = st.number_input(
            "Workshops / Certifications",
            min_value=0,
            max_value=3,
            value=1,
            step=1,
        )

        aptitude = st.number_input(
            "Aptitude Test Score",
            min_value=60,
            max_value=90,
            value=75,
            step=1,
        )

    with col2:

        softskills = st.number_input(
            "Soft Skills Rating",
            min_value=3.0,
            max_value=4.8,
            value=4.0,
            step=0.1,
        )

        extracurricular = st.selectbox(
            "Extracurricular Activities",
            ["No", "Yes"]
        )

        placement_training = st.selectbox(
            "Placement Training",
            ["No", "Yes"]
        )

        ssc = st.number_input(
            "SSC Marks",
            min_value=55,
            max_value=90,
            value=75,
            step=1,
        )

        hsc = st.number_input(
            "HSC Marks",
            min_value=57,
            max_value=88,
            value=75,
            step=1,
        )

    predict = st.form_submit_button(
        "Predict Placement",
        use_container_width=True
    )

# ---------------------------------------------------
# Prediction
# ---------------------------------------------------

if predict:

    extracurricular = 1 if extracurricular == "Yes" else 0
    placement_training = 1 if placement_training == "Yes" else 0

    student = np.array([[
        cgpa,
        internships,
        projects,
        workshops,
        aptitude,
        softskills,
        extracurricular,
        placement_training,
        ssc,
        hsc
    ]])

    try:

        student = scaler.transform(student)

        prediction = model.predict(student)[0]

        probability = None

        if hasattr(model, "predict_proba"):
            probability = model.predict_proba(student)[0][1]

        st.divider()

        if prediction == 1:

            st.success("🎉 Prediction Result")

            st.success("The student is likely to be placed.")

        else:

            st.error("❌ Prediction Result")

            st.error("The student is not likely to be placed.")

        if probability is not None:

            st.subheader("Placement Confidence")

            st.progress(float(probability))

            st.metric(
                "Placement Probability",
                f"{probability*100:.2f}%"
            )

        st.subheader("Entered Details")

        st.table({
            "Feature": [
                "CGPA",
                "Internships",
                "Projects",
                "Workshops",
                "Aptitude",
                "Soft Skills",
                "Extracurricular",
                "Placement Training",
                "SSC Marks",
                "HSC Marks"
            ],
            "Value": [
                cgpa,
                internships,
                projects,
                workshops,
                aptitude,
                softskills,
                "Yes" if extracurricular else "No",
                "Yes" if placement_training else "No",
                ssc,
                hsc
            ]
        })

    except Exception as e:

        st.error(f"Prediction Error: {e}")

st.divider()

st.caption("Student Career Analytics System (SCAS)")