import unittest
from table import Table


class TableClassTesting(unittest.TestCase):
    def test_TABLE_object_creation(self):
        table = Table()
        self.assertIsInstance(table, Table)

    def test_get_tabla_length(self):
        table = Table()
        self.assertEqual(table.get_tabla_len(), 23)

    def test_get_table_letter(self):
        table = Table()
        self.assertTrue(table.get_tabla_letter(0), "T")
        self.assertTrue(table.get_tabla_letter(1), "R")
        self.assertTrue(table.get_tabla_letter(2), "W")

    def test_calculate_letter(self):
        table = Table()
        self.assertTrue(table.calcular_letra(78484464), "T")
        self.assertTrue(table.calcular_letra(72376173), "A")
        self.assertTrue(table.calcular_letra(95882054), "E")


if __name__ == "__main__":
    unittest.main()
