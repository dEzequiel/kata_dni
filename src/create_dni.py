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
        self.set_healthy_number(self.check_dni_length and self.check_last_char_is_int)
        return self.get_healthy_number()

    def check_dni_length(self):
        if len(self.dni) == 9:
            return True
        return False

    # this method is for not passing a letter in the string
    def check_last_char_is_int(self):
        if self.dni[:-1].isdigit():
            return True
        return False
