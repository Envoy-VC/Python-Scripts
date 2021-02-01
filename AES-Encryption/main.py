from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(f'{filename}.enc', "wb") as file:
        file.write(encrypted_data)

def decrypt(filename, key):
    f = Fernet(key)
    with open(f'{filename}.enc', "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    with open(f'{filename}.dec', "wb") as file:
        file.write(decrypted_data)

write_key()

# AFTER RUNNING THE FILE FOR THE FIRST TIME COMMENT
# OUT THE ABOVE LINE TO PREVENT OVERWRITING OF TKE 'KEY.KEY'
# FILE

#LOADING THE KEY
key = load_key()

file = 'YOUR FILENAME HERE'

#THIS FUNCTION FOR ENCRYPTION
encrypt(file,key)

#THIS FUNCTION FOR DECRYPTION
decrypt(file,key)