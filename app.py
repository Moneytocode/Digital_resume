from pathlib import Path

import streamlit as st
from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir /"assets"/ "profile-pic4.png"


PAGE_TITLE = "Digital CV | Abhinav Dogra"
PAGE_ICON =":wave:"
NAME ="Abhinav Dogra"
DESCRIPTION= ""
EMAIL="abhinavdogra649@gmail.com"
SOCIAL_MEDIA ={
    "Linkedin": "http://www.linkedin.com/in/abhinav-dogra-22b44016a/",
    "GitHub": "https://github.com/Money2Code/"
}

PROJECTS ={
    "Mutual Funds DashBoad":"https://https://www.bajajamc.com/",
    "KPN - Cognizant":"https://https://www.kpn.com/"
    
}

st.set_page_config(page_title =PAGE_TITLE, page_icon=PAGE_ICON)

with open(css_file)  as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

col1, col2 = st.columns(2, gap = "small")
with col1:
    st.image(profile_pic, width =230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label =" Download Resume",
        data = PDFbyte,
        file_name= resume_file.name,
        mime = "application/octet-stream",

    )
    st.write("",EMAIL)


#----SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index , (platform , link ) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
- 3+ year of experience in python development and api 
- 2+ year of experience in cloud technology
- Good understanding in web development
- Excellent team-player and displaying strong sense of initiative on tasks

"""
)

st.write("#")
st.subheader("Hard skills")
st.write(
    """
- Creative thinking, Logical approach, Business communication, Aptitude, Team Working
- PYTHON SKILLS: RESTful API development |Python,|Django,|Regression, |Serialization,|JSON,|Python libraries,|Pytest,|Python PIL,|CSV,|PyPDF2,|Smtplib, |BeautifulSoup,|Python Data Stucture,|Requests,|SQL/MySQL/PostgreSQL 
- DEVELOPMENT TOOLS: Docker,|Jenkins,|VSCode,|GIT,|Postman,|Sonar,|Checkmarx,|Vault,|Sentry,|virtualenv/venv 
- OS SKILLS: Linux,|Vagrant ,|Bashscripting ,|VirtualMachine ,|Oracle virtual box 
- FRONTEND SKILLS: HTML,|CSS,|JavaScript

"""
)

st.write("#")
st.subheader("Work History")
st.write("---")

st.write("*", "**Software Engineer-II | Bajaj Markets   -------  Jan 2023 to Feb 2023** ")
st.write("""
- Bajaj Markets, an initiative by Bajaj Finserv, is a one-stop digital marketplace that offers 1300+ financial products in one place. The platform offers hundreds of financial products across loans, cards, insurance, investments, and payments.

        - Sprint Planning with Mutual fund team .
        - Development for the payment and stock-exchange portal.
        - Testing and Go-live planning .
        - Regression Testing and continuous integration.
        - Successfully deployed of mutual funds portal for live customers.
        - Critical approach towards the portal to develop API for stock holding.
        - Worked as team lead for backend developers.
         """)



st.write("*", "**Associate Software Developer | Cognizant  -----  Jun 2019 to Dec 2022** ")
st.write("""
- Cognizant (Nasdaq-100: CTSH) engineers modern businesses. We help our clients modernize technology, reimagine processes and transform experiences so they can stay ahead in our fast-changing world. Together, we’re improving everyday life.

        1. Network LEC B2B.(https://www.kpn.com/).
           - Developed Python partition which is whole isolated platform to consume the API,
             which was developed in java and connected to the partition through Python services
             model
           - Provided a whole new URL for fetching the data after serialization as well as the
             OOPs concept of Python.
           - Statistical analysis on data by performing sonar on the code using different Jenkins
             stages in order to run the Python code through these stages .
           - Improved the code coverage to 94 % by implementing the logic´s and by reducing
             the redundancy.
           - Achieved a most effective code for the platform in bitbucket.

        2. WHG( wyndham hospitality)
          - Developed python api for payload for hotel reservations.
          - Worked on a mock test with the pytest library.
          - Deployed a platform which collects data of new customers.
          - Successfully achieved less complexity and high code coverage.
         """)
st.write("*", "**CO-OP Software Developer Intern at Cognizant   -------  01/2019-04/2019** ")
st.write("""
              - Developed the Health management system in python.
              - Front End development using angular for portal.
              - Lead the team of four members during the project.
         """)
st.write("""
            - **PROMOTIONS**
              - Programmer analyst to software Developer
              - Software Developer to associate Developer
         """)

st.write("""
            - **COURSE & CERTIFICATION**
              - Python boot camp course Udemy 2020
              - Devops complete hands on by udemy 2023
              - FSE certified by Cognizant.
         """)

st.write("""
            - **INTERESTS & EXTRACURRICULAR ACTIVITIES**
              - Hacker rank certificate(https://www.hackerrank.com/certificates/f6579c8bc3de)
              - Clouds and Devops
              - Gym and fitness training.
              - Secured Second position at King kong naturals (Bodybuilding)
         """)

st.write("*", "**VOLUNTEER**")
st.write("""
          - **Childcare Program(outreach) | Cognizant,Mumbai    ----       07/2019-01/2020**
              - Helped students with basic concepts of Maths.
              - Helped them regarding money management for future
              - School cleaning with team members.
         
          - **Sales associate at General Nutrition company| Toronto  ---- 09/2023-present**
              - Working as a GNC nutrition coach.
              - Recommending best supplement regarding the goals.
              - Creating sales records and shipments.
         """)

