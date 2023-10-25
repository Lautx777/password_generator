import shelve

def main():
    with shelve.open("passwords_db") as passwords_db:
        for key, value in passwords_db.items():
            print(f"Website: {key}, Encrypted Password: {value}")

if __name__ == "__main__":
    main()
