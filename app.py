import streamlit as st

# Adding custom CSS
st.markdown(
    """
    <style>
    /* Customize the main header */
    .main-header {
        font-size: 36px;
        font-weight: bold;
        color: #FF5722; /* Orange color */
        text-align: center;
        margin: 10px 0;
    }

    /* Style for email and contact links */
    .contact-info {
        font-size: 16px;
        color: #FFC107; /* Yellow color */
        text-align: center;
        margin: 10px 0;
    }
    .contact-info a {
        color: #FF5722; /* Orange color */
        text-decoration: none;
    }

    /* Sidebar styling */
    .sidebar .sidebar-content {
        background-color: #FFF3E0; /* Light orange background */
        padding: 15px;
        border-radius: 10px;
    }

    /* Header for different sections */
    .section-header {
        font-size: 24px;
        color: #FF5722; /* Orange color */
        margin-top: 15px;
        margin-bottom: 5px;
    }

    /* List styling */
    .section-content {
        font-size: 16px;
        color: #FFFFFF; /* White color */
        margin: 5px 0;
        line-height: 1.5;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar for Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Skills", "Experience", "Certifications", "Education", "Contact"])

# Title and Header
st.markdown('<div class="main-header">Suraj K - QA Engineer</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="contact-info">suraj.kukkipady1@gmail.com | +91 866 015 3482 | <a '
    'href="https://www.linkedin.com/in/suraj-k/" target="_blank">LinkedIn</a></div>',
    unsafe_allow_html=True)

# Conditional rendering based on sidebar selection
if page == "Home":
    st.markdown('<div class="section-header">Welcome!</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-content">This is my portfolio website. Use the sidebar to navigate through different '
        'sections.</div>',
        unsafe_allow_html=True)

elif page == "Skills":
    st.markdown('<div class="section-header">Skills</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-content">Web Testing, API Testing, Mobile Testing, SQL, Communication</div>',
        unsafe_allow_html=True)

    st.markdown('<div class="section-header">Tools</div>', unsafe_allow_html=True)
    tools = """
    <div class="section-content">
    Jira, Postman, Strapi, Zephyr, Android Studio, Xcode, Metabase, Lambda Test, Selenium, Testim, Playwright, Zipy, Sentry
    </div>
    """
    st.markdown(tools, unsafe_allow_html=True)


elif page == "Experience":
    st.markdown('<div class="section-header">Professional Experience</div>', unsafe_allow_html=True)

    st.subheader("QA Engineer, ElevateHQ")
    st.write("**Jan 2023 – present | Remote, Bangalore**")
    st.markdown("""
    <div class="section-content">
    - Involved in UI and API testing.<br>
    - Planning tests, writing test cases, and executing them accordingly.<br>
    - Reporting bugs faced by customers and prioritizing the bugs.<br>
    - Monitoring tools like Zippy and Sentry for bugs and errors.
    </div>
    """, unsafe_allow_html=True)

    st.subheader("QA Engineer, Kommunicate")
    st.write("**Jun 2021 – Jan 2023 | Remote, Bangalore**")
    st.markdown("""
    <div class="section-content">
    - Involved in Functional, Integration, System, and User Acceptance testing.<br>
    - Worked on Web and Mobile applications.<br>
    - Writing test cases as per requirement and executing them accordingly.<br>
    - Verifying issues faced by users and filing bugs and improvements.
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Junior Administrator, Diya Systems")
    st.write("**Aug 2018 – Jul 2019 | Mangalore**")
    st.markdown("""
    <div class="section-content">
    - Worked as Customer Engagement Specialist for a client named Constant Contact.<br>
    - Involved in Testing Emails templates compatibility.
    </div>
    """, unsafe_allow_html=True)



elif page == "Certifications":
    st.markdown('<div class="section-header">Courses</div>', unsafe_allow_html=True)

    # Java, Python and Testing Certification
    abc_cert = 'https://drive.google.com/file/d/1cjWG6PA2fk2ANRi7gJbeayGB6VLfzvL9/view?usp=drive_link'
    st.markdown(
        f'''
        <div style="text-align:center; display: flex; align-items: center; justify-content: center; gap: 10px;">
            <div class="section-content">Java, Python and Testing, ABC for Technology Training</div>
            <a href="{abc_cert}" target="_blank"><button 
            style="background-color:#FF5722;color:white;border:none;padding:10px 20px;border-radius:5px;cursor:pointer;">
            View Certificate</button></a>
        </div>
        ''',
        unsafe_allow_html=True
    )

    # Career Essentials in Generative AI Certification
    linkedin_certificate_url = 'https://www.linkedin.com/learning/certificates/549eeefd3c17661de373018ea235ffd357fc16887c3751286bef340762035b96/'
    st.markdown(
        f'''
        <div style="text-align:center; display: flex; align-items: center; justify-content: center; gap: 10px;">
            <div class="section-content">Career Essentials in Generative AI by Microsoft and LinkedIn</div>
            <a href="{linkedin_certificate_url}" target="_blank"><button 
            style="background-color:#FF5722;color:white;border:none;padding:10px 20px;border-radius:5px;cursor:pointer;">
            View Certificate</button></a>
        </div>
        ''',
        unsafe_allow_html=True
    )




elif page == "Education":
    st.markdown('<div class="section-header">Education</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-content">Bachelor of Engineering (ECE), Srinivas Institute of Technology, Mangalore</div>',
        unsafe_allow_html=True)
    st.markdown('<div class="section-content">Aug 2014 – Aug 2018 | Mangalore</div>', unsafe_allow_html=True)

elif page == "Contact":
    st.markdown('<div class="section-header">Contact</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-content">You can reach me at:</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-content">- Email: suraj.kukkipady1@gmail.com</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-content">- Phone: +91 866 015 3482</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-content">- LinkedIn: <a href="https://www.linkedin.com/in/suraj-k/" '
        'target="_blank">Suraj K</a></div>',
        unsafe_allow_html=True)
