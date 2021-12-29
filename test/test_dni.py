import unittest
from src.dni_cif import DNI


class DniClassTesting(unittest.TestCase):
    def test_DNI_object_creation(self):
        testing_value = DNI("123456789")
        self.assertIsInstance(testing_value, DNI)


if __name__ == "__main__":
    unittest.main()


# def check_dni():
#     objeto = DNI()
#     assert True == check_dni(objeto)
