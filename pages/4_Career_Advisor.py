import streamlit as st

st.set_page_config(
    page_title="Career Advisor",
    page_icon="💼",
    layout="wide"
)

st.title("💼 Career Advisor")

st.write("Receive personalized career guidance based on your academic profile.")

st.markdown("---")

with st.form("career_form"):

    col1, col2 = st.columns(2)

    with col1:

        cgpa = st.number_input(
            "CGPA",
            min_value=6.5,
            max_value=9.1,
            value=7.5,
            step=0.1
        )

        internships = st.number_input(
            "Internships",
            min_value=0,
            max_value=2,
            value=1
        )

        projects = st.number_input(
            "Projects",
            min_value=0,
            max_value=3,
            value=1
        )

        workshops = st.number_input(
            "Workshops / Certifications",
            min_value=0,
            max_value=3,
            value=1
        )

        aptitude = st.number_input(
            "Aptitude Test Score",
            min_value=60,
            max_value=90,
            value=75
        )

    with col2:

        softskills = st.number_input(
            "Soft Skills Rating",
            min_value=3.0,
            max_value=4.8,
            value=4.0,
            step=0.1
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
            value=75
        )

        hsc = st.number_input(
            "HSC Marks",
            min_value=57,
            max_value=88,
            value=75
        )

    submit = st.form_submit_button(
        "Generate Career Advice",
        use_container_width=True
    )

if submit:

    st.markdown("---")

    recommendations = []

    if cgpa < 7.5:
        recommendations.append(
            "📚 Improve your CGPA by focusing on academic performance."
        )

    if internships == 0:
        recommendations.append(
            "🏢 Complete at least one internship to gain industry exposure."
        )

    if projects < 2:
        recommendations.append(
            "💻 Build more real-world projects to strengthen your portfolio."
        )

    if workshops < 2:
        recommendations.append(
            "📜 Attend workshops and earn professional certifications."
        )

    if aptitude < 75:
        recommendations.append(
            "🧠 Practice aptitude questions daily to improve placement readiness."
        )

    if softskills < 4.0:
        recommendations.append(
            "🗣 Improve communication and presentation skills."
        )

    if extracurricular == "No":
        recommendations.append(
            "🎯 Participate in extracurricular activities to develop leadership skills."
        )

    if placement_training == "No":
        recommendations.append(
            "🎓 Join placement training sessions for interview preparation."
        )

    if ssc < 70:
        recommendations.append(
            "📖 Strengthen your fundamental academic knowledge."
        )

    if hsc < 70:
        recommendations.append(
            "📘 Improve your higher secondary academic performance."
        )

    score = 0

    if cgpa >= 8:
        score += 1
    if internships >= 1:
        score += 1
    if projects >= 2:
        score += 1
    if aptitude >= 75:
        score += 1
    if softskills >= 4:
        score += 1
    if placement_training == "Yes":
        score += 1

    if score >= 5:
        st.success("🌟 Excellent Profile")
    elif score >= 3:
        st.warning("👍 Good Profile")
    else:
        st.error("⚠ Needs Improvement")

    st.subheader("📋 Personalized Recommendations")

    if recommendations:
        for rec in recommendations:
            st.write(rec)
    else:
        st.success(
            "🎉 Excellent! Your profile is strong. Continue improving your skills and keep practicing interviews."
        )

st.markdown("---")

st.caption("Student Career Analytics System (SCAS)")