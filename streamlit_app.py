import streamlit as st

st.set_page_config(page_title="Career Guidance Chatbot", page_icon="🎓")

st.title("🎓 Advanced Career Guidance Chatbot")

st.write("Get career recommendations based on your interests.")

name = st.text_input("Enter Your Name")

interest = st.selectbox(

    "Select Your Interest",

    [

        "Artificial Intelligence",

        "Data Science",

        "Web Development",

        "Cyber Security",

        "Cloud Computing",

        "Mobile App Development"

    ]

)

if st.button("Get Career Guidance"):

    if interest == "Artificial Intelligence":

        career = "AI Engineer"

        skills = "Python, Machine Learning, Deep Learning, NLP"

        salary = "₹8 - ₹20 LPA"

        roadmap = [

            "Learn Python",

            "Study Machine Learning",

            "Learn Deep Learning",

            "Build AI Projects",

            "Apply for AI Jobs"

        ]

    elif interest == "Data Science":

        career = "Data Scientist"

        skills = "Python, Pandas, Statistics, SQL"

        salary = "₹6 - ₹18 LPA"

        roadmap = [

            "Learn Python",

            "Learn Data Analysis",

            "Study Statistics",

            "Build Data Projects",

            "Apply for Data Science Roles"

        ]

    elif interest == "Web Development":

        career = "Full Stack Developer"

        skills = "HTML, CSS, JavaScript, React, Python"

        salary = "₹5 - ₹15 LPA"

        roadmap = [

            "Learn HTML & CSS",

            "Learn JavaScript",

            "Learn React",

            "Learn Backend Development",

            "Build Full Stack Projects"

        ]

    elif interest == "Cyber Security":

        career = "Cyber Security Analyst"

        skills = "Networking, Linux, Ethical Hacking"

        salary = "₹6 - ₹16 LPA"

        roadmap = [

            "Learn Networking",

            "Learn Linux",

            "Study Cyber Security",

            "Practice Ethical Hacking",

            "Earn Certifications"

        ]

    elif interest == "Cloud Computing":

        career = "Cloud Engineer"

        skills = "AWS, Azure, Linux, Docker"

        salary = "₹7 - ₹18 LPA"

        roadmap = [

            "Learn Linux",

            "Learn Cloud Basics",

            "Study AWS/Azure",

            "Learn Docker",

            "Work on Cloud Projects"

        ]

    else:

        career = "Mobile App Developer"

        skills = "Flutter, Dart, Firebase"

        salary = "₹5 - ₹14 LPA"

        roadmap = [

            "Learn Dart",

            "Learn Flutter",

            "Build Mobile Apps",

            "Use Firebase",

            "Publish Apps"

        ]

    st.success(f"Hello {name}!")

    st.subheader("🎯 Recommended Career")

    st.write(career)

    st.subheader("🛠 Required Skills")

    st.write(skills)

    st.subheader("💰 Average Salary")

    st.write(salary)

    st.subheader("📚 Career Roadmap")

    for step in roadmap:

        st.write("✅", step)

    st.subheader("🏆 Recommended Courses")

    st.write("• Python Programming")

    st.write("• Data Structures")

    st.write("• Database Management Systems")

    st.write("• Cloud Computing")

    st.write("• Artificial Intelligence")

    st.balloons()