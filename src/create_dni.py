from src.tabla_asignacion import TablaAsignacion


class DNI:
    def __init__(self, chain=""):
        self.dni = chain
        self.healthy_number = False
        self.healthy_letter = False
        self.table = TablaAsignacion()

    # methods to modify object instance
    def set_dni(self, chain):
        self.dni = chain

    def get_dni(self):
        return self.dni

    def set_healthy_number(self, number):
        self.healthy_number = number

    def get_healthy_number(self):
        return self.healthy_number

    def set_healthy_letter(self, letter):
        self.healthy_letter = letter

    def get_healthy_letter(self):
        return self.healthy_letter

    # checkers methods
    def check_dni(self):
        self.set_healthy_number(
            self.check_dni_length() and self.check_last_char_is_digit()
        )
        return self.get_healthy_number()

    def check_dni_length(self):
        if len(self.dni) == 9:
            return True
        else:
            return False

    def check_last_char_is_digit(self):
        if self.dni[:-1].isdigit():
            return True
        else:
            return False

    def check_letter(self):
        if self.set_healthy_letter(
            self.get_alphabet_dni().isupper()
            and not self.get_alphabet_dni().isdigit()
            and self.check_valid_letter()
        ):
            return self.get_healthy_letter()
        else:
            return False

    def get_alphabet_dni(self):
        return self.dni[-1]

    def get_table_letter(self):
        if self.get_healthy_number():
            return self.table.calcular_letra(self.dni[:-1])
        else:
            return False

    def check_valid_letter(self):
        if self.get_healthy_number:
            return self.get_alphabet_dni() == self.get_table_letter()
        else:
            return False

    def check_cif(self):
        pass


if __name__ == "__main__":
    pass
