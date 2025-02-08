import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp_1 = Employee('John', 'Doe', 50000)
        self.emp_2 = Employee('Jane', 'Smith', 60000)

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'John.Doe@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

        self.emp_1.first = 'Jim'
        self.emp_2.first = 'Janet'

        self.assertEqual(self.emp_1.email, 'Jim.Doe@email.com')
        self.assertEqual(self.emp_2.email, 'Janet.Smith@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'John Doe')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

        self.emp_1.first = 'Jim'
        self.emp_2.first = 'Janet'

        self.assertEqual(self.emp_1.fullname, 'Jim Doe')
        self.assertEqual(self.emp_2.fullname, 'Janet Smith')

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    @patch('employee.requests.get')
    def test_monthly_schedule(self, mock_get):
        mock_get.return_value.ok = True
        mock_get.return_value.text = 'Success'

        schedule = self.emp_1.monthly_schedule('May')
        mock_get.assert_called_with('http://company.com/Doe/May')
        self.assertEqual(schedule, 'Success')

        mock_get.return_value.ok = False

        schedule = self.emp_2.monthly_schedule('June')
        mock_get.assert_called_with('http://company.com/Smith/June')
        self.assertEqual(schedule, 'Bad Response!')

if __name__ == '__main__':
    unittest.main()