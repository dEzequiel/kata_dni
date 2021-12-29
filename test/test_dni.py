import unittest
from src.create_dni import DNI


class DniClassTesting(unittest.TestCase):
    def test_DNI_object_creation(self):
        testing_value = DNI("123456789")
        self.assertIsInstance(testing_value, DNI)

    def test_check_dni(self):
        value = DNI("123456789")
        self.assertTrue(value.check_dni())
        value2 = DNI("12345678")
        self.assertFalse(value2.check_dni())

    def test_check_dni_length(self):
        value = DNI("123456789")
        value2 = DNI("12345678")
        self.assertTrue(value.check_dni_length())
        self.assertFalse(value2.check_dni_length())

    def test_check_last_char_is_digit(self):
        value = DNI("12345678A")
        self.assertTrue(value.check_last_char_is_digit())
        value2 = DNI("12345678AA")
        self.assertFalse(value2.check_last_char_is_digit())
        value3 = DNI("123,e6789")
        self.assertFalse(value3.check_last_char_is_digit())


if __name__ == "__main__":
    unittest.main()
