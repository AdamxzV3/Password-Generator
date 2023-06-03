import random
import string

def generate_password(length=12, include_lowercase=True, include_uppercase=True, include_digits=True, include_symbols=True):
    lowercase_letters = string.ascii_lowercase if include_lowercase else ''
    uppercase_letters = string.ascii_uppercase if include_uppercase else ''
    digits = string.digits if include_digits else ''
    symbols = string.punctuation if include_symbols else ''
    
    characters = lowercase_letters + uppercase_letters + digits + symbols
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter the desired password length: "))
include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
include_digits = input("Include digits? (y/n): ").lower() == 'y'
include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

# Validate if at least one character set is selected
if not (include_lowercase or include_uppercase or include_digits or include_symbols):
    print("You cannot choose nothing as a password.")
else:
    password = generate_password(length, include_lowercase, include_uppercase, include_digits, include_symbols)
    print("Generated Password:", password)
