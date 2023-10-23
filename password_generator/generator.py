from cryptography.fernet import Fernet
import string
import secrets

def encryptPassword(password, key):
    cipherSuite = Fernet(key)
    encrypted = cipherSuite.encrypt(password.encode())
    return encrypted

def generatePassword(length):
    asciiLetters = string.ascii_letters
    characters = asciiLetters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def savePassword(website, password, key):
    encryptedContent = encryptPassword(password, key)
    with open("new_passwords.txt", "a") as file:
        file.write(f"{website}: {encryptedContent.decode()}\n")
        print("Password encrypted and saved successfully.")

def main():
    encryptionKey = Fernet.generate_key()
    print("Save this encryption key in a secure place:")
    print(encryptionKey.decode())

    desiredLength = int(input("Enter the desired length for the password: "))
    website = input("For which social media or service is this password: ")

    generatedPassword = generatePassword(desiredLength)
    print(f"Password generated for {website}: {generatedPassword}")

    savePassword(website, generatedPassword, encryptionKey)

if __name__ == "__main__":
    main()