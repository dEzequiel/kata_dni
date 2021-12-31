from random import choice, randint, randrange
from string import ascii_uppercase
from tabla_asignacion import TablaAsignacion


class DNI:
    def __init__(self, identity_numer=""):
        self.dni = identity_numer
        self.healthy_number = False
        self.healthy_letter = False
        self.table = TablaAsignacion()

    # methods to modify object instance
    def set_dni(self, identity_number):
        self.dni = identity_number

    def get_dni(self):
        return self.dni

    def set_healthy_number(self, status):
        self.healthy_number = status

    def get_healthy_number(self):
        return self.healthy_number

    def set_healthy_letter(self, status):
        self.healthy_letter = status

    def get_healthy_letter(self):
        return self.healthy_letter

    # checkers methods
    def check_dni(self):
        self.set_healthy_number(
            self.check_dni_length() and self.check_last_char_is_digit()
        )
        return self.get_healthy_number()

    def check_dni_length(self):
        return len(self.dni) == 9

    def check_last_char_is_digit(self):
        return self.dni[:-1].isdigit()

    def check_letter(self):
        if self.get_healthy_number():
            self.set_healthy_letter(
                self.get_alphabet_dni().isupper()
                and not self.get_alphabet_dni().isdigit()
                and self.check_valid_letter()
            )
            return self.get_healthy_letter()
        else:
            return False  # return get_tabble_letter

    def get_alphabet_dni(self):
        return self.dni[-1]

    def get_numerical_dni(self):
        return self.dni[:-1]

    def get_table_letter(self):
        if self.get_healthy_number():
            return self.table.calcular_letra(self.get_numerical_dni())
        else:
            return False

    def check_valid_letter(self):
        return (
            self.get_healthy_number()
            and self.get_alphabet_dni() == self.get_table_letter()
        )

    def check_cif(self):
        return self.check_dni() and self.check_letter()


if __name__ == "__main__":

    import math
    import random
    import string

    # person = DNI("42375166N")
    # print("DNI -->", person.get_dni())
    # person.check_dni()
    # print("Check status --> ", person.get_healthy_number())
    # # print("Letter status --> ", person.check_letter())
    # person2 = DNI("42375188B")  # B
    # print("DNI -->", person2.get_dni())
    # print("DNI NUMBER status -->", person2.check_dni())
    # print("DNI LETTER status --> ", person2.check_letter())
    # print("CIF STATUS -->", person2.check_cif())

casosTest = []
numeroCasos = 25

for i in range(1, numeroCasos + 1):
    caso = ""
    for j in range(1, 9):
        # random.randrange(start, stop[, step])
        # numeroAleatorio = random.randint(0, 9)
        # ASCII 48-57 = 0-9    65-90 = A-Z   58 = ":"
        # generamos un numero aleatorio entre 48 y 58
        caracterAscii = random.randrange(48, 58 + 1, 1)
        # convertimos el numero ASCII a caracter. chr() toma el argumento como codigo ASCII de un caracter
        caso = caso + chr(caracterAscii)
    # en la ultima posicion añado una letra A-Z
    caso = caso + chr(random.randrange(65, 90 + 1, 1))
    casosTest = casosTest + [caso]

print(casosTest)

for dni in casosTest:
    objeto = DNI(dni)
    print(objeto.get_dni())
    objeto.check_cif()
    print("dni --->", objeto.get_healthy_number())
    # print(objeto.calcularLetra())
    print("Letra --->", objeto.get_healthy_letter())
    print("La letra es", objeto.get_table_letter())
