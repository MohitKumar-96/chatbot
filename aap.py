from datetime import datetime
import streamlit as st

# ==========================================
# PAGE CONFIGURATION & STYLING
# ==========================================
st.set_page_config(
    page_title="Marwadi University Chatbot",
    page_icon="🎓",
    layout="centered"
)

# ==========================================
# COLLEGE INFORMATION / DATES DATABASE
# ==========================================
COLLEGE_INFO = {
    "name": "Marwadi University",
    "location": "Rajkot, Gujarat, India",
    "accreditation": "NAAC A+ Grade Accredited Institution",
    "admission_start": "01 June 2026",
    "admission_last_date": "30 July 2026",
    "semester_start": "15 July 2026",
    "semester_end": "30 November 2026",
    "exam_start": "01 December 2026",
    "exam_end": "15 December 2026",
    "assignment_deadline": "25 November 2026",
    "scholarship_last_date": "31 August 2026",
    "event_date": "10 October 2026",
    "library_weekday": "8:30 AM - 8:00 PM (Monday to Saturday)",
    "library_weekend": "10:00 AM - 4:00 PM (Sunday & Public Holidays)",
    "college_open": "9:00 AM",
    "college_close": "4:30 PM",
    "hostel_application": "30 June 2026",
    "placement_start": "05 January 2027",
    "website": "www.marwadiuniversity.ac.in",
    "helpline": "+91 281 7123456"
}

TOPICS_LIST = [
    "My College", "Admission", "Courses", "Fees", "Timetable", "Attendance",
    "Exams", "Assignments", "Library Timings", "Hostel", "Scholarship",
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
        "- *Tell me about my college*\n"
        "- *How are you?*\n"
        "- *What are the library timings?*\n"
        "- *When is admission?*\n"
        "- *When are exams?*\n"
        "- *What is the assignment deadline?*"
    )

# ==========================================
# CHATBOT RESPONSE ENGINE
# ==========================================
def chatbot_response(user_input):
    """Processes user input and returns matching responses based on keyword triggers."""
    text = user_input.lower().strip()

    # Friendly Check-in / How are you
    if any(phrase in text for phrase in ["how are you", "how are u", "how r u", "how do you do"]):
        return (
            "😊 I'm doing great, thank you for asking!\n"
            "I'm ready to help you with any questions about **Marwadi University**. What would you like to know today?"
        )

    # Greetings
    elif any(word in text for word in ["hello", "hi", "hey", "hii", "good morning", "good afternoon", "good evening"]):
        return "Hello! 👋 Welcome to your **Marwadi University Assistant**.\nHow can I help you today?"

    # College Information (Marwadi University)
    elif any(word in text for word in ["my college", "about college", "marwadi", "marwadi university", "stored college", "stured college", "university details"]):
        return (
            f"🏛️ **ABOUT {COLLEGE_INFO['name'].upper()}**\n\n"
            f"- **Institution:** {COLLEGE_INFO['name']} ({COLLEGE_INFO['accreditation']})\n"
            f"- **Location:** {COLLEGE_INFO['location']}\n"
            f"- **Official Website:** [{COLLEGE_INFO['website']}](https://{COLLEGE_INFO['website']})\n"
            f"- **Helpline:** {COLLEGE_INFO['helpline']}\n\n"
            "Marwadi University offers diploma, undergraduate, postgraduate, and doctoral programs across Engineering, Management, Computer Applications, Pharmacy, Science, Law, and Architecture."
        )

    # Help
    elif "help" in text or "what can you do" in text:
        return generate_help_text()

    # Today / Date
    elif any(word in text for word in ["today", "date", "current date", "what day is today"]):
        return show_today()

    # Library Timings (With Days)
    elif any(word in text for word in ["library", "book", "books", "library time", "library timing", "library hours"]):
        return (
            "📖 **CENTRAL LIBRARY TIMINGS**\n\n"
            f"- 🗓️ **Monday to Saturday:** {COLLEGE_INFO['library_weekday']}\n"
            f"- 🗓️ **Sunday & Public Holidays:** {COLLEGE_INFO['library_weekend']}\n\n"
            "📌 *Note:* A valid Student ID card is mandatory for borrowing books and entering reading zones."
        )

    # Admission
    elif any(word in text for word in ["admission", "admissions", "enroll", "enrollment"]):
        return (
            "📌 **ADMISSION INFORMATION**\n\n"
            f"- **Admission starts:** {COLLEGE_INFO['admission_start']}\n"
            f"- **Last date to apply:** {COLLEGE_INFO['admission_last_date']}\n\n"
            "Required documents: 10th/12th marksheets, graduation degree (if applicable), ID proof, photographs, and entrance scorecards.\n"
            "Visit the Marwadi University Admission Cell for registration assistance."
        )

    # Courses
    elif any(word in text for word in ["course", "courses", "degree", "program", "programs", "branch", "department"]):
        return (
            "📚 **COURSES OFFERED**\n\n"
            "Marwadi University provides programs in:\n"
            "- **Technology:** B.Tech, M.Tech, Diploma Engineering\n"
            "- **Computer Applications:** BCA, MCA\n"
            "- **Management:** BBA, MBA\n"
            "- **Sciences & Pharmacy:** B.Sc, M.Sc, B.Pharm\n"
            "- **Other Streams:** Law, Architecture, Physiotherapy, Nursing"
        )

    # Fees
    elif any(word in text for word in ["fee", "fees", "tuition", "payment", "cost"]):
        return (
            "💳 **FEES INFORMATION**\n\n"
            "Fees cover tuition, laboratory, examination, and student activity charges.\n"
            "Semester fee deadlines are published on your Marwadi University Student Portal (ERP).\n"
            "Contact the Accounts Department for payment receipts or installment queries."
        )

    # Timetable
    elif any(word in text for word in ["timetable", "schedule", "class timing", "class schedule", "lecture"]):
        return (
            "🗓️ **CLASS TIMETABLE**\n\n"
            "Your weekly lecture schedule is updated on the Student Portal / ERP app.\n"
            f"- **Upcoming Semester Starts:** {COLLEGE_INFO['semester_start']}\n\n"
            "Check your department notice board for updates."
        )

    # Attendance
    elif any(word in text for word in ["attendance", "absent", "present", "attendance percentage"]):
        return (
            "📊 **ATTENDANCE POLICY**\n\n"
            "Students are required to maintain a minimum attendance threshold (usually 75%).\n"
            f"- **Semester Window:** {COLLEGE_INFO['semester_start']} to {COLLEGE_INFO['semester_end']}\n\n"
            "Track daily attendance directly via the Student ERP portal."
        )

    # Exams
    elif any(word in text for word in ["exam", "exams", "examination", "test", "semester exam"]):
        return (
            "📝 **EXAM SCHEDULE**\n\n"
            f"- **End-Semester Exams Start:** {COLLEGE_INFO['exam_start']}\n"
            f"- **Exams End:** {COLLEGE_INFO['exam_end']}\n\n"
            "Ensure you collect your examination hall ticket from the portal prior to exam week."
        )

    # Assignments
    elif any(word in text for word in ["assignment", "assignments", "project", "homework", "submission"]):
        return (
            "📑 **ASSIGNMENT SUBMISSION**\n\n"
            f"- **General Submission Deadline:** {COLLEGE_INFO['assignment_deadline']}\n\n"
            "Upload digital submissions to the LMS platform or hand over hard copies to your subject faculty."
        )

    # Hostel
    elif any(word in text for word in ["hostel", "room", "accommodation", "dormitory"]):
        return (
            "🏢 **HOSTEL ACCOMMODATION**\n\n"
            f"- **Application Deadline:** {COLLEGE_INFO['hostel_application']}\n\n"
            "Marwadi University offers AC and Non-AC hostel rooms with mess facilities, Wi-Fi, and 24/7 security."
        )

    # Scholarship
    elif any(word in text for word in ["scholarship", "financial aid", "financial assistance"]):
        return (
            "🎓 **SCHOLARSHIPS**\n\n"
            f"- **Application Deadline:** {COLLEGE_INFO['scholarship_last_date']}\n\n"
            "Merit-based, GATE, and category scholarships are available for eligible students."
        )

    # Placement
    elif any(word in text for word in ["placement", "placements", "job", "jobs", "career", "campus"]):
        return (
            "💼 **TRAINING & PLACEMENTS**\n\n"
            f"- **Placement Drives Begin:** {COLLEGE_INFO['placement_start']}\n\n"
            "The Marwadi University Placement Cell organizes campus drives, mock interviews, and skill workshops."
        )

    # Faculty
    elif any(word in text for word in ["faculty", "teacher", "teachers", "professor", "professors"]):
        return (
            "👨‍🏫 **FACULTY DIRECTORY**\n\n"
            "Faculty profiles and contact details are available on your department portal page.\n"
            "Consult your department secretary for office hours."
        )

    # Events
    elif any(word in text for word in ["event", "events", "festival", "fest", "function", "program"]):
        return (
            "🎉 **CAMPUS EVENTS**\n\n"
            f"- **Next Major Cultural Event:** {COLLEGE_INFO['event_date']}\n\n"
            "Includes tech fests, sports meets, cultural nights, and guest speaker sessions."
        )

    # Transport
    elif any(word in text for word in ["bus", "transport", "transportation"]):
        return (
            "🚌 **BUS TRANSPORT**\n\n"
            "Buses cover major routes across Rajkot city.\n"
            "Check the transport desk for route numbers, timings, and semester bus pass fees."
        )

    # ID Card
    elif any(word in text for word in ["id card", "identity card", "student card"]):
        return (
            "🪪 **STUDENT ID CARD**\n\n"
            "Mandatory for campus entry, library access, and exam attendance.\n"
            "Report lost cards to the Student Affairs desk immediately for re-issuance."
        )

    # Contact
    elif any(word in text for word in ["contact", "phone number", "email", "office", "contact number"]):
        return (
            "📞 **CONTACT DETAILS**\n\n"
            f"- **Campus:** {COLLEGE_INFO['name']}, Rajkot-Morbi Highway, Gujarat\n"
            f"- **Helpline:** {COLLEGE_INFO['helpline']}\n"
            f"- **Website:** [{COLLEGE_INFO['website']}](https://{COLLEGE_INFO['website']})"
        )

    # Timings
    elif any(word in text for word in ["college timing", "college timings", "working hours", "opening time", "college hours"]):
        return (
            "⏰ **COLLEGE TIMINGS**\n\n"
            f"- **College Opens:** {COLLEGE_INFO['college_open']}\n"
            f"- **College Closes:** {COLLEGE_INFO['college_close']}\n\n"
            "Administrative offices operate Monday through Saturday."
        )

    # Leave Application
    elif any(word in text for word in ["leave", "leave application", "holiday", "absence"]):
        return (
            "📝 **LEAVE APPLICATION**\n\n"
            "Submit leave requests via the Student Portal or hand a signed application to your Faculty Mentor."
        )

    # Semester
    elif any(word in text for word in ["semester", "semester start", "semester end"]):
        return (
            "📅 **SEMESTER TIMELINE**\n\n"
            f"- **Start Date:** {COLLEGE_INFO['semester_start']}\n"
            f"- **End Date:** {COLLEGE_INFO['semester_end']}\n"
            f"- **Exams:** {COLLEGE_INFO['exam_start']} to {COLLEGE_INFO['exam_end']}"
        )

    # Thanks
    elif any(word in text for word in ["thank you", "thanks", "thank"]):
        return "You're welcome! 😊 Let me know if you need any more details about Marwadi University."

    # Bye / Exit
    elif any(word in text for word in ["bye", "goodbye", "exit", "quit"]):
        return "Goodbye! 👋 Wishing you academic success at Marwadi University!"

    # Fallback
    else:
        return (
            "🤖 I don't quite understand that question yet.\n\n"
            "**Try asking queries like:**\n"
            "- *Tell me about my college*\n"
            "- *How are you?*\n"
            "- *What are the library timings?*\n"
            "- *When are my exams?*\n"
            "- *When is admission?*\n\n"
            "Or type **'help'** to see all supported topics."
        )

# ==========================================
# STREAMLIT UI LAYOUT & LOGIC
# ==========================================

st.title("🎓 Marwadi University Assistant")
st.caption("Ask questions about campus details, library hours, schedules, admissions, and exams.")

# Sidebar Navigation & Quick Access
with st.sidebar:
    st.header("⚙️ Chatbot Info")
    st.write("Welcome to the official student chatbot for **Marwadi University**.")
    
    st.divider()
    
    st.subheader("📌 Quick Topics")
    for topic in TOPICS_LIST:
        st.write(f"- {topic}")
    
    st.divider()
    if st.button("🗑️ Clear Chat History", type="secondary"):
        st.session_state.messages = []
        st.rerun()

# Initialize Chat Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hello! 👋 I am your **Marwadi University Assistant**.\n\n"
                "You can ask me about **my college**, **library timings**, admissions, exams, or type **'help'** to view all topics."
            )
        }
    ]

# Display Existing Chat Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input Processing
if prompt := st.chat_input("Ask a question (e.g., 'Tell me about my college')..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    bot_reply = chatbot_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
