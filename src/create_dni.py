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

    import random

######################################################################################
# RANDOM TEST CASES #

number_cases = 5
list_cases = []

for i in range(1, number_cases + 1):
    case = ""  # Innitial dni, as you create your DNI object.
    for j in range(1, 9):
        number_sequence = random.randrange(48, 58 + 1, 1)  # returns a number
        case = case + chr(
            number_sequence
        )  # return the last returned number (line 118) into a ASCII char

    case = case + chr(
        random.randrange(65, 90 + 1, 1)
    )  # add random letter between A-Z to the final sequence
    list_cases = list_cases + [case]

print(list_cases)

for dni in list_cases:
    example = DNI(dni)
    print("DNI -->", example.get_dni())
    print("NUMBER STATUS -->", example.check_dni())
    if example.check_letter():
        print("LETTER STATUS -->", example.check_letter())
    else:
        print("EXPECTED LETTER -->", example.get_table_letter())
    print("CIF STATUS -->", example.check_cif())
    print("\n")

######################################################################################
