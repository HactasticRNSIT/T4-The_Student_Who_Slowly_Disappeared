import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Student Career Guidance System",
    layout="wide"
)

# PREMIUM UI CSS
st.markdown("""
<style>

html, body, [class*="css"]  {
    font-family: 'Segoe UI', sans-serif;
    background-color: #020617;
    color: white;
}

.main {
    background: linear-gradient(
        135deg,
        #020617,
        #0f172a,
        #111827
    );
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
}

h1 {
    color: #ffffff;
    font-size: 3rem;
    font-weight: 700;
    text-align: center;
    margin-bottom: 20px;
}

h2, h3 {
    color: #e2e8f0;
    margin-top: 25px;
}

div[data-testid="stMetric"] {
    background-color: #111827;
    border: 1px solid #334155;
    padding: 15px;
    border-radius: 16px;
    box-shadow: 0px 0px 15px rgba(59,130,246,0.15);
}

.stButton > button {
    width: 100%;
    background: linear-gradient(
        90deg,
        #2563eb,
        #7c3aed
    );
    color: white;
    border: none;
    border-radius: 14px;
    height: 3.2em;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.02);
    box-shadow: 0px 0px 20px rgba(124,58,237,0.5);
}

.stNumberInput,
.stSlider,
.stRadio,
.stFileUploader {
    background-color: #111827;
    border-radius: 14px;
    padding: 12px;
    border: 1px solid #334155;
}

div.stAlert {
    border-radius: 14px;
}

[data-testid="stDataFrame"] {
    border-radius: 12px;
    overflow: hidden;
}

</style>
""", unsafe_allow_html=True)

st.title("AI Student Career Guidance System")

st.markdown("""
This intelligent system analyzes:
- Academic performance
- Attendance
- Student satisfaction
- Digital latency behavior
- Personal reflection

and generates personalized career guidance.
""")

# CGPA SECTION
st.header("Academic Performance")

num_semesters = st.number_input(
    "Enter Number of Semesters Attended",
    min_value=1,
    max_value=12,
    value=4,
    step=1
)

cgpas = []

st.subheader("Enter Semester-wise CGPA")

cols = st.columns(2)

for i in range(num_semesters):

    with cols[i % 2]:

        cgpa = st.number_input(
            f"Semester {i+1} CGPA",
            min_value=0.0,
            max_value=10.0,
            step=0.01,
            key=f"sem_{i}"
        )

        cgpas.append(cgpa)

average_cgpa = sum(cgpas) / len(cgpas)

# DIGITAL LATENCY FACTOR
st.header("Digital Latency Analysis")

st.markdown("""
Upload a CSV file containing:
- Day of Week
- Average Delay Before Starting Tasks
""")

uploaded_file = st.file_uploader(
    "Upload Digital Latency CSV",
    type=["csv"]
)

latency_score = 3

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Dataset")

    st.dataframe(df)

    st.subheader("Digital Latency Over Week")

    st.line_chart(
        df.set_index("Day")
    )

    latency_score = df["LatencyScore"].mean()

    st.metric(
        "Average Digital Latency Score",
        f"{latency_score:.2f}/5"
    )

    if latency_score >= 4:
        st.success(
            "Excellent task engagement behavior detected."
        )

    elif latency_score >= 3:
        st.info(
            "Moderate engagement behavior detected."
        )

    else:
        st.warning(
            "High task delay tendency detected."
        )

else:

    latency_score = st.slider(
        "How quickly do you start assignments after they are assigned?",
        1,
        5,
        3
    )

# FEEDBACK SECTION
st.header("Student Feedback")

activities = st.slider(
    "Student Activities Involvement",
    1,
    5,
    3
)

teachers = st.slider(
    "Teacher Support & Behavior",
    1,
    5,
    3
)

classmates = st.slider(
    "Classmate Interaction",
    1,
    5,
    3
)

attendance = st.number_input(
    "Attendance Percentage",
    min_value=0,
    max_value=100,
    value=75
)

average_feedback = (
    activities +
    teachers +
    classmates +
    latency_score
) / 4

# PERSONAL REMARKS
st.header("PERSONAL REMARKS")

questions = [
    "Do my teachers support and guide me when I need help?",
    "Am I learning useful things from my classes?",
    "Do I interact well with my classmates and friends?",
    "Will I miss the college environment and student life?",
    "Have I tried asking teachers or seniors for advice before deciding?",
    "Am I leaving because of one bad phase or a long-term problem?",
    "Can changing my study habits improve my situation?",
    "What opportunities in college am I ignoring right now?",
    "Will dropping out affect my future job or higher studies?",
    "Do I have a clear and practical plan if I leave college?"
]

yes_count = 0

for i, question in enumerate(questions):

    answer = st.radio(
        question,
        ["Yes", "No"],
        key=i
    )

    if answer == "Yes":
        yes_count += 1



# GENERATE RESULT
if st.button("Generate Career Recommendation"):

    st.success("Analysis Complete Successfully")

    st.header("Student Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Average CGPA", f"{average_cgpa:.2f}")
        st.metric("Attendance", f"{attendance}%")

    with col2:
        st.metric("Average Feedback", f"{average_feedback:.1f}/5")
        st.metric("Digital Latency Score", f"{latency_score:.1f}/5")

    st.divider()

    # GOOD CONDITION
    if attendance >= 75 and average_feedback > 3.5 and yes_count > 7 and average_cgpa > 5 :

        st.header("Recommendation: Continue College")

        st.success(
            "You show strong academic engagement and positive institutional alignment."
        )

        st.markdown("""
### Recommended Focus Areas

#### Side Projects
- Build real-world applications
- Create GitHub portfolio projects
- Participate in hackathons

#### Internships
- Apply for internships early
- Build LinkedIn profile
- Improve practical engineering skills

#### Career Growth
- Learn AI/ML, Cybersecurity, Web Development
- Improve communication and networking
- Explore startup ecosystems

#### Productivity
Your digital latency score indicates how quickly you act on academic tasks.
Lower delay usually correlates with higher professional discipline.
""")

    else:

        st.header("Alternative Engineering Career Paths")

        st.warning(
            "Current engagement levels suggest exploring broader engineering-related opportunities carefully."
        )

        st.markdown("""
### Recommended Alternatives

#### Freelancing
- Web Development
- UI/UX Design
- Video Editing
- Automation Services

#### Cybersecurity
- Bug Bounty Hunting
- Ethical Hacking
- Security Testing

#### Emerging Technology
- AI Tools
- Prompt Engineering
- No-Code Development
- SaaS Building

#### Tech Content Creation
- YouTube
- Coding Tutorials
- Technical Blogging

### Important Note
Alternative career paths require:
- Discipline
- Clear planning
- Strong practical skills
- Consistency
""")

    st.divider()

    st.subheader("Final Verdict")

    if attendance >= 75 and average_feedback > 3.5 and yes_count > 7:
        st.success("Stay in college and aggressively build skills outside academics.")
    else:
        st.warning("Carefully evaluate alternative engineering-focused career paths.")