import os
import re
import streamlit as st

from database.database import db_manager

# ---------------------------------------------------
# Configuration
# ---------------------------------------------------

PHOTO_FOLDER = "assets/profile_photos"
os.makedirs(PHOTO_FOLDER, exist_ok=True)


# ---------------------------------------------------
# Validation Functions
# ---------------------------------------------------

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)


def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10


# ---------------------------------------------------
# Student Profile Page
# ---------------------------------------------------

def profile_page():

    student = db_manager.get_student()

    # ----------------------------------------------
    # Load Existing Values
    # ----------------------------------------------

    name_value = student.name if student else ""
    email_value = student.email if student else ""
    phone_value = student.phone if student else ""
    college_value = student.college if student else ""

    department_value = student.department if student else "AI & DS"
    year_value = student.year if student else "1st Year"
    semester_value = student.semester if student else "1"
    career_value = student.career_goal if student else "AI Engineer"
    study_value = student.preferred_study_time if student else "Morning"
    learning_value = student.learning_style if student else "Videos"

    # ----------------------------------------------

    st.title("👤 Student Profile")
    st.caption("Complete your profile for a personalized AI experience")

    st.divider()

    # ----------------------------------------------
    # Existing Photo
    # ----------------------------------------------

    if (
        student
        and student.profile_image
        and os.path.exists(student.profile_image)
    ):
        st.image(student.profile_image, width=170)

    uploaded_photo = st.file_uploader(
        "📷 Upload Profile Photo (Optional)",
        type=["jpg", "jpeg", "png"]
    )

    st.divider()

    # ----------------------------------------------
    # Personal Information
    # ----------------------------------------------

    st.subheader("👤 Personal Information")

    col1, col2 = st.columns(2)

    with col1:

        name = st.text_input(
            "👤 Full Name *",
            value=name_value
        )

        email = st.text_input(
            "📧 Email Address *",
            value=email_value
        )

        phone = st.text_input(
            "📱 Mobile Number *",
            value=phone_value
        )

    with col2:

        college = st.text_input(
            "🏫 College / University *",
            value=college_value
        )

        year_list = [
            "1st Year",
            "2nd Year",
            "3rd Year",
            "4th Year",
            "Postgraduate"
        ]

        year = st.selectbox(
            "📚 Current Year *",
            year_list,
            index=year_list.index(year_value)
            if year_value in year_list else 0
        )

        semester_list = [
            "1","2","3","4","5","6","7","8"
        ]

        semester = st.selectbox(
            "🎓 Semester *",
            semester_list,
            index=semester_list.index(semester_value)
            if semester_value in semester_list else 0
        )

    st.divider()

    # ----------------------------------------------
    # Academic Information
    # ----------------------------------------------

    st.subheader("🎓 Academic Information")

    departments = [

        "AI & DS",
        "Artificial Intelligence",
        "Data Science",
        "Computer Science Engineering",
        "Information Technology",
        "Cyber Security",
        "Electronics & Communication Engineering",
        "Electrical & Electronics Engineering",
        "Mechanical Engineering",
        "Civil Engineering",
        "Biomedical Engineering",
        "Chemical Engineering",
        "Robotics & Automation",
        "Mechatronics",
        "Architecture",
        "Commerce",
        "Business Administration",
        "Medicine",
        "Law",
        "Science",
        "Arts",
        "Agriculture",
        "Pharmacy",
        "Diploma",
        "Other"

    ]

    department = st.selectbox(

        "🎓 Department *",

        departments,

        index=departments.index(department_value)
        if department_value in departments else 0

    )

    if department == "Other":

        department = st.text_input(
            "Enter Your Department *"
        )

    careers = [

        "AI Engineer",
        "Machine Learning Engineer",
        "Data Scientist",
        "Data Analyst",
        "Software Engineer",
        "Full Stack Developer",
        "Cloud Engineer",
        "Cyber Security Analyst",
        "DevOps Engineer",
        "Mobile App Developer",
        "Game Developer",
        "Research Scientist",
        "Entrepreneur",
        "Higher Studies",
        "Government Job",
        "Other"

    ]

    career_goal = st.selectbox(

        "🎯 Career Goal *",

        careers,

        index=careers.index(career_value)
        if career_value in careers else 0

    )

    if career_goal == "Other":

        career_goal = st.text_input(
            "Enter Career Goal *"
        )

    study_times = [

        "Early Morning",
        "Morning",
        "Afternoon",
        "Evening",
        "Night",
        "Late Night"

    ]

    study_time = st.selectbox(

        "⏰ Preferred Study Time *",

        study_times,

        index=study_times.index(study_value)
        if study_value in study_times else 0

    )

    learning_styles = [

        "Videos",
        "Reading Notes",
        "Practice Problems",
        "Projects",
        "Group Study",
        "Mixed"

    ]

    learning_style = st.selectbox(

        "📖 Preferred Learning Style *",

        learning_styles,

        index=learning_styles.index(learning_value)
        if learning_value in learning_styles else 0

    )

    st.divider()

    # ----------------------------------------------
    # Profile Completion
    # ----------------------------------------------

    required_fields = [

        name,
        email,
        phone,
        college,
        department,
        year,
        semester,
        career_goal,
        study_time,
        learning_style

    ]

    completed = sum(
        bool(str(field).strip())
        for field in required_fields
    )

    progress = completed / len(required_fields)

    st.subheader("📊 Profile Completion")

    st.progress(progress)

    st.write(f"**{int(progress*100)}% Completed**")

    st.divider()

    # ----------------------------------------------
    # Live Validation
    # ----------------------------------------------

    form_valid = True

    if len(name.strip()) < 3:

        st.warning("👤 Name should contain at least 3 characters.")

        form_valid = False

    if not is_valid_email(email):

        st.warning("📧 Please enter a valid email address.")

        form_valid = False

    if not is_valid_phone(phone):

        st.warning("📱 Mobile number must contain exactly 10 digits.")

        form_valid = False

    if not college.strip():

        form_valid = False

    if not department.strip():

        form_valid = False

    if not career_goal.strip():

        form_valid = False

    # ----------------------------------------------
    # Save Button
    # ----------------------------------------------

    if not form_valid:

        st.info(
            "🔒 Complete all required fields correctly to enable saving."
        )

    if st.button(

        "💾 Save / Update Profile",

        disabled=not form_valid,

        use_container_width=True

    ):

        image_path = student.profile_image if student else ""

        if uploaded_photo:

            image_path = os.path.join(
                PHOTO_FOLDER,
                "student_profile.png"
            )

            with open(image_path, "wb") as f:

                f.write(uploaded_photo.getbuffer())

        student_data = {

            "name": name,
            "email": email,
            "phone": phone,
            "college": college,
            "department": department,
            "year": year,
            "semester": semester,
            "career_goal": career_goal,
            "preferred_study_time": study_time,
            "learning_style": learning_style,
            "profile_image": image_path

        }

        db_manager.save_student(student_data)

        st.success("✅ Profile Updated Successfully!")

        st.balloons()

        st.rerun()