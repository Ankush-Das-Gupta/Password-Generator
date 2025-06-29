import random
import string
def generate_password():
    print("Welcome to the Python Password Generator!")
    try:
        length = int(input("Enter the desired password length: "))
        if length < 4:
            print("Password length should be at least 4 characters.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    all_chars = lowercase + uppercase + digits + symbols
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]
    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)
    final_password = ''.join(password)
    print(f"\nYour generated password is: {final_password}")
generate_password()
