import shelve
from cryptography.fernet import Fernet
import string
import secrets

def encrypt_password(password, key):
    cipher_suite = Fernet(key)
    encrypted = cipher_suite.encrypt(password.encode())
    return encrypted 

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password 

def save_password(website, password, key, shelve_file):
    encrypted_content = encrypt_password(password, key)
    with shelve.open(shelve_file) as passwords_db:
        passwords_db[website] = encrypted_content
        print("Password encrypted and saved successfully.")

def main():
    encryption_key = Fernet.generate_key()
    print("Save this encryption key in a secure place:")
    print(encryption_key.decode())

    desired_length = int(input("Enter the desired length for the password: "))
    website = input("For which social media or service is this password: ")
    shelve_file = "data/password"  # Change the filename as needed

    generated_password = generate_password(desired_length)
    print(f"Password generated for {website}: {generated_password}")

    save_password(website, generated_password, encryption_key, shelve_file)

if __name__ == "__main__":
    main()