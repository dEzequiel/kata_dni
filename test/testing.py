import pytest
from dni_cif import DNI


def check_dni():
    objeto = DNI(123456789)
    assert True == check_dni(objeto)
