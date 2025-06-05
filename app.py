import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Hussein Ali",
    page_icon="🐉",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject CSS for UI tweaks and footer styling
st.markdown("""
    <style>
    /* Hide main menu, footer, header */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Hide sidebar collapse button */
    [data-testid="collapsedControl"] {
        display: none;
    }

    /* Fix sidebar width */
    section[data-testid="stSidebar"] {
        min-width: 300px;
        max-width: 300px;
    }

    /* Center and resize sidebar image */
    .sidebar .stImage > img {
        max-width: 100%;
        height: auto;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }

    /* Footer styling */
    .footer {
        text-align: center;
        font-size: 0.85rem;
        color: #666666;  /* improved visibility */
        margin-top: 3rem;
        margin-bottom: 2rem;
        padding-bottom: 10px;
    }

    /* Link styles */
    a {
        color: #0A66C2;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

import streamlit as st

# Load your resume PDF
with open("./assets/docs/hussein-ali.pdf", "rb") as f:
    resume_data = f.read()

# Sidebar content
st.sidebar.image(
    "./assets/images/profile.png",  # Replace with your real image path or URL
    use_container_width=True
)
st.sidebar.title("Hussein Ali")
st.sidebar.markdown("**Data Scientist / ML Engineer**")
st.sidebar.markdown(
    """
    [LinkedIn](https://www.linkedin.com/in/xwsain) | 
    [Kaggle](https://www.kaggle.com/xwsein) | 
    [YouTube](https://www.youtube.com/@xwsein) | 
    [GitHub](https://www.github.com/xwsein)
    """,
    unsafe_allow_html=True
)

# Download Resume button
st.sidebar.download_button(
    label="📄 Download Resume",
    data=resume_data,
    file_name="hussein-ali.pdf",
    mime="application/pdf"
)

# Main content
st.title("Hi, I'm Hussein Ali")
st.markdown("""
Data-driven problem solver with a Bachelor’s degree in Computer Science and proven experience in data analytics, machine learning, and business intelligence. Proficient in Python, SQL, Power BI, and data visualization. Skilled in building predictive models, automating reporting, and designing dashboards that drive business insights. Strong foundation in statistics, programming, and cloud technologies (AWS, Azure). Seeking challenging roles in Data Analytics, Machine Learning, or Data Science to deliver actionable insights and measurable business impact.
""")

st.header("Skills")
st.markdown("""
- **Technologies & Tools:** Python (NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, PyTorch), C, Power BI, Looker, Excel, PostgreSQL, MongoDB, AWS, Azure, Git, GitHub, Jupyter Notebook, VS Code.

- **Technical Skills:** Data collection, cleaning, modeling, exploratory data analysis, feature engineering, statistical testing, predictive modeling, model evaluation, A/B testing, dashboard creation, KPI tracking, root cause analysis, pipeline automation, deployment, monitoring.

- **Soft Skills:** Analytical thinking, structured problem-solving, effective communication, teamwork, time management, adaptability.
""")

st.header("Experience")

st.subheader("Data Analyst Intern – COB Solution (Feb 2023 – Aug 2023)")
st.markdown("""
- Developed dashboards for billing and auditing using Power BI and Excel.  
- Automated reporting processes, reducing manual work.  
- Performed financial analytics on claims and performance data.  
""")

st.subheader("Applied Data Scientist – WorldQuant University (Mar 2022 – Sep 2022)")
st.markdown("""
- Built ML models and performed exploratory data analysis using Python.  
- Delivered mini-projects on finance and real estate data.  
""")

st.subheader("Data Analyst Intern – Business Spike (Jul 2021 – Jan 2022)")
st.markdown("""
- Predicted market behavior and customer trends using Python.  
- Analyzed investment data for strategic decision-making.  
""")

st.header("Education")

st.subheader("Information Technology Institute (ITI) – Data Analyst Track")
st.markdown("""
- Completed a focused learning track in data analytics and visualization with hands-on experience in Python, R, SQL, Power BI, and Tableau.  
- Developed practical skills in data cleaning, exploratory analysis, dashboard creation, and cloud-based data processing using AWS and Azure.  
""")

st.subheader("Beni-Suef University – B.Sc. Computer Science")
st.markdown("""
- Graduated with a focus on Data Science and Artificial Intelligence, acquiring strong theoretical and practical knowledge in algorithms and AI techniques.  
- Completed coursework and projects emphasizing data science principles, software development, and programming skills.  
""")

st.header("Projects")
st.markdown("""
**M2 Medical Assistant (Graduation Project)**  
- Developed deep learning and computer vision models to detect multiple medical conditions.  
- Integrated large language model (LLM) for natural language diagnoses and treatment suggestions.

**PROPIX Real Estate Market Analysis**  
- Scraped property data and applied regression and clustering techniques for price prediction.  
- Created a web dashboard enabling non-technical users to explore market insights.

**SCHEDULIZER CPU Scheduling Python Package**  
- Developed a Python package simulating CPU scheduling algorithms for operating systems education.

**ROGEN Rocket Trajectory Simulator**  
- Designed a web-based simulation applying genetic algorithms to model rocket trajectories and optimize accuracy.
""")

st.header("Certifications")
st.markdown("""
- Microsoft Machine Learning Engineer – DEPI (Oct 2024)  
- Google Data Analytics Professional Certificate – Coursera (Jan 2023)  
- ITI Data Analyst Track – Information Technology Institute (Dec 2022)  
- Data Analysis with Python – freeCodeCamp (Jul 2022)
""")

st.header("Contact")
st.markdown("""
<ul style="list-style-type:none; padding-left:0;">
  <li style="margin-bottom:8px;"><strong>Location:</strong> Cairo, Egypt</li>
  <li style="margin-bottom:8px;"><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/xwsain" target="_blank">linkedin.com/in/xwsain</a></li>
  <li style="margin-bottom:8px;"><strong>Old Kaggle:</strong> <a href="https://www.kaggle.com/thisishusseinali" target="_blank">kaggle.com/thisishusseinali</a></li>
  <li style="margin-bottom:8px;"><strong>Old Github:</strong> <a href="https://www.github.com/thisishusseinali" target="_blank">github.com/thisishusseinali</a></li>
  <li><strong>New Profiles:</strong> 
    <a href="https://www.kaggle.com/xwsein" target="_blank" style="margin-right:10px;">Kaggle</a> | 
    <a href="https://www.youtube.com/@xwsein" target="_blank" style="margin-left:10px; margin-right:10px;">YouTube</a> | 
    <a href="https://www.github.com/xwsein" target="_blank" style="margin-left:10px;">GitHub</a>
  </li>
</ul>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown('<p class="footer">© 2025 Hussein Ali</p>', unsafe_allow_html=True)

