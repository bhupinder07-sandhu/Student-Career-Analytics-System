import streamlit as st
import joblib
import numpy as np
from pathlib import Path

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Student Segmentation",
    page_icon="👥",
    layout="wide"
)

# -----------------------------
# Load Models
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

model = joblib.load(BASE_DIR / "models" / "kmeans_model.pkl")
scaler = joblib.load(BASE_DIR / "models" / "cluster_scaler.pkl")

# -----------------------------
# Title
# -----------------------------
st.title("👥 Student Segmentation")

st.write(
    "Identify which student performance group a student belongs to using K-Means Clustering."
)

st.markdown("---")

# -----------------------------
# Input Form
# -----------------------------
with st.form("cluster_form"):

    col1, col2 = st.columns(2)

    with col1:

        cgpa = st.number_input(
            "CGPA",
            min_value=6.5,
            max_value=9.1,
            value=7.5,
            step=0.1,
        )

        aptitude = st.number_input(
            "Aptitude Test Score",
            min_value=60,
            max_value=90,
            value=75,
            step=1,
        )

        projects = st.number_input(
            "Projects",
            min_value=0,
            max_value=3,
            value=1,
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
        "Identify Student Segment",
        use_container_width=True
    )

# -----------------------------
# Prediction
# -----------------------------
if predict:

    try:

        data = np.array([[
            cgpa,
            aptitude,
            softskills,
            projects,
            ssc,
            hsc
        ]])

        scaled = scaler.transform(data)

        cluster = model.predict(scaled)[0]

        st.markdown("---")

        st.success(f"Student belongs to **Cluster {cluster}**")

        st.subheader("Cluster Interpretation")

        if cluster == 0:

            st.info("""
### 📘 Cluster 0

Average-performing students.

**Recommendations**

- Improve aptitude skills.
- Complete more projects.
- Participate in workshops.
- Build technical knowledge.
""")

        elif cluster == 1:

            st.success("""
### 🌟 Cluster 1

High-performing students.

**Recommendations**

- Continue internships.
- Improve communication skills.
- Practice interviews.
- Apply for top companies.
""")

        elif cluster == 2:

            st.warning("""
### 📈 Cluster 2

Students with improvement opportunities.

**Recommendations**

- Improve CGPA.
- Focus on aptitude preparation.
- Complete additional certifications.
- Build practical projects.
""")

        else:

            st.info(f"Cluster {cluster} detected.")

    except Exception as e:

        st.error(f"Prediction Error : {e}")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")

st.caption("Student Career Analytics System (SCAS)")