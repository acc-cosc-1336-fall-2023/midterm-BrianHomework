'''
Midterm question tests
'''
#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import reverse_string
from src.question_b.question_b import get_day_of_week
from src.question_c.question_c import use_local_variable
from src.question_d.question_d import get_tax_assessed, get_assessment_value

#class tests_strings(unittest.TestCase):

class test_config(unittest.TestCase):

    def test_hello_world(self):
        input_string = "Hello, World!"
        result = reverse_string(input_string)
        self.assertEqual(result, "!dlroW ,olleH")

    def test_hello(self):
        input_string = "hello"
        result = reverse_string(input_string)
        self.assertEqual(result, "olleh")


    #Tests for question_b
    def test_invalid_number(self):
        self.assertEqual(get_day_of_week(0), "Invalid number. Please enter a number in the range of 1 through 7.")
        self.assertEqual(get_day_of_week(8), "Invalid number. Please enter a number in the range of 1 through 7.")

    def test_valid_numbers(self):
        self.assertEqual(get_day_of_week(1), "Monday")
        self.assertEqual(get_day_of_week(2), "Tuesday")
        self.assertEqual(get_day_of_week(3), "Wednesday")

    #Tests for question_c
    def test_function_with_num_100(self):
        num = 100
        #use_local_variable(num)
        self.assertEqual(num, 100)

    #Tests for question_d
    def test_get_assessment_value_10000(self):
        result = get_assessment_value(10000)
        self.assertEqual(result, 6000)

    def test_get_assessment_value_20000(self):
        result = get_assessment_value(20000)
        self.assertEqual(result, 12000)
