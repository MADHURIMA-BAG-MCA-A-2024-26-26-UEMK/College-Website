# Raja Narendra Lal Khan Women's College (Autonomous), Medinipur
### Official Institutional Web Portal

A modern, responsive, and professional web application for **Raja Narendra Lal Khan Women's College (Autonomous)**, located at Gope Palace, Medinipur, Paschim Medinipur, West Bengal (Estd. 1957, NAAC Re-Accredited 'A' Grade, Affiliated to Vidyasagar University).

Built with **Python 3**, **Flask**, **Jinja2 Templates**, **HTML5**, **CSS3**, and **JavaScript**.

---

## 🌟 Key Features & Sections

1. **Top Information Bar**:
   - Dark navy-blue header (`#0B2D55`)
   - Direct helpline (`+91 9876543210`) and email (`info@college.ac.in`)
   - Interactive Student ERP Login & Faculty ERP Login modal popups
   - Online Admission direct link
   - Social channels (Facebook, Instagram, YouTube)

2. **Main Navigation Bar**:
   - Clean white navbar with college seal and typography
   - Active page indicator with blue underline animation
   - Multi-tier dropdown menus (About, Departments, Courses, Admission)
   - Fully responsive mobile navigation with hamburger toggle drawer

3. **Hero Carousel**:
   - Full-width hero banner with dark gradient overlay
   - 3 dynamic slides: *College Campus*, *Academic Excellence*, and *Student Activities*
   - Heading, subtitle, and CTA buttons (*Admission Enquiry*, *Learn More*)
   - Previous/Next arrows and pagination dots

4. **About Our College Section (3-Column Layout)**:
   - **Left Column**: Institutional profile and "Read More" button
   - **Center Column**: Gope Palace heritage campus image
   - **Right Column**: Notice Board card with colorful date badges, "NEW" tags, scrollable circulars, and "View All" link

5. **Courses Section**:
   - Light blue background (`#F4F9FD`)
   - 6 soft-pastel course cards in one row on desktop:
     1. **BCA** (Bachelor of Computer Applications)
     2. **MCA** (Master of Computer Applications)
     3. **B.Ed** (Bachelor of Education)
     4. **BA** (Bachelor of Arts)
     5. **B.Sc** (Bachelor of Science)
     6. **Other Courses** (UG/PG Diplomas & Skill Certifications)

6. **Quick Access Feature Cards**:
   - 4 large image-based feature cards with hover zoom and circular arrow buttons:
     1. **Our Faculty**
     2. **Gallery**
     3. **Contact Us**
     4. **Find Us**

7. **Dedicated Inner Pages**:
   - **About Page (`/about`)**: History, Vision & Mission, Principal's Message with Dr. Jayasree Laha's portrait, Infrastructure grid (Central Library, Computing Labs, DST-FIST Labs, Sports Stadium, Hostels, Eco-friendly campus).
   - **Departments Page (`/departments`)**: 8 academic faculties (Computer Science, Bengali, English, History, Geography, Education, Commerce, Science) with HOD details, faculty count, and facilities.
   - **Courses Page (`/courses`) & Detail (`/course/<name>`)**: Detailed syllabi, eligibility criteria, fees, seats, curriculum tags, career paths, and PDF syllabus download.
   - **Faculty Directory (`/faculty`)**: Faculty cards with photos, designations, qualifications, research interests, emails, and real-time department filter.
   - **Admission Portal (`/admission`)**: 4-step admission workflow, eligibility matrix, required documents checklist, important dates schedule, and online enquiry form with Flask POST validation.
   - **Notice Board (`/notices` & `/notice/<id>`)**: Category filters (Admission, Examination, Scholarship, Events, General), real-time live search, and printable official letterhead view.
   - **Media Gallery (`/gallery`)**: Category filter tabs, responsive image grid, hover zoom effects, and full-screen Lightbox modal with next/prev controls and captions.
   - **Contact Us (`/contact`)**: Campus address, phone EPABX, email, office hours, interactive Google Maps embed, and validated contact form.

8. **Footer**:
   - Dark navy-blue footer with college seal, quick links, copyright, and floating Back-to-Top button.

---

## 🛠️ Technology Stack

- **Backend**: Python 3.10+ & Flask 3.x
- **Template Engine**: Jinja2 (with reusable `base.html` inheritance)
- **Frontend**: HTML5, Vanilla CSS3 (Custom Design System with CSS variables), Vanilla JavaScript (ES6)
- **Icons**: Font Awesome 6
- **Typography**: Google Fonts (*Merriweather*, *Playfair Display*, *Inter*)

---

## 📁 Project Directory Structure

```text
college_website/
│
├── app.py                     # Flask application & routes backend
├── requirements.txt           # Project dependencies (Flask)
├── test_app.py                # Comprehensive automated unit test suite
├── README.md                  # Project documentation & instructions
│
├── templates/                 # Jinja2 HTML Templates
│   ├── base.html              # Master base layout with nav, header, footer, modals
│   ├── index.html             # Home page (Hero carousel, 3-col about, courses, quick access)
│   ├── about.html             # About college, history, vision, principal message, infra
│   ├── departments.html       # 8 Academic departments listing
│   ├── courses.html           # 6 Academic programs detailed listing
│   ├── course_detail.html     # Single course detail view (/course/<slug>)
│   ├── faculty.html           # Faculty directory with department filter
│   ├── admission.html         # Admission guidelines & online enquiry form
│   ├── notices.html           # Notice board with live search & category filter
│   ├── notice_detail.html     # Single notice official circular view (/notice/<id>)
│   ├── gallery.html           # Photo gallery with interactive Lightbox
│   ├── contact.html           # Contact info, enquiry form & Google Maps embed
│   ├── 404.html               # Custom 404 error page
│   └── 500.html               # Custom 500 server error page
│
└── static/
    ├── css/
    │   └── style.css          # Master stylesheet with academic design tokens
    │
    ├── js/
    │   └── script.js          # Interactive JavaScript (carousel, filters, lightbox, nav)
    │
    └── images/                # Photographic assets & institutional graphics
        ├── logo.png           # Official College Heraldic Crest
        ├── college-building.jpg# Gope Palace main academic building
        ├── campus.jpg         # Historic campus grounds & sports track
        ├── academic-excellence.jpg # Central library & digital reading zone
        ├── student-activities.jpg  # Convocation & student activities
        ├── principal.jpg      # Principal's official portrait
        ├── faculty.jpg        # Faculty conference team
        ├── faculty1.jpg       # Senior faculty portrait (female)
        ├── faculty2.jpg       # Senior faculty portrait (male)
        ├── gallery-lab.jpg    # Computer Science & Biotechnology lab
        ├── gallery-cultural.jpg# Classical dance cultural festival
        ├── gallery-sports.jpg # Annual athletics track event
        ├── gallery-seminar.jpg# Academic auditorium seminar
        ├── quick-faculty.jpg  # Quick link: Faculty
        ├── quick-gallery.jpg  # Quick link: Gallery
        ├── quick-contact.jpg  # Quick link: Contact Us
        └── quick-map.jpg      # Quick link: Find Us
```

---

## 🚀 Installation & Running the Application

### 1. Prerequisites
Ensure you have **Python 3.10+** installed on your system.

Check Python version:
```bash
python --version
```

### 2. Install Dependencies
Install Flask from `requirements.txt`:
```bash
python -m pip install -r requirements.txt
```
Or directly:
```bash
python -m pip install flask
```

### 3. Run the Flask Application
Start the development server:
```bash
python app.py
```

You will see output in the terminal:
```text
====================================================
 Raja Narendra Lal Khan Women's College Portal
 Medinipur, West Bengal - 721102 (Autonomous)
 Starting development server at http://127.0.0.1:5000/
====================================================
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

### 4. Open in Web Browser
Open your web browser and visit:
👉 **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

## 🧪 Running Automated Tests
A complete automated test suite is provided in `test_app.py`, validating all 15 routes, form submissions, and error handlers:
```bash
python test_app.py
```
Output:
```text
...............
----------------------------------------------------------------------
Ran 15 tests in 0.268s

OK
```

---

## 🖼️ Instructions for Customizing / Adding Images

All website images are located in the `static/images/` directory:

- **College Seal / Logo**:
  - Replace `static/images/logo.png` with your college crest. Transparent PNG or SVG recommended (approx. 200x200px or larger).
- **Hero Carousel Slides**:
  - `college-building.jpg` (Slide 1: Campus facade, 1920x1080px)
  - `academic-excellence.jpg` (Slide 2: Library/academics, 1920x1080px)
  - `student-activities.jpg` (Slide 3: Convocation/fest, 1920x1080px)
- **Principal's Portrait**:
  - Replace `static/images/principal.jpg` (4:3 aspect ratio portrait).
- **Faculty Photos**:
  - Add individual faculty photos into `static/images/` and update the `photo` path attribute in `FACULTY_DATA` within `app.py`.
- **Photo Gallery**:
  - Place your event, cultural, or sports photos in `static/images/` and add them to the `GALLERY_DATA` list in `app.py` with title, category, and caption.

---

## 🎨 Design System & Color Codes

| Token | Hex Code | Description |
| :--- | :--- | :--- |
| **Primary Navy** | `#0B2D55` | Top bar, footer, and academic headings |
| **Secondary Blue** | `#0056D2` | Active links, primary buttons, accents |
| **Accent Gold** | `#D4AF37` | Badges, awards, top bar hover highlights |
| **Light Background** | `#F4F9FD` | Section backgrounds, card light tint |
| **Card Pastel Blue** | `#EBF5FF` | BCA course card |
| **Card Pastel Purple** | `#F3E8FF` | MCA course card |
| **Card Pastel Green** | `#E8F8F0` | B.Ed course card |
| **Card Pastel Pink** | `#FDEEF5` | BA course card |
| **Card Pastel Yellow** | `#FEF8E7` | B.Sc course card |
| **Card Pastel Teal** | `#E6F7F7` | Other Courses card |

---

## 📄 License & Attribution
Designed for **Raja Narendra Lal Khan Women's College (Autonomous)**, Medinipur, West Bengal.
All rights reserved © 2026.
