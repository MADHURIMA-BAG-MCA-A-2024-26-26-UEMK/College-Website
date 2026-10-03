"""
Raja Narendra Lal Khan Women's College (Autonomous)
Medinipur, West Bengal - 721102
Flask Web Application Backend
"""

import os
import re
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, abort, jsonify

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "rnlk-womens-college-secret-key-2026")

# Global College Information
COLLEGE_INFO = {
    "name": "Raja Narendra Lal Khan Women's College",
    "status": "Autonomous College | NAAC Re-Accredited 'A' Grade (Cycle-3)",
    "affiliation": "Affiliated to Vidyasagar University",
    "location": "Gope Palace, Medinipur, Paschim Medinipur, West Bengal - 721102",
    "short_location": "Medinipur, West Bengal",
    "phone": "+91 9876543210",
    "alt_phone": "03222-275426",
    "email": "info@college.ac.in",
    "admission_email": "admissions@college.ac.in",
    "established": 1957,
    "principal": "Dr. Jayasree Laha",
    "motto": "Sa Vidya Ya Vimuktaye (Education That Liberates)",
    "current_year": datetime.now().year,
}

# Context Processor for Global Variables
@app.context_processor
def inject_college_info():
    return dict(college=COLLEGE_INFO)

# -------------------------------------------------------------
# Data Models / Repositories
# -------------------------------------------------------------

COURSES_DATA = {
    "bca": {
        "slug": "bca",
        "name": "BCA",
        "full_name": "Bachelor of Computer Applications",
        "level": "Undergraduate",
        "duration": "3 Years (6 Semesters)",
        "icon": "fa-solid fa-laptop-code",
        "color": "#E8F3FF",
        "border_color": "#0056D2",
        "badge_color": "#0056D2",
        "eligibility": "10+2 Higher Secondary in any stream with Mathematics / Computer Science / Statistics / Information Practices with minimum 50% aggregate marks.",
        "seats": 60,
        "fees_per_sem": "₹18,500",
        "overview": "The Bachelor of Computer Applications (BCA) is an undergraduate program designed to equip students with a solid foundation in computer applications, programming paradigms, modern software engineering, web architectures, and cloud computing principles.",
        "curriculum": [
            "Programming in C, C++, and Python",
            "Data Structures and Algorithms",
            "Database Management Systems & SQL",
            "Web Development (HTML5, CSS3, JavaScript, Full Stack)",
            "Computer Networks & Cyber Security",
            "Operating Systems & Linux Architecture",
            "Cloud Computing and Mobile App Development",
            "Major Industry Capstone Project"
        ],
        "career_paths": [
            "Software Developer / Engineer",
            "Full Stack Web Developer",
            "System & Database Administrator",
            "Cloud Support Associate",
            "UI/UX Designer",
            "IT Consultant"
        ]
    },
    "mca": {
        "slug": "mca",
        "name": "MCA",
        "full_name": "Master of Computer Applications",
        "level": "Postgraduate",
        "duration": "2 Years (4 Semesters)",
        "icon": "fa-solid fa-server",
        "color": "#F3E8FF",
        "border_color": "#7C3AED",
        "badge_color": "#7C3AED",
        "eligibility": "Passed BCA / Bachelor Degree in Computer Science Engineering or equivalent. Or passed B.Sc / B.Com / B.A. with Mathematics at 10+2 level or at Graduation Level with at least 50% marks. Valid JECA / Entrance rank.",
        "seats": 40,
        "fees_per_sem": "₹24,000",
        "overview": "The Master of Computer Applications (MCA) is a specialized postgraduate program tailored to nurture industry-ready software architects, data scientists, and advanced technology leaders through in-depth theoretical and laboratory training.",
        "curriculum": [
            "Advanced Data Structures & Algorithms",
            "Artificial Intelligence & Machine Learning",
            "Distributed Systems and Cloud Computing",
            "Advanced Java Enterprise & Spring Framework",
            "Data Science, Big Data & Analytics",
            "Cyber Security, Cryptography & Network Defense",
            "DevOps, CI/CD and Containerization",
            "Master's Thesis and 6-Month Industry Internship"
        ],
        "career_paths": [
            "Senior Software Architect",
            "Machine Learning Engineer / Data Scientist",
            "DevOps & Cloud Engineer",
            "Cyber Security Analyst",
            "Product Manager",
            "R&D Technology Specialist"
        ]
    },
    "bed": {
        "slug": "bed",
        "name": "B.Ed",
        "full_name": "Bachelor of Education",
        "level": "Professional / NCTE Approved",
        "duration": "2 Years (4 Semesters)",
        "icon": "fa-solid fa-chalkboard-user",
        "color": "#E8F8F0",
        "border_color": "#059669",
        "badge_color": "#059669",
        "eligibility": "Candidates with at least 50% marks either in the Bachelor's Degree and/or in the Master's Degree in Sciences/Social Sciences/Humanities. Recognized by NCTE.",
        "seats": 100,
        "fees_per_sem": "₹16,000",
        "overview": "NCTE recognized Bachelor of Education program aimed at cultivating visionary teachers, educational psychologists, and pedagogic innovators equipped with contemporary teaching methodologies and educational technologies.",
        "curriculum": [
            "Childhood and Growing Up",
            "Contemporary India and Education",
            "Learning and Teaching Methodologies",
            "Pedagogy of School Subjects (Bengali, English, History, Science, Math)",
            "Assessment for Learning & Evaluation",
            "Gender, School and Society",
            "ICT in Educational Instruction",
            "School Internship & Simulated Practice Teaching"
        ],
        "career_paths": [
            "Secondary & Higher Secondary Teacher",
            "Curriculum Developer & Instructional Designer",
            "Educational Counselor & Mentor",
            "Academic Administrator & Head of Institution",
            "EdTech Content Specialist"
        ]
    },
    "ba": {
        "slug": "ba",
        "name": "BA",
        "full_name": "Bachelor of Arts (Honours & Multidisciplinary)",
        "level": "Undergraduate",
        "duration": "4 Years (NEP 2020 Framework) / 3 Years Exit Option",
        "icon": "fa-solid fa-book-open-reader",
        "color": "#FDEEF5",
        "border_color": "#DB2777",
        "badge_color": "#DB2777",
        "eligibility": "10+2 Higher Secondary examination passed from any recognized Board/Council with minimum 45% aggregate and relevant subject cut-off.",
        "seats": 420,
        "fees_per_sem": "₹4,800",
        "overview": "A rich humanities curriculum offering major specializations in Bengali, English, History, Geography, Education, Political Science, Philosophy, and Music with interdisciplinary skill-enhancement courses under NEP guidelines.",
        "curriculum": [
            "Major Core Disciplines & Literature Analysis",
            "Minor Allied Electives across Humanities",
            "Ability Enhancement Courses (Language & Communication)",
            "Skill Enhancement Courses (Content Writing, Translation, GIS)",
            "Value Added Courses (Environmental Studies, Human Rights)",
            "Community Engagement & Fieldwork Survey",
            "Undergraduate Research Methodology & Dissertation"
        ],
        "career_paths": [
            "Civil Services & Public Administration (UPSC/WBCS)",
            "Journalism, Media & Mass Communication",
            "Content Strategy, Copywriting & Publishing",
            "Academic Research & University Lecturership",
            "NGO, Social Policy & Human Rights Advocacy"
        ]
    },
    "bsc": {
        "slug": "bsc",
        "name": "B.Sc",
        "full_name": "Bachelor of Science (Honours & Research)",
        "level": "Undergraduate",
        "duration": "4 Years (NEP 2020 Framework) / 3 Years Exit Option",
        "icon": "fa-solid fa-flask-vial",
        "color": "#FEF8E7",
        "border_color": "#D97706",
        "badge_color": "#D97706",
        "eligibility": "10+2 in Science stream with Physics, Chemistry, Mathematics / Biology with minimum 50% in aggregate and subject concerned.",
        "seats": 320,
        "fees_per_sem": "₹7,200",
        "overview": "Cutting-edge scientific education blending empirical laboratory investigation, computational simulations, and theoretical rigor across Physics, Chemistry, Mathematics, Botany, Zoology, Physiology, and Nutrition.",
        "curriculum": [
            "Disciplinary Core Foundations & Laboratory Practicals",
            "Instrumental Analytical Techniques & Spectroscopy",
            "Bio-informatics and Computational Modelling",
            "Biostatistics and Research Methodology",
            "Industrial Visits and Field Ecological Surveys",
            "Undergraduate Research Project & Laboratory Defense"
        ],
        "career_paths": [
            "Scientific Research Assistant & Laboratory Analyst",
            "Pharmaceutical & Biotechnology Specialist",
            "Environmental Consultant & Quality Controller",
            "Data Analyst & Quantitative Modeler",
            "Higher Academics (M.Sc, Integrated Ph.D.)"
        ]
    },
    "other-courses": {
        "slug": "other-courses",
        "name": "Other Courses",
        "full_name": "Postgraduate, Diploma & Skill Certification Courses",
        "level": "Undergraduate, PG & Vocational",
        "duration": "6 Months to 2 Years",
        "icon": "fa-solid fa-graduation-cap",
        "color": "#E6F7F7",
        "border_color": "#0D9488",
        "badge_color": "#0D9488",
        "eligibility": "Varies by diploma/certificate course. Open to 10+2 passed candidates and graduating students.",
        "seats": 180,
        "fees_per_sem": "₹3,500 - ₹9,500",
        "overview": "Vocational, diploma, and skill enhancement certifications including M.A./M.Sc. PG programs, Certificate in Spoken English, GIS & Remote Sensing, Food Processing & Preservation, and Computer Accounting with Tally & GST.",
        "curriculum": [
            "M.A. & M.Sc. Postgraduate Specialties",
            "Certificate in Remote Sensing & GIS Application",
            "Diploma in Digital Marketing & E-Commerce",
            "Certificate in Mushroom Cultivation & Food Preservation",
            "Computerized Financial Accounting with GST & Tally Prime",
            "Communicative English & Soft Skills for Corporate Placement"
        ],
        "career_paths": [
            "GIS Analyst & Spatial Mapping Technician",
            "Financial Accountant & Tax Filing Specialist",
            "Agri-business & Food Processing Entrepreneur",
            "Digital Marketer & Social Media Strategist",
            "Vocational Trainer & Educator"
        ]
    }
}

NOTICES_DATA = [
    {
        "id": 1,
        "title": "Admission Notice 2026-27: UG & PG Online Portal Open",
        "date_day": "15",
        "date_month": "OCT",
        "date_year": "2026",
        "category": "Admission",
        "is_new": True,
        "color_class": "badge-blue",
        "summary": "UG and PG online admission process started for academic session 2026-27. Candidates can submit applications through the centralized portal.",
        "content": "This is to notify all prospective students that the online admission portal for Undergraduate (BCA, BA, B.Sc) and Postgraduate (MCA, MA, M.Sc) courses for the academic session 2026-27 is now active. All applicants must submit their applications along with scanned copies of relevant mark sheets and caste/income certificates on or before November 10, 2026. Merit lists will be published strictly as per Vidyasagar University & State Government norms."
    },
    {
        "id": 2,
        "title": "Examination Notice: Even Semester Internal Assessment Schedule",
        "date_day": "10",
        "date_month": "OCT",
        "date_year": "2026",
        "category": "Examination",
        "is_new": True,
        "color_class": "badge-orange",
        "summary": "Internal assessment schedule published for 2nd, 4th and 6th semester students. Check departmental routine.",
        "content": "The Controller of Examinations announces that the mid-term continuous assessment and internal tests for 2nd, 4th, and 6th semester undergraduate and postgraduate students will commence from October 28, 2026. Detailed time tables and laboratory viva schedules have been uploaded to respective departmental notice boards. Attendance of all registered students is mandatory."
    },
    {
        "id": 3,
        "title": "Scholarship Notification: Swami Vivekananda Merit-cum-Means (SVMCM) 2026",
        "date_day": "05",
        "date_month": "OCT",
        "date_year": "2026",
        "category": "Scholarship",
        "is_new": True,
        "color_class": "badge-green",
        "summary": "Eligible students are requested to apply for SVMCM, Kanyashree (K3) and Aikyashree scholarships through West Bengal state portal.",
        "content": "Eligible meritorious students with family income less than ₹2.5 Lakhs per annum and holding minimum 60% marks in qualifying examinations are advised to apply online for Swami Vivekananda Merit-cum-Means (SVMCM) scholarship. Female postgraduate scholars should also submit Kanyashree Prakalpa (K3) renewal applications. Physical verification of hard copies will be conducted at the College Scholarship Desk between 11:00 AM and 3:00 PM."
    },
    {
        "id": 4,
        "title": "College Event: Annual Cultural Program & Mahisasuramardini Celebration",
        "date_day": "28",
        "date_month": "SEP",
        "date_year": "2026",
        "category": "Events",
        "is_new": False,
        "color_class": "badge-purple",
        "summary": "Annual cultural festival and Rabindra-Nazrul Sandhya will be celebrated in the college heritage auditorium.",
        "content": "The Cultural Committee cordially invites all faculty members, staff, and students to the Annual Cultural Celebration and Sharodotsav in the Gope Palace Heritage Auditorium on October 18, 2026. Auditions for music, classical dance, drama, and recitation will be held on October 08, 2026. Interested participants should register with the Students' Union representatives."
    },
    {
        "id": 5,
        "title": "National Seminar on 'Emerging Trends in AI and Cyber Security'",
        "date_day": "20",
        "date_month": "SEP",
        "date_year": "2026",
        "category": "General",
        "is_new": False,
        "color_class": "badge-cyan",
        "summary": "Two-day national seminar organized by Department of Computer Science & BCA with IEEE Student Branch.",
        "content": "The Department of Computer Science and BCA, in collaboration with the Internal Quality Assurance Cell (IQAC), will conduct a Two-Day UGC-sponsored National Seminar on 'Emerging Horizons in Artificial Intelligence, Cloud Infrastructure, and Cyber Defense'. Eminent keynote speakers from IIT Kharagpur, Jadavpur University, and leading tech companies will deliver plenary talks. Researchers can submit abstract papers by October 15, 2026."
    },
    {
        "id": 6,
        "title": "Annual Athletic Meet & Inter-Departmental Sports 2026",
        "date_day": "12",
        "date_month": "SEP",
        "date_year": "2026",
        "category": "Events",
        "is_new": False,
        "color_class": "badge-purple",
        "summary": "Track and field events, football, badminton and chess tournaments announced for all departments.",
        "content": "The Department of Physical Education is pleased to announce the Annual Inter-Departmental Sports Meet to be held on the college central stadium grounds from November 15 to 17, 2026. Events include 100m sprint, relay race, high jump, shot put, badminton singles & doubles, and chess championship. Entry forms are available at the sports counter."
    }
]

DEPARTMENTS_DATA = [
    {
        "id": "computer-science",
        "name": "Computer Science & Application",
        "icon": "fa-solid fa-laptop-code",
        "color": "#0056D2",
        "bg_color": "#E8F3FF",
        "established": 2001,
        "hod": "Dr. Subrata Sengupta, Ph.D. (IIT KGP)",
        "faculty_count": 8,
        "programs": "BCA, MCA, B.Sc Computer Science (Hons)",
        "desc": "Pioneering technological education with state-of-the-art computing laboratories, high-speed fiber-optic network, AI/ML development clusters, and dedicated career placement support.",
        "facilities": ["200+ High-Performance Workstations", "AI & Robotics Research Lab", "IoT & Embedded Systems Wing", "24/7 High Speed Internet"]
    },
    {
        "id": "bengali",
        "name": "Department of Bengali",
        "icon": "fa-solid fa-feather-pointed",
        "color": "#C026D3",
        "bg_color": "#FAE8FF",
        "established": 1957,
        "hod": "Dr. Anuradha Mukherjee, Ph.D.",
        "faculty_count": 6,
        "programs": "B.A. Bengali (Hons), M.A. Bengali, Ph.D.",
        "desc": "Preserving and celebrating the literary heritage of Bengal through critical textual analysis, folk literature research of Jungle Mahal, Rabindra studies, and creative writing workshops.",
        "facilities": ["Rare Bengali Manuscript Archive", "Departmental Seminar Library", "Literary Magazine 'Ananya'", "Folk Culture Research Wing"]
    },
    {
        "id": "english",
        "name": "Department of English",
        "icon": "fa-solid fa-book-journal-whills",
        "color": "#4338CA",
        "bg_color": "#E0E7FF",
        "established": 1957,
        "hod": "Prof. Sreerupa Ray, M.Phil, NET",
        "faculty_count": 6,
        "programs": "B.A. English (Hons), M.A. English",
        "desc": "Fostering communicative excellence, critical thinking, British, American, and Postcolonial literature, gender studies, film criticism, and digital humanities.",
        "facilities": ["Digital Language Learning Laboratory", "English Drama & Film Society", "Phonetics & Audio Lab", "International Journal Access"]
    },
    {
        "id": "history",
        "name": "Department of History",
        "icon": "fa-solid fa-landmark-dome",
        "color": "#B45309",
        "bg_color": "#FEF3C7",
        "established": 1957,
        "hod": "Dr. Malabika Dasgupta, Ph.D.",
        "faculty_count": 5,
        "programs": "B.A. History (Hons), M.A. History",
        "desc": "Unearthing historical narratives with specialized research on the freedom movement of Medinipur, Gope Palace royal archives, subaltern studies, and archaeological field surveys.",
        "facilities": ["Gope Heritage Archival Gallery", "Archaeological Artifacts Display", "Historical Map Collection", "Oral History Documentation Lab"]
    },
    {
        "id": "geography",
        "name": "Department of Geography",
        "icon": "fa-solid fa-earth-americas",
        "color": "#047857",
        "bg_color": "#D1FAE5",
        "established": 1968,
        "hod": "Dr. Prabal Kanti Mondal, Ph.D.",
        "faculty_count": 7,
        "programs": "B.Sc/B.A. Geography (Hons), M.Sc Geography",
        "desc": "Equipped with advanced GIS & Remote Sensing laboratories, soil testing analyzers, total station survey instruments, and periodic environmental fieldwork tours.",
        "facilities": ["ArcGIS & QGIS Computer Lab", "Cartography & Surveying Unit", "Soil & Water Quality Analysis Lab", "Meteorological Weather Station"]
    },
    {
        "id": "education",
        "name": "Department of Education & B.Ed",
        "icon": "fa-solid fa-graduation-cap",
        "color": "#BE185D",
        "bg_color": "#FCE7F3",
        "established": 1974,
        "hod": "Dr. Sharmistha Bhattacharya, Ph.D.",
        "faculty_count": 8,
        "programs": "B.A. Education (Hons), B.Ed (NCTE)",
        "desc": "NCTE-approved premier teacher training center combining educational psychology, inclusive education methods, classroom micro-teaching, and psychometric assessment.",
        "facilities": ["Psychological Testing Laboratory", "Smart Micro-Teaching Studio", "Curriculum Resource Centre", "Educational Technology Wing"]
    },
    {
        "id": "commerce",
        "name": "Department of Commerce",
        "icon": "fa-solid fa-chart-line",
        "color": "#0369A1",
        "bg_color": "#E0F2FE",
        "established": 1985,
        "hod": "Prof. Tapan Kumar Roy, M.Com, M.Phil",
        "faculty_count": 5,
        "programs": "B.Com (Hons in Accounting & Finance)",
        "desc": "Instilling financial acumen, taxation skills, corporate governance ethics, auditing expertise, and computer-assisted business analytics in aspiring women leaders.",
        "facilities": ["Financial Accounting Computer Lab", "Tally Prime & GST Certification", "Commerce Incubation Cell", "Stock Trading Simulation Portal"]
    },
    {
        "id": "science",
        "name": "Faculty of Pure & Applied Sciences",
        "icon": "fa-solid fa-atom",
        "color": "#15803D",
        "bg_color": "#DCFCE7",
        "established": 1960,
        "hod": "Dr. Aniruddha Mukherjee, Ph.D.",
        "faculty_count": 14,
        "programs": "B.Sc (Hons in Physics, Chemistry, Botany, Zoology, Nutrition)",
        "desc": "A vibrant scientific ecosystem with DST-FIST sponsored research laboratories, botanical conservatory, animal tissue culture lab, and interdisciplinary bio-chemical research.",
        "facilities": ["DST-FIST Central Instrumentation Lab", "Botanical Conservatory & Herbarium", "Spectrophotometry & Chromatography", "Zoological Museum & Lab"]
    }
]

FACULTY_DATA = [
    {
        "id": 1,
        "name": "Dr. Jayasree Laha",
        "designation": "Principal & Ex-Officio Head",
        "department": "Administration & Sciences",
        "qualification": "M.Sc., Ph.D., Post-Doctoral Fellow",
        "experience": "28+ Years in Higher Education",
        "email": "principal@college.ac.in",
        "photo": "images/principal.jpg",
        "research": "Plant Ecology, Higher Education Governance, Women's Empowerment"
    },
    {
        "id": 2,
        "name": "Dr. Subrata Sengupta",
        "designation": "Associate Professor & HOD",
        "department": "Computer Science & Application",
        "qualification": "M.Tech, Ph.D. (IIT Kharagpur)",
        "experience": "18 Years",
        "email": "s.sengupta@college.ac.in",
        "photo": "images/faculty2.jpg",
        "research": "Artificial Intelligence, Computer Vision, Distributed Cloud Architectures"
    },
    {
        "id": 3,
        "name": "Dr. Anuradha Mukherjee",
        "designation": "Associate Professor & HOD",
        "department": "Bengali",
        "qualification": "M.A., Ph.D., D.Litt. (Honorary)",
        "experience": "22 Years",
        "email": "a.mukherjee@college.ac.in",
        "photo": "images/faculty1.jpg",
        "research": "19th Century Bengali Literature, Women in Bengal Renaissance"
    },
    {
        "id": 4,
        "name": "Prof. Sreerupa Ray",
        "designation": "Assistant Professor & HOD",
        "department": "English",
        "qualification": "M.A. (CU), M.Phil, UGC-NET",
        "experience": "14 Years",
        "email": "s.ray@college.ac.in",
        "photo": "images/faculty1.jpg",
        "research": "Postcolonial Women Writers, Translation Studies, Cultural Theory"
    },
    {
        "id": 5,
        "name": "Dr. Malabika Dasgupta",
        "designation": "Associate Professor & HOD",
        "department": "History",
        "qualification": "M.A., Ph.D.",
        "experience": "20 Years",
        "email": "m.dasgupta@college.ac.in",
        "photo": "images/faculty1.jpg",
        "research": "Subaltern History of Southwest Bengal, Heritage & Archaeology"
    },
    {
        "id": 6,
        "name": "Dr. Prabal Kanti Mondal",
        "designation": "Associate Professor & HOD",
        "department": "Geography",
        "qualification": "M.Sc, Ph.D., PG Diploma in GIS & RS",
        "experience": "16 Years",
        "email": "pk.mondal@college.ac.in",
        "photo": "images/faculty2.jpg",
        "research": "Remote Sensing, Hydro-geomorphology, Watershed Management"
    },
    {
        "id": 7,
        "name": "Dr. Sharmistha Bhattacharya",
        "designation": "Associate Professor & HOD",
        "department": "Education & B.Ed",
        "qualification": "M.A. (Edn), M.Ed, Ph.D.",
        "experience": "19 Years",
        "email": "s.bhattacharya@college.ac.in",
        "photo": "images/faculty1.jpg",
        "research": "Educational Psychology, Inclusive Classroom Strategies, Teacher Pedagogy"
    },
    {
        "id": 8,
        "name": "Dr. Aniruddha Mukherjee",
        "designation": "Professor & Dean of Sciences",
        "department": "Faculty of Sciences",
        "qualification": "M.Sc (Gold Medalist), Ph.D., Post-Doc",
        "experience": "24 Years",
        "email": "dean.science@college.ac.in",
        "photo": "images/faculty2.jpg",
        "research": "Spectroscopy, Molecular Biology, Environmental Toxicology"
    }
]

GALLERY_DATA = [
    {
        "id": 1,
        "title": "Historic Gope Palace Main Academic Building",
        "category": "Campus",
        "image": "images/college-building.jpg",
        "caption": "The grand heritage facade of Raja Narendra Lal Khan Women's College nestled in tranquil greenery."
    },
    {
        "id": 2,
        "title": "Central University Library & Digital Reading Room",
        "category": "Students",
        "image": "images/academic-excellence.jpg",
        "caption": "Students engaged in collaborative research and digital learning in the central automated library."
    },
    {
        "id": 3,
        "title": "Annual Youth Convocation & Degree Felicitation",
        "category": "Events",
        "image": "images/student-activities.jpg",
        "caption": "Joyous graduating scholars celebrating academic triumph and degrees at the annual convocation."
    },
    {
        "id": 4,
        "title": "Computer Science & Advanced Biotech Research Labs",
        "category": "Seminars",
        "image": "images/gallery-lab.jpg",
        "caption": "Female researchers conducting cutting-edge computation, bioinformatics, and analytical experiments."
    },
    {
        "id": 5,
        "title": "Sharodotsav Rabindra Nritya Cultural Celebration",
        "category": "Cultural Programs",
        "image": "images/gallery-cultural.jpg",
        "caption": "Exquisite Bengali classical dance and Tagore tributes staged during the annual college cultural festival."
    },
    {
        "id": 6,
        "title": "Annual Athletic Championship on Olympic Running Track",
        "category": "Sports",
        "image": "images/gallery-sports.jpg",
        "caption": "Young female track athletes competing fiercely in sprint races at the college stadium."
    },
    {
        "id": 7,
        "title": "UGC Sponsored National Educational Seminar",
        "category": "Seminars",
        "image": "images/gallery-seminar.jpg",
        "caption": "Eminent academicians addressing researchers and faculty in the college auditorium."
    },
    {
        "id": 8,
        "title": "Scenic Aerial Panorama of Historic Gope Campus",
        "category": "Campus",
        "image": "images/campus.jpg",
        "caption": "Expansive 45-acre lush green grounds, playing fields, and heritage palace towers in Medinipur."
    }
]

# -------------------------------------------------------------
# Routes
# -------------------------------------------------------------

@app.route("/")
def index():
    # Pass 6 main courses, top notices, and quick access cards
    courses_list = list(COURSES_DATA.values())
    recent_notices = NOTICES_DATA[:4]
    return render_template(
        "index.html",
        courses=courses_list,
        notices=recent_notices,
        active_page="home"
    )

@app.route("/about")
def about():
    return render_template("about.html", active_page="about")

@app.route("/departments")
def departments():
    return render_template(
        "departments.html",
        departments=DEPARTMENTS_DATA,
        active_page="departments"
    )

@app.route("/courses")
def courses():
    return render_template(
        "courses.html",
        courses=COURSES_DATA,
        active_page="courses"
    )

@app.route("/course/<course_name>")
def course_detail(course_name):
    course_name_lower = course_name.lower().strip()
    course = COURSES_DATA.get(course_name_lower)
    if not course:
        # Check by full name or slug matching
        for key, val in COURSES_DATA.items():
            if key in course_name_lower or val["name"].lower() == course_name_lower:
                course = val
                break
    if not course:
        flash(f"Course '{course_name}' was not found. Here are all available academic programs.", "warning")
        return redirect(url_for("courses"))
    return render_template("course_detail.html", course=course, active_page="courses")

@app.route("/faculty")
def faculty():
    departments_set = sorted(list(set(f["department"] for f in FACULTY_DATA)))
    return render_template(
        "faculty.html",
        faculty_list=FACULTY_DATA,
        departments=departments_set,
        active_page="faculty"
    )

@app.route("/admission", methods=["GET", "POST"])
def admission():
    if request.method == "POST":
        full_name = request.form.get("full_name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        course = request.form.get("course", "").strip()
        dob = request.form.get("dob", "").strip()
        address = request.form.get("address", "").strip()
        message = request.form.get("message", "").strip()

        # Validation
        errors = []
        if not full_name:
            errors.append("Please provide your full legal name.")
        if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            errors.append("Please provide a valid email address.")
        if not phone or not re.match(r"^[0-9+\-\s]{10,15}$", phone):
            errors.append("Please enter a valid 10-digit mobile phone number.")
        if not course:
            errors.append("Please select your desired course.")

        if errors:
            for error in errors:
                flash(error, "danger")
            return render_template(
                "admission.html",
                courses=COURSES_DATA,
                active_page="admission",
                form_data=request.form
            )

        flash(
            f"Thank you, {full_name}! Your admission enquiry for {course.upper()} has been successfully registered. Application Reference #RNLK-{datetime.now().strftime('%Y%m%d%H%M')}. Our admissions counselor will contact you via email ({email}) and phone ({phone}) shortly.",
            "success"
        )
        return redirect(url_for("admission"))

    return render_template(
        "admission.html",
        courses=COURSES_DATA,
        active_page="admission",
        form_data={}
    )

@app.route("/notices")
def notices():
    category = request.args.get("category", "All")
    search_q = request.args.get("q", "").strip().lower()
    
    filtered = NOTICES_DATA
    if category and category != "All":
        filtered = [n for n in filtered if n["category"].lower() == category.lower()]
    if search_q:
        filtered = [n for n in filtered if search_q in n["title"].lower() or search_q in n["summary"].lower() or search_q in n["category"].lower()]
        
    categories = ["All", "Admission", "Examination", "Scholarship", "Events", "General"]
    return render_template(
        "notices.html",
        notices=filtered,
        all_notices=NOTICES_DATA,
        selected_category=category,
        search_query=search_q,
        categories=categories,
        active_page="notices"
    )

@app.route("/notice/<int:notice_id>")
def notice_detail(notice_id):
    notice = next((n for n in NOTICES_DATA if n["id"] == notice_id), None)
    if not notice:
        flash(f"Notice with ID #{notice_id} does not exist.", "warning")
        return redirect(url_for("notices"))
    related_notices = [n for n in NOTICES_DATA if n["id"] != notice_id][:3]
    return render_template(
        "notice_detail.html",
        notice=notice,
        related_notices=related_notices,
        active_page="notices"
    )

@app.route("/gallery")
def gallery():
    categories = ["All", "Campus", "Events", "Cultural Programs", "Sports", "Seminars", "Students"]
    return render_template(
        "gallery.html",
        gallery_items=GALLERY_DATA,
        categories=categories,
        active_page="gallery"
    )

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        subject = request.form.get("subject", "").strip()
        message = request.form.get("message", "").strip()

        errors = []
        if not name:
            errors.append("Please provide your name.")
        if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            errors.append("Please provide a valid email address.")
        if not message or len(message) < 5:
            errors.append("Please provide a meaningful message (at least 5 characters).")

        if errors:
            for error in errors:
                flash(error, "danger")
            return render_template(
                "contact.html",
                active_page="contact",
                form_data=request.form
            )

        flash(
            f"Dear {name}, thank you for contacting Raja Narendra Lal Khan Women's College! Your message regarding '{subject or 'General Inquiry'}' has been received. Our administrative office will reply within 1-2 business days.",
            "success"
        )
        return redirect(url_for("contact"))

    return render_template(
        "contact.html",
        active_page="contact",
        form_data={}
    )

# -------------------------------------------------------------
# Error Handlers
# -------------------------------------------------------------

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", active_page=""), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html", active_page=""), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("HOST", "0.0.0.0")
    print("====================================================")
    print(" Raja Narendra Lal Khan Women's College Portal")
    print(" Medinipur, West Bengal - 721102 (Autonomous)")
    print(f" Server running at http://{host}:{port}/")
    print("====================================================")
    app.run(host=host, port=port, debug=False)
