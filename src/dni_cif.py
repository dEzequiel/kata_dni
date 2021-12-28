class DNI:
    def __init__(self, chain=""):
        self.dni = chain
        self.healthy_number = False
        self.healthy_letter = False
        # ToDo: tabla de asignación.

        # ToDo: investigar sobre interfaces en py.

        # Interfaz publica porque lo puedes usar fuera de la clase, para crear el objeto?
        # set methods
        def set_dni(self, chain):
            self.dni = chain

        def set_healthy_number(self, value):
            self.healthy_number = value

        def set_healthy_letter(self, value):
            self.healthy_letter = value

        # get metheods
        def get_dni(self):
            return self.dni

        def get_healthy_number(self):
            return self.healthy_number

        def get_healthy_letter(self):
            return self.healthy_letter

        # check methods (class variables are boolean)
        def check_dni(self):
            if set_healthy_number(self.check_length() and self.check_last_int()):
                return get_healthy_number()

        # private methods
        def check_length(self):
            if len(self.dni) == 9:
                return True
            return False

        # tiene que ser digito o char?
        def check_last_int(self):
            if self.dni[:-1].isdigit():
                return True
            return False
