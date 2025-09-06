import streamlit as st
import os

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Sahil's Portfolio", page_icon="💼", layout="wide")

# ---- CUSTOM CSS ----
st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
    }
    .main-header h1 {
        color: white !important;
        font-size: 3rem !important;
        margin-bottom: 0.5rem;
    }
    .main-header h3 {
        color: #f0f0f0 !important;
        font-weight: 300;
    }
    .skill-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .project-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    .contact-section {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
    }
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    .section-header {
        color: #667eea;
        font-size: 2rem;
        margin-bottom: 1rem;
        border-bottom: 3px solid #667eea;
        padding-bottom: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# ---- HEADER SECTION ----
st.markdown("""
    <div class="main-header">
        <h1>👋 Hi, I'm Sahil Mittal</h1>
        <h3>MIS Executive | Data Analyst</h3>
        <p style="font-size: 1.1rem; margin-top: 1rem; opacity: 0.9;">
            Passionate and detail-oriented Data Analyst with expertise in SQL, Python, Excel, Tableau, and Power BI. 
            I specialize in transforming raw data into actionable insights to support business decision-making.
        </p>
    </div>
""", unsafe_allow_html=True)

# ---- MAIN CONTENT LAYOUT ----
left_col, right_col = st.columns([1, 1])

# ---- LEFT COLUMN ----
with left_col:
    st.markdown('<h2 class="section-header">About Me</h2>', unsafe_allow_html=True)
    st.markdown("""
    I am an MIS Executive and Data Analyst with strong skills in **SQL, Python, Excel, Tableau, and Power BI**. 
    I enjoy analyzing complex datasets, building dashboards, and providing business insights that drive decisions.
    
    **Strengths:**
    - Data Cleaning, Transformation & Analysis
    - SQL Querying & Database Management
    - Power BI & Tableau Dashboards
    - MIS Reporting & Automation (Excel, VBA)
    """)

    st.markdown("<h2 class=\"section-header\">Key Skills</h2>", unsafe_allow_html=True)

    skill_cols = st.columns(2)
    skills = ["Power BI", "Tableau", "Excel (Advanced)", "VBA", "SQL", "Python (Pandas, NumPy, Seaborn)"]
    for i, skill in enumerate(skills):
        with skill_cols[i % 2]:
            st.markdown(f'<div class="skill-card">{skill}</div>', unsafe_allow_html=True)

    st.markdown('<h2 class="section-header">Certifications</h2>', unsafe_allow_html=True)
    st.markdown("""
    - Certified Data Analyst – SLA Consultants  
    - SQL Certification – HackerRank  
    - Python Certification – HackerRank  
    """)

    st.markdown('<h2 class="section-header">Contact Me</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="contact-section">
        <h3>Let's Connect! 🤝</h3>
        <p>📧 <a href="mailto:sahilmittal656@gmail.com" style="color:white;">sahilmittal656@gmail.com</a></p>
        <p>📞 +91 8930593945</p>
        <p>🔗 <a href="https://linkedin.com/in/sahil-mittal-594587166/" target="_blank" style="color:white;">LinkedIn</a></p>
    </div>
    """, unsafe_allow_html=True)

# ---- RIGHT COLUMN ----
with right_col:
    st.markdown('<h2 class="section-header">Professional Experience</h2>', unsafe_allow_html=True)
    st.markdown("""
    ### 🏢 MIS Executive & Data Analyst | SLA Consultants, Delhi (Sept 2023 - Dec 2024)
    - Developed interactive dashboards using **Power BI**.
    - Performed **data cleaning, transformation, and analysis** using Excel and Python.
    - Automated reporting workflows with **VBA**.
    - Generated detailed analytical reports summarizing methodologies & insights.
    """)

    st.markdown('<h2 class="section-header">Projects</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="project-card">
        <h3>📊 Grocery Store Sales Analysis</h3>
        <p>Analyzed sales data using SQL & Python to identify trends and opportunities.</p>
    </div>
    <div class="project-card">
        <h3>⚙️ VBA Data Compiler</h3>
        <p>Automated the compilation of multiple Excel files into a single workbook.</p>
    </div>
    <div class="project-card">
        <h3>🎬 RSVP Movies Dataset Analysis</h3>
        <p>SQL-based analysis to derive insights and optimize production planning & marketing strategies.</p>
    </div>
    <div class="project-card">
        <h3>💳 Loan Default Risk Analytics</h3>
        <p>Developed risk profiles to minimize credit risk and support lending decisions.</p>
    </div>
    """, unsafe_allow_html=True)

# ---- RESUME ----
st.markdown('<h2 class="section-header">Resume</h2>', unsafe_allow_html=True)
try:
    with open("assets/sahil_resume.pdf", "rb") as file:
        st.download_button("📄 Download Resume (PDF)", file.read(), "Sahil_Resume.pdf", "application/pdf")
except FileNotFoundError:
    st.warning("Resume file not found. Place it in `assets/sahil_resume.pdf`.")

# ---- FOOTER ----
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #666; padding: 2rem;">
        <p>© 2025 Sahil Mittal | Portfolio built with ❤️ using Streamlit</p>
    </div>
""", unsafe_allow_html=True)
