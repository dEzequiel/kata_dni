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


if __name__ == "__main__":

    objeto = DNI("12345766N")
    print(objeto.dni)
