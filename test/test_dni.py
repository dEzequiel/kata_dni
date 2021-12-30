import unittest
from src.create_dni import DNI

# from src.tabla_asignacion import TablaAsignacion


class DniClassTesting(unittest.TestCase):
    def test_DNI_object_creation(self):
        testing_value = DNI("123456789")
        self.assertIsInstance(testing_value, DNI)

    def test_check_dni(self):
        value = DNI("123456789")
        self.assertTrue(value.check_dni())
        value2 = DNI("123,e678")
        self.assertFalse(value2.check_dni())
        value3 = DNI("12345678N")
        self.assertTrue(value3.check_dni())
        value4 = DNI("123")
        self.assertFalse(value4.check_dni())

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

    def test_get_alphabet_dni(self):
        value = DNI("95882054E")
        self.assertEqual(value.get_alphabet_dni(), "E")

    def test_get_numerical_dni(self):
        value = DNI("42375166N")
        self.assertEqual(value.get_numerical_dni(), "42375166")
        value2 = DNI("12345678P")
        self.assertNotEqual(value2.get_numerical_dni(), "12345678P")

    def test_calculate_letter(self):
        value = DNI("42375166N")
        value.set_healthy_number(True)
        self.assertTrue(value.get_table_letter())
        self.assertEqual(value.get_table_letter(), "N")
        self.assertNotEqual(value.get_table_letter(), "O")

    def test_check_valid_letter(self):
        value = DNI("42375166N")
        value2 = DNI("42375166O")
        value.set_healthy_number(True)
        self.assertTrue(value.check_valid_letter())
        self.assertFalse(value2.check_valid_letter())

    def test_check_letter(self):
        value = DNI("42375166N")
        value.set_healthy_number(True)
        self.assertTrue(value.check_letter())

    def test_check_cif(self):
        value = DNI("42375166N")
        value.set_healthy_number(True)
        value.set_healthy_letter(True)
        self.assertTrue(value.check_cif())


if __name__ == "__main__":
    unittest.main()
