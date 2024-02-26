import random
import string
import sys
#imported the random and string to get the better results
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
#join is used to join them irrespective of type
def main():
    try:
        num_passwords = int(input("Enter the number of passwords to generate: "))
        password_length = int(input("Enter the length of each password: "))
        if num_passwords <= 0 or password_length <= 0:
            print("Please enter valid positive integers for number of passwords and password length.")
            return
        for i in range(num_passwords):
            password = generate_password(password_length)
            print(f"Password {i + 1}: {password}")
    except ValueError:
        print("Please enter valid positive integers for number of passwords and password length.")

if __name__ == "__main__":
    main()