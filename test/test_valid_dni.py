from create_dni import DNI

######################################################################################
# VALID TEST CASES #

test_cases = [ 
				 "78484464T","72376173A","01817200Q","95882054E","63587725Q",
				 "26861694V","21616083Q","26868974Y","40135330P","89044648X",
				 "80117501Z","34168723S","76857238R","66714505S","66499420A"]

for dni in test_cases:
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
