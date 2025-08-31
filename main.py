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
        <h1>👋 Hi, I'm Sahil</h1>
        <h3>Data Scientist | AI Enthusiast | Problem Solver</h3>
        <p style="font-size: 1.1rem; margin-top: 1rem; opacity: 0.9;">
            I build intelligent systems, scrapers, and data-driven applications. 
            Welcome to my portfolio where I showcase my passion for technology and innovation!
        </p>
    </div>
""", unsafe_allow_html=True)

# ---- MAIN CONTENT LAYOUT ----
left_col, right_col = st.columns([1, 1])

# ---- LEFT COLUMN ----
with left_col:
    st.markdown('<h2 class="section-header">About Me</h2>', unsafe_allow_html=True)
    st.markdown("""
    I am a passionate data scientist and AI enthusiast with a love for building intelligent systems 
    that solve real-world problems. My journey in technology has led me to specialize in:
    
    🔹 **Data Science & Machine Learning**  
    🔹 **Web Scraping & Automation**  
    🔹 **AI-Powered Applications**  
    🔹 **Full-Stack Development**  
    
    Currently, I'm focused on developing job scraping applications, automation pipelines, 
    and AI-powered tools that help businesses and individuals make better decisions.
    """)

    st.markdown("### Quick Facts")
    st.markdown("""
    - 🎓 **Education**: Computer Science/Data Science  
    - 🌍 **Location**: Remote/Worldwide  
    - 💼 **Experience**: 3+ years in tech  
    - 🚀 **Projects**: 10+ completed  
    - 🏆 **Specialties**: Python, ML, Automation  
    """)

    st.markdown('<h2 class="section-header">Skills & Technologies</h2>', unsafe_allow_html=True)
    
    st.subheader("🖥️ Programming Languages")
    lang_cols = st.columns(2)
    for i, lang in enumerate(["Python", "JavaScript", "SQL", "R"]):
        with lang_cols[i % 2]:
            st.markdown(f'<div class="skill-card">{lang}</div>', unsafe_allow_html=True)

    st.subheader("🛠️ Frameworks & Tools")
    tool_cols = st.columns(2)
    for i, tool in enumerate(["Streamlit", "Pandas", "Scikit-learn", "TensorFlow", "BeautifulSoup", "Selenium", "Git", "Docker"]):
        with tool_cols[i % 2]:
            st.markdown(f'<div class="skill-card">{tool}</div>', unsafe_allow_html=True)

    st.subheader("📊 Data & Analytics")
    data_cols = st.columns(2)
    for i, skill in enumerate(["Data Visualization", "Statistical Analysis", "ETL Pipelines", "Database Design"]):
        with data_cols[i % 2]:
            st.markdown(f'<div class="skill-card">{skill}</div>', unsafe_allow_html=True)

    st.markdown('<h2 class="section-header">Contact Me</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="contact-section">
        <h3>Let's Connect! 🤝</h3>
        <p>I'm always interested in new opportunities and collaborations. 
        Feel free to reach out if you'd like to work together!</p>
        <p>📧 <a href="mailto:sahil@example.com" style="color:white;">sahil@example.com</a></p>
        <p>🔗 <a href="https://linkedin.com" target="_blank" style="color:white;">LinkedIn</a></p>
        <p>🐙 <a href="https://github.com" target="_blank" style="color:white;">GitHub</a></p>
    </div>
    """, unsafe_allow_html=True)

# ---- RIGHT COLUMN ----
with right_col:
    st.markdown('<h2 class="section-header">Professional Experience</h2>', unsafe_allow_html=True)
    st.markdown("""
    ### 🏢 Senior Data Scientist | Tech Company (2022 - Present)  
    - Led ML model development for segmentation  
    - Built automated pipelines (1M+ records/day)  
    - Mentored junior data scientists  
    
    ### 🎓 Data Science Intern | Startup (2021 - 2022)  
    - Built web scraping solutions  
    - Developed predictive models for sales forecasting  
    
    ### 🚀 Freelance Projects (2020 - Present)  
    - E-commerce analytics  
    - Social media scraping  
    - Workflow automation  
    """)

    st.markdown('<h2 class="section-header">Featured Projects</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="project-card">
        <h3>📊 Job Scraper Web App</h3>
        <p>A Streamlit app that scrapes job listings with filtering & export features.</p>
        <p><strong>Stack:</strong> Python, Streamlit, BeautifulSoup, Pandas, SQLite</p>
    </div>
    <div class="project-card">
        <h3>🔍 E-commerce Analytics Dashboard</h3>
        <p>Real-time analytics dashboard tracking sales & customer behavior.</p>
        <p><strong>Stack:</strong> Python, Streamlit, Plotly, PostgreSQL</p>
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
        <p>© 2024 Sahil's Portfolio | Built with ❤️ using Streamlit</p>
    </div>
""", unsafe_allow_html=True)
