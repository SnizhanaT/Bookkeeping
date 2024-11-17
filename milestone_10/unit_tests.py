import unittest
from server import app


class TestEmployeeServer(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_birthdays_success(self):
        response = self.app.get('/birthdays?month=Apr&department=HR')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['total'], 2)
        self.assertEqual(data['employees'][0]['name'], 'John Doe')

    def test_get_anniversaries_success(self):
        response = self.app.get('/anniversaries?month=Apr&department=Engineering')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['total'], 1)
        self.assertEqual(data['employees'][0]['name'], 'Bob Johnson')

    def test_get_birthdays_invalid_month(self):
        response = self.app.get('/birthdays?month=XYZ&department=HR')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['total'], 0)

    def test_get_birthdays_invalid_department(self):
        response = self.app.get('/birthdays?month=Apr&department=NonExistent')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['total'], 0)

    def test_load_employees_corrupted_csv(self):
        with open('corrupted.csv', 'wb') as f:
            f.write(b"""id,name,age,department
        1,John Doe,30,Engineering
        2,Jane Smith,,HR
        3,Bob Johnson,25,
        4,Invalid Line Without Enough Columns
        5,Chris,,35,Marketing
        6,,40,Sales""")  # Create a mock corrupted CSV
            
        with open('corrupted.csv', 'rb') as f:
            response = self.app.post('/load_employees', data={'file': f})
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid or corrupted CSV", response.get_json()['error'])
    
