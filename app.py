import streamlit as st

st.set_page_config(page_title="Student Career Counselling")

st.title(" Student Career Guidance System")

st.header("Enter CGPA for Past 4 Semesters")

sem1 = st.number_input(
    "Semester 1 CGPA",
    min_value=0.0,
    max_value=10.0,
    step=0.1
)

sem2 = st.number_input(
    "Semester 2 CGPA",
    min_value=0.0,
    max_value=10.0,
    step=0.1
)

sem3 = st.number_input(
    "Semester 3 CGPA",
    min_value=0.0,
    max_value=10.0,
    step=0.1
)

sem4 = st.number_input(
    "Semester 4 CGPA",
    min_value=0.0,
    max_value=10.0,
    step=0.1
)

average_cgpa = (sem1 + sem2 + sem3 + sem4) / 4

st.header("Student Feedback")

activities = st.slider(
    "How involved are you in student activities?",
    1,
    5,
    3
)

teachers = st.slider(
    "How do you feel about teachers' behavior?",
    1,
    5,
    3
)

classmates = st.slider(
    "How do you feel about fellow classmates interaction?",
    1,
    5,
    3
)

attendance = st.number_input(
    "Enter Attendance Percentage",
    min_value=0,
    max_value=100,
    value=75
)
st.header("PERSONAL REMARKS")

q1 = st.radio(
    "Do my teachers support and guide me when I need help?",
    ["Yes", "No"]
)

q2 = st.radio(
    "Am I learning useful things from my classes?",
    ["Yes", "No"]
)

q3 = st.radio(
    "Do I interact well with my classmates and friends?",
    ["Yes", "No"]
)

q4 = st.radio(
    "Will I miss the college environment and student life?",
    ["Yes", "No"]
)

q5 = st.radio(
    "Have I tried asking teachers or seniors for advice before deciding?",
    ["Yes", "No"]
)

q6 = st.radio(
    "Am I leaving because of one bad phase ?",
    ["Yes", "No"]
)

q7 = st.radio(
    "Can changing my study habits improve my situation?",
    ["Yes", "No"]
)

q8 = st.radio(
    "Am i actively ingonoring opportunities provided in college?",
    ["Yes", "No"]
)

q9 = st.radio(
    "Will dropping out affect my future job or higher studies?",
    ["Yes", "No"]
)

q10 = st.radio(
    "Do I have a clear and practical plan if I leave college?",
    ["Yes", "No"]
)

yes_count = 0

answers = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

for answer in answers:
    if answer == "Yes":
        yes_count += 1


average_feedback = (
    activities +
    teachers +
    classmates
) / 3

if st.button("Generate Career Suggestion"):

    st.success("Analysis Complete ")

    st.subheader(" Academic Summary")

    st.write(f"Average CGPA: {average_cgpa:.2f}")

    st.write(f"Attendance: {attendance}%")

    st.write(f"Student Activities: {'⭐' * activities}")

    st.write(f"Teacher Behavior Rating: {'⭐' * teachers}")

    st.write(f"Classmate Interaction Rating: {'⭐' * classmates}")

    st.write(f"Average Feedback Rating: {average_feedback:.1f}/5")

    st.divider()

    # GOOD CASE
    if attendance >= 75 and average_feedback > 3.5 and average_cgpa > 5 and yes_count > 7 :

        st.header(" Recommendation: Continue College")

        st.success(
            "Your engagement and attendance indicate that "
            "college is currently beneficial for you."
        )

        st.subheader("What You Should Focus On")

        st.markdown("""
### Side Projects
- Build real-world applications
- Create GitHub portfolio projects
- Participate in hackathons
- Learn modern technologies

###  Internships
- Apply for internships from 2nd/3rd year
- Build LinkedIn profile
- Network with seniors and alumni
- Focus on practical engineering skills

### Skill Building
- DSA and problem solving
- Web development
- AI/ML or Cybersecurity
- Open-source contributions

###  Career Strategy
- Use college mainly for:
  - networking
  - placements
  - internships
  - exposure

The real growth happens outside classrooms.
        """)

    # LOW ENGAGEMENT CASE
    else:

        st.header("⚠ Alternative Career Path Suggested")

        st.warning(
            "Your current academic engagement appears low."
        )

        st.subheader("Possible Alternative Engineering Careers")

        st.markdown("""
###  Freelancing
- Web development
- App development
- Graphic design
- Video editing
- UI/UX design

###  Cybersecurity
- Bug bounty hunting
- Ethical hacking
- Security testing

###  Tech Skill Careers
- AI tools automation
- Prompt engineering
- No-code development
- Cloud computing

###  Content + Engineering
- Tech YouTube channel
- Engineering tutorials
- Coding content creation

###  Startup Path
- Build small products
- Solve local business problems
- Create SaaS tools

###  Important Note
Dropping out should never be impulsive.

Only consider alternative paths if:
- you already have strong skills,
- clear direction,
- discipline,
- and financial planning.
        """)

    st.divider()

    st.subheader(" Final Verdict")

    if attendance >= 75 and average_feedback > 3.5 and average_cgpa > 5 and yes_count > 7 :
        st.success(
            "Stay in college and aggressively build skills outside academics."
        )
    else:
        st.warning(
            "Explore alternative engineering-focused career paths carefully."
        )