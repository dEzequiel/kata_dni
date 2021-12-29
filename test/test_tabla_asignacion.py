## unit testing
import unittest
from src.tabla_asignacion import TablaAsignacion


class TablaAsignacionClassTesting(unittest.TestCase):
    def test_TABLE_object_creation(self):
        table = TablaAsignacion()
        self.assertIsInstance(table, TablaAsignacion)

    def test_get_tabla_length(self):
        table = TablaAsignacion()
        self.assertEqual(table.get_tabla_len(), 23)

    def test_get_table_letter(self):
        table = TablaAsignacion()
        self.assertTrue(table.get_tabla_letter(0), "T")
        self.assertTrue(table.get_tabla_letter(1), "R")
        self.assertTrue(table.get_tabla_letter(2), "W")

    def test_calculate_letter(self):
        table = TablaAsignacion()
        self.assertTrue(table.calcular_letra(78484464), "T")
        self.assertTrue(table.calcular_letra(72376173), "A")
        self.assertTrue(table.calcular_letra(95882054), "E")


if __name__ == "__main__":
    unittest.main()
