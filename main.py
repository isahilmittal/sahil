import streamlit as st
from streamlit_lottie import st_lottie
import requests
import sys
import os

# Add burger_maker directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'burger_maker'))

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Sahil's Portfolio", page_icon="💼", layout="wide")

# init session state
if "burger_page" not in st.session_state:
    st.session_state.burger_page = "portfolio"

# decide which page to show
if st.session_state.burger_page == "portfolio":
    # Portfolio content will be shown below
    pass
elif st.session_state.burger_page == "burger_home":
    import burger_home
    burger_home.show()
    st.stop()  # Stop execution here, don't show portfolio content
elif st.session_state.burger_page == "burger_builder":
    import burger_maker
    burger_maker.show()
    st.stop()  # Stop execution here, don't show portfolio content


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

# ---- LEFT COLUMN: PERSONAL, SKILLS & CONTACT ----
with left_col:
    # About Me
    st.markdown('<h2 class="section-header">About Me</h2>', unsafe_allow_html=True)
    st.markdown("""
    I am a passionate data scientist and AI enthusiast with a love for building intelligent systems 
    that solve real-world problems. My journey in technology has led me to specialize in:
    
    🔹 **Data Science & Machine Learning** - Building predictive models and data-driven insights  
    🔹 **Web Scraping & Automation** - Creating efficient data collection and processing pipelines  
    🔹 **AI-Powered Applications** - Developing intelligent systems that enhance user experiences  
    🔹 **Full-Stack Development** - Building complete solutions from data to deployment  
    
    Currently, I'm focused on developing job scraping applications, automation pipelines, 
    and AI-powered tools that help businesses and individuals make better decisions.
    """)

    # Quick Facts
    st.markdown("""
    ### Quick Facts
    - 🎓 **Education**: Computer Science/Data Science
    - 🌍 **Location**: Remote/Worldwide
    - 💼 **Experience**: 3+ years in tech
    - 🚀 **Projects**: 10+ completed
    - 🏆 **Specialties**: Python, ML, Automation
    """)

    # Skills
    st.markdown('<h2 class="section-header">Skills & Technologies</h2>', unsafe_allow_html=True)
    
    # Programming Languages
    st.subheader("🖥️ Programming Languages")
    lang_cols = st.columns(2)
    languages = ["Python", "JavaScript", "SQL", "R"]
    for i, lang in enumerate(languages):
        with lang_cols[i % 2]:
            st.markdown(f'<div class="skill-card">{lang}</div>', unsafe_allow_html=True)

    # Frameworks & Tools
    st.subheader("🛠️ Frameworks & Tools")
    tool_cols = st.columns(2)
    tools = ["Streamlit", "Pandas", "Scikit-learn", "TensorFlow", "BeautifulSoup", "Selenium", "Git", "Docker"]
    for i, tool in enumerate(tools):
        with tool_cols[i % 2]:
            st.markdown(f'<div class="skill-card">{tool}</div>', unsafe_allow_html=True)

    # Additional Skills
    st.subheader("📊 Data & Analytics")
    data_cols = st.columns(2)
    data_skills = ["Data Visualization", "Statistical Analysis", "ETL Pipelines", "Database Design"]
    for i, skill in enumerate(data_skills):
        with data_cols[i % 2]:
            st.markdown(f'<div class="skill-card">{skill}</div>', unsafe_allow_html=True)

    # Contact Section
    st.markdown('<h2 class="section-header">Contact Me</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="contact-section">
        <h3>Let's Connect! 🤝</h3>
        <p style="font-size: 1rem; margin-bottom: 1rem;">
            I'm always interested in new opportunities and collaborations. 
            Feel free to reach out if you'd like to work together!
        </p>
        <div style="text-align: center;">
            <p style="margin: 0.5rem 0;">📧 <a href="mailto:sahil@example.com" style="color: white;">sahil@example.com</a></p>
            <p style="margin: 0.5rem 0;">🔗 <a href="https://linkedin.com" target="_blank" style="color: white;">LinkedIn</a></p>
            <p style="margin: 0.5rem 0;">🐙 <a href="https://github.com" target="_blank" style="color: white;">GitHub</a></p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---- RIGHT COLUMN: PROJECTS & EXPERIENCE ----
with right_col:
    # Experience Section
    st.markdown('<h2 class="section-header">Professional Experience</h2>', unsafe_allow_html=True)
    st.markdown("""
    ### 🏢 Senior Data Scientist
    **Tech Company** | 2022 - Present
    
    - Led development of machine learning models for customer segmentation
    - Built automated data pipelines processing 1M+ records daily
    - Mentored junior data scientists and conducted technical interviews
    - Reduced data processing time by 60% through optimization
    
    ### 🎓 Data Science Intern
    **Startup** | 2021 - 2022
    
    - Developed web scraping solutions for market research
    - Created predictive models for sales forecasting
    - Built interactive dashboards for stakeholder reporting
    
    ### 🚀 Freelance Projects
    **Various Clients** | 2020 - Present
    
    - **E-commerce Analytics**: Built customer behavior analysis tools
    - **Social Media Scraping**: Developed tools for trend analysis
    - **Automation Solutions**: Created workflow automation for small businesses
    
    ### 🏆 Achievements
    - **Certified Data Scientist** - IBM Professional Certificate
    - **Machine Learning Specialization** - Coursera
    - **Top 10%** in Kaggle competitions
    - **Speaker** at local tech meetups
    """)

    # Projects Section
    st.markdown('<h2 class="section-header">Featured Projects</h2>', unsafe_allow_html=True)

    # Project 1
    st.markdown("""
    <div class="project-card">
        <h3>📊 Job Scraper Web App</h3>
        <p>A comprehensive Streamlit application that scrapes job listings from multiple sources based on city and category preferences. Features include real-time data collection, filtering, and export capabilities.</p>
        <p><strong>Tech Stack:</strong> Python, Streamlit, BeautifulSoup, Pandas, SQLite</p>
        <p><strong>Features:</strong> Multi-source scraping, Advanced filtering, Data export, Real-time updates</p>
        <p><strong>Impact:</strong> Helps job seekers find relevant opportunities quickly and efficiently</p>
    </div>
    """, unsafe_allow_html=True)

    # Project 3 - Burger Maker
    st.markdown("""
    <div class="project-card">
        <h3>🍔 Burger Maker 3000</h3>
        <p>A fun and interactive app where you can build your own burger Subway-style! 
        Select buns, patties, cheese, toppings, and see your burger come alive with animations 
        and calorie counter.</p>
        <p><strong>Tech Stack:</strong> Streamlit, Lottie Animations, Python</p>
        <p><strong>Features:</strong> Interactive UI, Real-time burger building, Fun animations</p>
        <p><strong>Impact:</strong> Makes learning Streamlit fun & engaging through food! 😋</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("👉 Launch Burger Maker", key="burger_button"):
        st.session_state.burger_page = "burger_home"  # switch to burger app
        st.rerun()  # refresh to trigger navigation

   

    # Project 4
    st.markdown("""
    <div class="project-card">
        <h3>🔍 E-commerce Analytics Dashboard</h3>
        <p>A real-time analytics dashboard for e-commerce businesses that tracks sales, customer behavior, and inventory metrics.</p>
        <p><strong>Tech Stack:</strong> Python, Streamlit, Plotly, PostgreSQL</p>
        <p><strong>Features:</strong> Real-time data visualization, Interactive charts, Automated reporting</p>
        <p><strong>Impact:</strong> Provides actionable insights for business growth and optimization</p>
    </div>
    """, unsafe_allow_html=True)





# ---- RESUME DOWNLOAD ----
st.markdown('<h2 class="section-header">Resume</h2>', unsafe_allow_html=True)
st.markdown("""
    Download my detailed resume to learn more about my experience, education, and technical skills.
""")

# Create a download button with the actual resume file
try:
    with open("assets/sahil_resume.pdf", "rb") as file:
        st.download_button(
            label="📄 Download Resume (PDF)",
            data=file.read(),
            file_name="Sahil_Resume.pdf",
            mime="application/pdf"
        )
except FileNotFoundError:
    st.error("Resume file not found. Please ensure 'assets/sahil_resume.pdf' exists.")

# ---- FOOTER ----
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #666; padding: 2rem;">
        <p>© 2024 Sahil's Portfolio | Built with ❤️ using Streamlit</p>
    </div>
""", unsafe_allow_html=True)
