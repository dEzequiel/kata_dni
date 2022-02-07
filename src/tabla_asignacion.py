class Table:
    def __init__(self):
        self.positions = [number for number in range(0, 24)]
        self.letters = [
            "T",
            "R",
            "W",
            "A",
            "G",
            "M",
            "Y",
            "F",
            "P",
            "D",
            "X",
            "B",
            "N",
            "J",
            "Z",
            "S",
            "Q",
            "V",
            "H",
            "L",
            "C",
            "K",
            "E",
        ]
        self.table = dict(zip(self.positions, self.letters))

    def get_tabla_len(self):
        return len(self.table)

    def get_tabla_letter(self, position):
        try:
            return self.table[position]
        except:
            return "Letter position out of range"

    def calcular_letra(self, DNI):
        position = int(DNI) % self.get_tabla_len()
        return self.get_tabla_letter(position)

    def show_tabla(self):
        print(self.table)

