import streamlit as st
from PIL import Image
import pandas as pd
import base64

# ========== PAGE CONFIG ==========
st.set_page_config(
    page_title="M.SHAHBAZ KHAN | Portfolio",
    page_icon="🚀",
    layout="centered"
)

# ========== HELPER FUNCTIONS ==========
def skill_bar(level):
    """Creates a custom skill bar using Streamlit columns"""
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f"**{level}%**")
    with col2:
        st.progress(level)

# ========== HEADER SECTION ==========
col1, col2 = st.columns([1, 3])
# with col1:
#     # Replace with your image or keep placeholder
#     st.image("sss.jpeg")

with col2:
    st.title("M.Shahbaz khan")
    st.write("💌 **Email:** mak455790@gmail.com")
    st.write("📞 **Phone:** +92 324 3511956")
    st.write("🌐 **LinkedIn:** [linkedin.com/in/shahzad-ahmed](https://linkedin.com)")
    st.write("💻 **GitHub:** [github.com/shahzad-ahmed](https://github.com)")

st.markdown("---")

# ========== ABOUT SECTION ==========
st.header("👨‍💻 About Me")
st.write("""
I am a **Bachlor in Media Science** at **Sindh University** with a strong foundation in computer science principles. 
My educational journey began at Saifer College where I completed my Intermediate studies. 

Currently, I'm expanding my skills in **Python programming** and exploring its applications in software development. 
I hold professional certifications in **ACIT Computer Course** and **English Diploma**, which have equipped me with 
both technical and communication skills.
""")

# ========== EDUCATION SECTION ==========
st.header("🎓 Education")
edu_data = [
    {"Degree": "Intermediate", "Institute": "Saifer College", "Year": "2018-2020"},

]

for edu in edu_data:
    with st.expander(f"{edu['Degree']} - {edu['Institute']}"):
        st.write(f"**Institution:** {edu['Institute']}")
        if "Major" in edu:
            st.write(f"**Major:** {edu['Major']}")
        st.write(f"**Years:** {edu['Year']}")

# ========== CERTIFICATIONS ==========
st.header("📜 Certifications")
cert_col1, cert_col2 = st.columns(2)

with cert_col1:
    with st.container(border=True):
        st.subheader("CIT Computer Course")
        st.caption("python developer")

with cert_col2:
    with st.container(border=True):
        st.subheader("English Diploma")
        st.write("Professional English Communication")
        st.caption("Focus: Business English, Technical Writing, Presentation Skills")

# ========== SKILLS SECTION ==========
st.header("🛠️ Technical Skills")
skills = {
    "Python Programming": 75,
    "Problem Solving": 90,
    "Computer Fundamentals": 85,
    "English Communication": 80
}

for skill, level in skills.items():
    st.subheader(skill)
    skill_bar(level)

# ========== PROJECTS SECTION ===========
st.header("🚀 Projects")
project_tab1, project_tab2 = st.tabs(["Python Projects", "Academic Projects"])

with project_tab1:
    with st.expander("Personal Portfolio Website", expanded=True):
        st.write("""
        - Built with **Streamlit** (this website!)
        - Features interactive elements and clean UI
        - Deployed on Streamlit Cloud
        """)
    
    with st.expander("Automated Task Manager"):
        st.write("""
        - Python application with SQLite database
        - Features task scheduling and reminders
        - Command-line interface version
        """)

with project_tab2:
    st.write("""
    - **University Management System** (Database Course Project)
    - **E-Commerce Website Prototype** (Web Development Course)
    - **AI-based Simple Chatbot** (AI Fundamentals Course)
    """)

# ========== CONTACT SECTION ==========
st.header("📩 Get In Touch")

with st.form("contact_form"):
    name = st.text_input("Your Name", placeholder="Enter your name")
    email = st.text_input("Your Email", placeholder="Enter your email")
    message = st.text_area("Your Message", placeholder="Type your message here")
    
    submitted = st.form_submit_button("Send Message")
    if submitted:
        if name and email and message:
            st.success("Thank you! Your message has been sent.")
        else:
            st.warning("Please fill in all fields")

# ========== FOOTER ==========
st.markdown("---")
st.markdown("© 2024 Shahzad Ahmed | Made with Streamlit")