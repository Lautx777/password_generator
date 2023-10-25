import shelve
from cryptography.fernet import Fernet

def decrypt_password(ciphertext, key):
    cipher_suite = Fernet(key)
    password = cipher_suite.decrypt(ciphertext).decode()
    return password

def main():
    # Encryption key that you know (could be the originally generated one)
    recovery_key = input("Enter the encryption key: ")
    recovery_key = recovery_key.encode()

    # Website for which you want to recover the password
    website_to_recover = input("Enter the name of the website: ")

    # Attempt to recover the password from Shelve
    with shelve.open("data/password") as passwords_db:
        encrypted_content = passwords_db.get(website_to_recover)

        
        if encrypted_content:
            recovered_password = decrypt_password(encrypted_content, recovery_key)

            if recovered_password:
                print(f"Password recovered for {website_to_recover}: {recovered_password}")
            else:
                print(f"No password found for {website_to_recover}.")
        else:
            print(f"No entry found for {website_to_recover} in the Shelve database.")

if __name__ == "__main__":
    main()

