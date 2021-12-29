class DNI:
    def __init__(self, chain=""):
        self.dni = chain
        self.healthy_number = False
        self.healthy_letter = False

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
        if self.check_dni_length() and self.check_last_char_is_digit():
            return True
        else:
            return False

    def check_dni_length(self):
        if len(self.dni) == 9:
            return True
        else:
            return False

    # ToDo longitud del dni input
    # this method is for not passing a letter in middle of the string
    def check_last_char_is_digit(self):
        if self.dni[:-1].isdigit():
            return True
        else:
            return False


if __name__ == "__main__":
    pass
