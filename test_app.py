"""
Unit tests for Raja Narendra Lal Khan Women's College Flask Web Application
Verifies all routes, templates, form submissions, and static assets.
"""

import unittest
from app import app

class CollegeWebsiteTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Raja Narendra Lal Khan", response.data)
        self.assertIn(b"Women's College", response.data)
        self.assertIn(b"About Our College", response.data)
        self.assertIn(b"Notice Board", response.data)
        self.assertIn(b"Our Courses", response.data)
        self.assertIn(b"BCA", response.data)
        self.assertIn(b"MCA", response.data)
        self.assertIn(b"Our Faculty", response.data)

    def test_about_page(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About Our College", response.data)
        self.assertIn(b"Vision &amp; Mission", response.data)
        self.assertIn(b"Principal's Message", response.data)

    def test_departments_page(self):
        response = self.client.get('/departments')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Computer Science", response.data)
        self.assertIn(b"Bengali", response.data)
        self.assertIn(b"English", response.data)
        self.assertIn(b"History", response.data)

    def test_courses_page(self):
        response = self.client.get('/courses')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"BCA", response.data)
        self.assertIn(b"MCA", response.data)
        self.assertIn(b"B.Ed", response.data)

    def test_course_detail_routes(self):
        for course_name in ['bca', 'mca', 'bed', 'ba', 'bsc', 'other-courses']:
            response = self.client.get(f'/course/{course_name}')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"Curriculum", response.data)

    def test_faculty_page(self):
        response = self.client.get('/faculty')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Dr. Jayasree Laha", response.data)
        self.assertIn(b"Dr. Subrata Sengupta", response.data)

    def test_admission_page_get(self):
        response = self.client.get('/admission')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Online Admission Enquiry Form", response.data)

    def test_admission_form_post_success(self):
        response = self.client.post('/admission', data={
            'full_name': 'Ananya Ghosh',
            'email': 'ananya@example.com',
            'phone': '9876543210',
            'course': 'bca',
            'dob': '2005-04-12',
            'address': 'Medinipur Town',
            'message': 'Interested in BCA morning batch'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"successfully registered", response.data)

    def test_admission_form_post_invalid(self):
        response = self.client.post('/admission', data={
            'full_name': '',
            'email': 'invalid-email',
            'phone': '123',
            'course': ''
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Please provide your full legal name", response.data)

    def test_notices_page(self):
        response = self.client.get('/notices')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Official Notice Board", response.data)
        self.assertIn(b"Admission Notice", response.data)

    def test_notice_detail_page(self):
        response = self.client.get('/notice/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Admission Notice 2026-27", response.data)

    def test_gallery_page(self):
        response = self.client.get('/gallery')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Life at Gope Palace Campus", response.data)
        self.assertIn(b"lightboxModal", response.data)

    def test_contact_page_get(self):
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Get in Touch With Us", response.data)
        self.assertIn(b"Gope Palace", response.data)

    def test_contact_form_post_success(self):
        response = self.client.post('/contact', data={
            'name': 'Priyanka Sen',
            'email': 'priyanka@example.com',
            'phone': '9876501234',
            'subject': 'Hostel Accommodation Query',
            'message': 'Please provide details on hostel admission rules for first year students.'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"thank you for contacting", response.data)

    def test_404_page(self):
        response = self.client.get('/nonexistent-page-url')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"Page Not Found", response.data)

if __name__ == '__main__':
    unittest.main()
