from concrete import fhe

# Define the homomorphic function
def is_above_21(dob_year, dob_month, dob_day):
    current_year = 2024
    current_month = 7
    current_day = 9

    # Calculate age in years
    age = current_year - dob_year

    # Adjust age if the birthday has not occurred yet this year
    age = age - ((current_month * 31 + current_day) < (dob_month * 31 + dob_day))

    # Check if age is above or equal to 21
    is_above_21 = (age >= 21)
    
    # Return 1 if above 21, otherwise 0
    return is_above_21

# Create the compiler
compiler = fhe.Compiler(is_above_21, {"dob_year": "encrypted", "dob_month": "encrypted", "dob_day": "encrypted"})

# Example input set
inputset = [(2002, 12, 26), (2005,12,12)]

print("Compilation...")
circuit = compiler.compile(inputset)

print("Key generation...")
circuit.keygen()

print("Homomorphic evaluation...")
encrypted_dob_year, encrypted_dob_month, encrypted_dob_day = circuit.encrypt(2007, 12, 26)
encrypted_result = circuit.run(encrypted_dob_year, encrypted_dob_month, encrypted_dob_day)
result = circuit.decrypt(encrypted_result)

if result == 1:
    print("Bob Jones is above 21.")
else:
    print("Bob Jones is not above 21.")
