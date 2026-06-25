import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About Student Career Analytics System")

st.markdown("---")

# -------------------------------------------------------
# Project Overview
# -------------------------------------------------------

st.header("📖 Project Overview")

st.write("""
The **Student Career Analytics System (SCAS)** is a Machine Learning-based application
developed to help students evaluate their placement readiness and academic performance.

The system analyzes a student's academic profile and provides:

- Placement Prediction
- Student Segmentation
- Career Guidance

The objective is to support students in identifying their strengths,
improving weak areas, and preparing effectively for future placements.
""")

st.markdown("---")

# -------------------------------------------------------
# Objectives
# -------------------------------------------------------

st.header("🎯 Project Objectives")

st.write("""
✔ Predict placement opportunities using Machine Learning.

✔ Group students into different performance clusters.

✔ Provide career guidance based on student profiles.

✔ Help students improve employability skills.

✔ Support data-driven career planning.
""")

st.markdown("---")

# -------------------------------------------------------
# Modules
# -------------------------------------------------------

st.header("📚 Project Modules")

col1, col2 = st.columns(2)

with col1:

    st.success("🎯 Placement Prediction")

    st.write("""
Predicts whether a student is likely to be placed using a Logistic Regression model.
""")

    st.success("👥 Student Segmentation")

    st.write("""
Groups students into similar categories using the K-Means Clustering algorithm.
""")

with col2:

    st.success("💼 Career Advisor")

    st.write("""
Provides personalized suggestions to improve placement readiness.
""")

    st.success("📊 Dashboard")

    st.write("""
Displays project information and overall system overview.
""")

st.markdown("---")

# -------------------------------------------------------
# Workflow
# -------------------------------------------------------

st.header("📈 Project Workflow")

st.info("""
Student Information

⬇

Data Preprocessing

⬇

Machine Learning Models

⬇

Prediction / Clustering

⬇

Career Recommendations

⬇

Final Result
""")

st.markdown("---")

# -------------------------------------------------------
# Machine Learning Models
# -------------------------------------------------------

st.header("🤖 Machine Learning Models")

st.table({
    "Module": [
        "Placement Prediction",
        "Student Segmentation"
    ],
    "Algorithm": [
        "Logistic Regression",
        "K-Means Clustering"
    ]
})

st.markdown("---")

# -------------------------------------------------------
# Team
# -------------------------------------------------------

st.header("👨‍💻 Project Team")

team1, team2 = st.columns(2)

with team1:

    st.info("""
### Bhupinder Sandhu
""")

    st.info("""
### Kriti
""")

with team2:

    st.info("""
### Bavneet

""")

    st.info("""
### Deepti

""")

st.markdown("---")

# -------------------------------------------------------
# Future Scope
# -------------------------------------------------------

st.header("🚀 Future Scope")

st.write("""
The project can be enhanced by adding:

• Resume Analyzer

• AI Career Chatbot

• Interview Preparation Module

• Company Recommendation System

• Skill Gap Analysis

• Job Recommendation System

• Real-time Placement Analytics
""")

st.markdown("---")

# -------------------------------------------------------
# Conclusion
# -------------------------------------------------------

st.header("🏁 Conclusion")

st.write("""
The Student Career Analytics System demonstrates how Machine Learning
can assist students in making informed career decisions.

By combining predictive analytics and clustering techniques,
the system provides meaningful insights that help students
prepare for placements and improve their career opportunities.
""")

st.markdown("---")

st.caption("Student Career Analytics System (SCAS)")
