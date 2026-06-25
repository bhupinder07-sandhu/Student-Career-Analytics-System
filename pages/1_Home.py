import streamlit as st

st.set_page_config(
    page_title="Student Career Analytics System",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Career Analytics System")
st.subheader("AI-Powered Career Guidance Platform")

st.markdown("---")

# -------------------------------------------------------
# Project Overview
# -------------------------------------------------------

st.header("📖 Project Overview")

st.write("""
The **Student Career Analytics System (SCAS)** is a Machine Learning-based
web application that helps students evaluate their placement readiness,
analyze academic performance, and receive career guidance.

The application uses predictive analytics and clustering techniques
to provide meaningful insights that help students prepare for placements.
""")

st.markdown("---")

# -------------------------------------------------------
# Dashboard
# -------------------------------------------------------

st.header("📊 Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Students", "10,000+")

with col2:
    st.metric("ML Models", "2")

with col3:
    st.metric("Modules", "3")

with col4:
    st.metric("Accuracy", "80%")

st.markdown("---")

# -------------------------------------------------------
# Features
# -------------------------------------------------------

st.header("✨ Key Features")

col1, col2 = st.columns(2)

with col1:
    st.success("🎯 Placement Prediction")
    st.success("👥 Student Segmentation")

with col2:
    st.success("💼 Career Advisor")
    st.success("📊 Interactive Dashboard")

st.markdown("---")

# -------------------------------------------------------
# Objectives
# -------------------------------------------------------

st.header("🎯 Project Objectives")

st.markdown("""
- Predict placement opportunities using Machine Learning.
- Analyze student academic performance.
- Group students into meaningful clusters.
- Provide personalized career guidance.
- Support students in making informed career decisions.
""")

st.markdown("---")

# -------------------------------------------------------
# Workflow
# -------------------------------------------------------

st.header("📈 Project Workflow")

st.info("""
Student Details

⬇

Data Preprocessing

⬇

Machine Learning Models

⬇

Prediction & Analysis

⬇

Results & Recommendations
""")

st.markdown("---")

# -------------------------------------------------------
# Modules
# -------------------------------------------------------

st.header("📚 Project Modules")

col1, col2 = st.columns(2)

with col1:

    st.subheader("🎯 Placement Prediction")

    st.write("""
Predicts whether a student is likely to be placed based on
academic performance and skill-related information.
""")

    st.subheader("👥 Student Segmentation")

    st.write("""
Groups students into similar performance categories
using Machine Learning clustering techniques.
""")

with col2:

    st.subheader("💼 Career Advisor")

    st.write("""
Provides personalized recommendations to improve
placement readiness and career opportunities.
""")

    st.subheader("ℹ️ About")

    st.write("""
Displays project information, objectives,
workflow and future scope.
""")

st.markdown("---")

# -------------------------------------------------------
# Team Members
# -------------------------------------------------------

st.header("👨‍💻 Team Members")

col1, col2 = st.columns(2)

with col1:
    st.info("""
### 👤 Bhupinder Sandhu

Project Team Member
""")

    st.info("""
### 👤 Kriti

Project Team Member
""")

with col2:
    st.info("""
### 👤 Bavneet

Project Team Member
""")

    st.info("""
### 👤 Deepti

Project Team Member
""")

st.markdown("---")

# -------------------------------------------------------
# Future Scope
# -------------------------------------------------------

st.header("🚀 Future Scope")

st.markdown("""
- Resume Analyzer
- AI Career Chatbot
- Interview Preparation
- Skill Gap Analysis
- Job Recommendation System
- Company Recommendation
""")

st.markdown("---")

# -------------------------------------------------------
# Footer
# -------------------------------------------------------

st.success("Thank you for using the Student Career Analytics System.")

st.caption("Developed as a Machine Learning Project using Streamlit.")
