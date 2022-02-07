
import random
from create_dni import DNI

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