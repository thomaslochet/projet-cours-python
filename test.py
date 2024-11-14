import unittest
from health_utils import calculate_bmi, calculate_bmr
from app import app

class TestHealthCalculator(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_calculate_bmi(self):
        """Test BMI calculation"""
        self.assertAlmostEqual(calculate_bmi(1.75, 70), 22.86, places=2)
        self.assertAlmostEqual(calculate_bmi(1.80, 80), 24.69, places=2)
        
        with self.assertRaises(ValueError):
            calculate_bmi(0, 70)
        with self.assertRaises(ValueError):
            calculate_bmi(1.75, -70)

    def test_calculate_bmr(self):
        """Test BMR calculation"""
        self.assertAlmostEqual(
            calculate_bmr(175, 70, 25, 'male'),
            1724.05,
            places=2
        )
        self.assertAlmostEqual(
            calculate_bmr(160, 60, 30, 'female'),
            1368.19,
            places=2
        )
        
        # Test invalid inputs
        with self.assertRaises(ValueError):
            calculate_bmr(0, 70, 25, 'male')
        with self.assertRaises(ValueError):
            calculate_bmr(175, -70, 25, 'male')
        with self.assertRaises(ValueError):
            calculate_bmr(175, 70, -25, 'male')
        with self.assertRaises(ValueError):
            calculate_bmr(175, 70, 25, 'invalid')

    def test_bmi_endpoint(self):
        """Test BMI API endpoint"""
        response = self.app.post('/bmi', json={
            'height': 1.75,
            'weight': 70
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertAlmostEqual(data['bmi'], 22.86, places=2)
        self.assertEqual(data['category'], 'Normal weight')

    def test_bmr_endpoint(self):
        """Test BMR API endpoint"""
        response = self.app.post('/bmr', json={
            'height': 175,
            'weight': 70,
            'age': 25,
            'gender': 'male'
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertAlmostEqual(data['bmr'], 1724.05, places=2)

if __name__ == '__main__':
    unittest.main()