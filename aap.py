from datetime import datetime
import streamlit as st

# ==========================================
# PAGE CONFIGURATION & STYLING
# ==========================================
st.set_page_config(
    page_title="College Student Chatbot",
    page_icon="🎓",
    layout="centered"
)

# ==========================================
# COLLEGE INFORMATION / DATES DATABASE
# ==========================================
COLLEGE_INFO = {
    "admission_start": "01 June 2026",
    "admission_last_date": "30 July 2026",
    "semester_start": "15 July 2026",
    "semester_end": "30 November 2026",
    "exam_start": "01 December 2026",
    "exam_end": "15 December 2026",
    "assignment_deadline": "25 November 2026",
    "scholarship_last_date": "31 August 2026",
    "event_date": "10 October 2026",
    "library_open": "9:00 AM",
    "library_close": "5:00 PM",
    "college_open": "9:00 AM",
    "college_close": "4:00 PM",
    "hostel_application": "30 June 2026",
    "placement_start": "05 January 2027",
}

TOPICS_LIST = [
    "Admission", "Courses", "Fees", "Timetable", "Attendance",
    "Exams", "Assignments", "Library", "Hostel", "Scholarship",
    "Placement", "Faculty", "College Events", "Transport", "ID Card",
    "Contact Information", "College Timings", "Leave Application",
    "Semester", "Today / Date", "Greeting", "Exit"
]

# ==========================================
# HELPER FUNCTIONS
# ==========================================
def show_today():
    """Fetches system date and time and formats them into readable strings."""
    today = datetime.now()
    return (
        f"📅 Today is **{today.strftime('%d %B %Y')}**.\n"
        f"⏰ Current time: **{today.strftime('%I:%M %p')}**"
    )

def generate_help_text():
    """Returns structured markdown text for help/instructions."""
    topics_formatted = "\n".join([f"- {topic}" for topic in TOPICS_LIST])
    return (
        "### I can help you with these topics:\n"
        f"{topics_formatted}\n\n"
        "**Example questions:**\n"
        "- *When is admission?*\n"
        "- *When are exams?*\n"
        "- *What is the assignment deadline?*\n"
        "- *When does the semester start?*\n"
        "- *What are the library timings?*\n"
        "- *When is the scholarship deadline?*"
    )

# ==========================================
# CHATBOT RESPONSE ENGINE
# ==========================================
def chatbot_response(user_input):
    """Processes user input and returns matching responses based on keyword triggers."""
    text = user_input.lower().strip()

    # Greetings
    if any(word in text for word in ["hello", "hi", "hey", "hii", "good morning", "good afternoon"]):
        return "Hello! 👋\nHow can I help you with your college questions?"

    # Help
    elif "help" in text or "what can you do" in text:
        return generate_help_text()

    # Today / Date
    elif any(word in text for word in ["today", "date", "current date", "what day is today"]):
        return show_today()

    # Admission
    elif any(word in text for word in ["admission", "admissions", "enroll", "enrollment"]):
        return (
            "📌 **ADMISSION INFORMATION**\n\n"
            f"- **Admission starts:** {COLLEGE_INFO['admission_start']}\n"
            f"- **Last date to apply:** {COLLEGE_INFO['admission_last_date']}\n\n"
            "Required documents may include marksheets, ID proof, photographs, and application forms.\n"
            "Please check your college's official admission office for final requirements."
        )

    # Courses
    elif any(word in text for word in ["course", "courses", "degree", "program", "programs", "branch", "department"]):
        return (
            "📚 **COURSES**\n\n"
            "Common college programs include BCA, B.Tech, B.Sc, B.Com, BBA, BA, MCA, and MBA.\n"
            "The exact courses depend on your college curriculum.\n"
            "Course information is normally updated before the admission period."
        )

    # Fees
    elif any(word in text for word in ["fee", "fees", "tuition", "payment", "cost"]):
        return (
            "💳 **FEES INFORMATION**\n\n"
            "College fees may include tuition, examination, library, and other service charges.\n"
            "Fee payment dates are usually announced before each semester.\n"
            "Please check your student portal or accounts department for details."
        )

    # Timetable
    elif any(word in text for word in ["timetable", "schedule", "class timing", "class schedule", "lecture"]):
        return (
            "🗓️ **TIMETABLE**\n\n"
            "Your class timetable is available through the student portal or notice board.\n"
            f"- **Semester starts:** {COLLEGE_INFO['semester_start']}\n\n"
            "Check your department for your exact daily schedule."
        )

    # Attendance
    elif any(word in text for word in ["attendance", "absent", "present", "attendance percentage"]):
        return (
            "📊 **ATTENDANCE**\n\n"
            "Regularly check your attendance percentage via the student portal.\n"
            f"- **Current semester period:** {COLLEGE_INFO['semester_start']} to {COLLEGE_INFO['semester_end']}\n\n"
            "For shortages, reach out directly to your academic mentor or department head."
        )

    # Exams
    elif any(word in text for word in ["exam", "exams", "examination", "test", "semester exam"]):
        return (
            "📝 **EXAM INFORMATION**\n\n"
            f"- **Exam starts:** {COLLEGE_INFO['exam_start']}\n"
            f"- **Exam ends:** {COLLEGE_INFO['exam_end']}\n\n"
            "Remember to download your admit card beforehand. Final schedules are confirmed by the exam cell."
        )

    # Assignments
    elif any(word in text for word in ["assignment", "assignments", "project", "homework", "submission"]):
        return (
            "📑 **ASSIGNMENT INFORMATION**\n\n"
            f"- **Assignment deadline:** {COLLEGE_INFO['assignment_deadline']}\n\n"
            "Ensure you follow your professor's submission format guidelines and keep a backup copy."
        )

    # Library
    elif any(word in text for word in ["library", "book", "books"]):
        return (
            "📖 **LIBRARY**\n\n"
            f"- **Library opens:** {COLLEGE_INFO['library_open']}\n"
            f"- **Library closes:** {COLLEGE_INFO['library_close']}\n\n"
            "A valid student ID card is required for borrowing physical books."
        )

    # Hostel
    elif any(word in text for word in ["hostel", "room", "accommodation", "dormitory"]):
        return (
            "🏢 **HOSTEL**\n\n"
            f"- **Hostel application deadline:** {COLLEGE_INFO['hostel_application']}\n\n"
            "For room availability, fees, and house rules, contact the hostel administration office."
        )

    # Scholarship
    elif any(word in text for word in ["scholarship", "financial aid", "financial assistance"]):
        return (
            "🎓 **SCHOLARSHIP**\n\n"
            f"- **Application deadline:** {COLLEGE_INFO['scholarship_last_date']}\n\n"
            "Eligibility depends on merit, financial need, or category. Verify via the official scholarship portal."
        )

    # Placement
    elif any(word in text for word in ["placement", "placements", "job", "jobs", "career", "campus"]):
        return (
            "💼 **PLACEMENT**\n\n"
            f"- **Expected drive start:** {COLLEGE_INFO['placement_start']}\n\n"
            "The placement cell conducts training drives, interviews, and aptitude tests."
        )

    # Faculty
    elif any(word in text for word in ["faculty", "teacher", "teachers", "professor", "professors"]):
        return (
            "👨‍🏫 **FACULTY**\n\n"
            "Directory details are listed on the department site or board.\n"
            "Contact your department office for specific faculty office hours."
        )

    # Events
    elif any(word in text for word in ["event", "events", "festival", "fest", "function", "program"]):
        return (
            "🎉 **COLLEGE EVENTS**\n\n"
            f"- **Next major event:** {COLLEGE_INFO['event_date']}\n\n"
            "Includes cultural fests, technical symposia, sports, and workshops."
        )

    # Transport
    elif any(word in text for word in ["bus", "transport", "transportation"]):
        return (
            "🚌 **TRANSPORT**\n\n"
            "College buses operate across predefined regional routes.\n"
            "Contact the transport office for route updates, timings, and pass fees."
        )

    # ID Card
    elif any(word in text for word in ["id card", "identity card", "student card"]):
        return (
            "🪪 **ID CARD**\n\n"
            "Required for entry, exams, and library issuance.\n"
            "Report lost or damaged cards to the student affairs office immediately."
        )

    # Contact
    elif any(word in text for word in ["contact", "phone number", "email", "office", "contact number"]):
        return (
            "📞 **CONTACT INFORMATION**\n\n"
            "Official helpline numbers and administrative emails are hosted on the main college website."
        )

    # Timings
    elif any(word in text for word in ["college timing", "college timings", "working hours", "opening time", "college hours"]):
        return (
            "⏰ **COLLEGE TIMINGS**\n\n"
            f"- **Opening time:** {COLLEGE_INFO['college_open']}\n"
            f"- **Closing time:** {COLLEGE_INFO['college_close']}\n\n"
            "Timings may vary slightly during exams or official holidays."
        )

    # Leave Application
    elif any(word in text for word in ["leave", "leave application", "holiday", "absence"]):
        return (
            "📝 **LEAVE APPLICATION**\n\n"
            "Submit an application to your faculty mentor prior to planned absences.\n"
            "Medical leaves require valid doctor certificates upon return."
        )

    # Semester
    elif any(word in text for word in ["semester", "semester start", "semester end"]):
        return (
            "📅 **SEMESTER DATES**\n\n"
            f"- **Start date:** {COLLEGE_INFO['semester_start']}\n"
            f"- **End date:** {COLLEGE_INFO['semester_end']}\n"
            f"- **Exam window:** {COLLEGE_INFO['exam_start']} to {COLLEGE_INFO['exam_end']}"
        )

    # Thanks
    elif any(word in text for word in ["thank you", "thanks", "thank"]):
        return "You're welcome! 😊 Let me know if you need anything else."

    # Bye / Exit
    elif any(word in text for word in ["bye", "goodbye", "exit", "quit"]):
        return "Goodbye! 👋 Wishing you all the best with your studies!"

    # Fallback
    else:
        return (
            "🤖 I don't quite understand that question yet.\n\n"
            "**Try asking queries like:**\n"
            "- *When are my exams?*\n"
            "- *When is admission?*\n"
            "- *What is the assignment deadline?*\n"
            "- *When does the semester start?*\n"
            "- *What are the library timings?*\n\n"
            "Or type **'help'** to see all supported topics."
        )

# ==========================================
# STREAMLIT UI LAYOUT & LOGIC
# ==========================================

st.title("🎓 College Student Assistant")
st.caption("Ask questions about college schedules, admissions, exams, and guidelines.")

# Sidebar Navigation & Info
with st.sidebar:
    st.header("⚙️ Chatbot Info")
    st.write("Welcome! Use this assistant to get quick details on academic timelines and campus services.")
    
    st.divider()
    
    st.subheader("📌 Available Topics")
    for topic in TOPICS_LIST:
        st.write(f"- {topic}")
    
    if st.button("🗑️ Clear Chat History", type="secondary"):
        st.session_state.messages = []
        st.rerun()

# Initialize Chat Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hello! 👋 I am your College Assistant.\n\n"
                "I can help answer common questions regarding admissions, exams, deadlines, and timings.\n\n"
                "Type **'help'** for quick instructions or **'today'** to view the current date."
            )
        }
    ]

# Display Existing Chat Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input Processing
if prompt := st.chat_input("Ask a question (e.g., 'When are exams?')..."):
    # Render User Message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate & Render Bot Response
    bot_reply = chatbot_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)