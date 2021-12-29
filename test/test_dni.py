import unittest
from src.create_dni import DNI


class DniClassTesting(unittest.TestCase):
    def test_DNI_object_creation(self):
        testing_value = DNI("123456789")
        self.assertIsInstance(testing_value, DNI)

    def test_check_dni(self):
        value = DNI("123456789")
        self.assertTrue(value.check_dni(), False)

    def test_check_dni_length(self):
        value = DNI("123456789")
        self.assertTrue(value.check_dni_length(), True)

    def test_check_last_char_is_int(self):
        value = DNI("123456789")
        self.assertTrue(value.check_last_char_is_int(), True)
        value2 = DNI("123456789EE")
        self.assertFalse(value2.check_last_char_is_int(), False)


if __name__ == "__main__":
    unittest.main()
