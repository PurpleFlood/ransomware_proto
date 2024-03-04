from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
import os
from random import randint

def generate_aes_key():
    """
    Generates a random AES key.
    """
    return os.urandom(32)  # 256-bit key for AES-256

def generate_rsa_key_pair():
    """
    Generates an RSA key pair.
    """
    key = RSA.generate(2048)  # Generate a 2048-bit RSA key pair
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def encrypt_file_aes(input_file, output_file, aes_key):
    """
    Encrypts a file using AES-256.
    """
    cipher = AES.new(aes_key, AES.MODE_EAX)
    with open(input_file, 'rb') as f_in:
        data = f_in.read()
        ciphertext, tag = cipher.encrypt_and_digest(data)
    with open(output_file, 'wb') as f_out:
        f_out.write(cipher.nonce)
        f_out.write(tag)
        f_out.write(ciphertext)

def decrypt_file_aes(input_file, output_file, aes_key):
    """
    Decrypts a file using AES-256.
    """
    with open(input_file, 'rb') as f_in:
        nonce = f_in.read(16)
        tag = f_in.read(16)
        ciphertext = f_in.read()
        cipher = AES.new(aes_key, AES.MODE_EAX, nonce)
        data = cipher.decrypt_and_verify(ciphertext, tag)
    with open(output_file, 'wb') as f_out:
        f_out.write(data)

def list_files(target_folder):
    files_found = []

    # Parcourir tous les fichiers et sous-dossiers dans le dossier donné
    for root, dirs, files in os.walk(target_folder):
        for fichier in files:
            chemin_fichier = os.path.join(root, fichier)
            files_found.append(chemin_fichier)

    return files_found

def main():

    # Generate AES key
    aes_key = generate_aes_key()
    # Generate RSA key pair
    private_key, public_key = generate_rsa_key_pair()

    # Save RSA keys to files
    with open("./pem/private_key.pem", "wb") as f:
        f.write(private_key)
    with open("./pem/public_key.pem", "wb") as f:
        f.write(public_key)

    # Encrypt a file using AES
    # Replace with the path to your input file
    #encrypted_file = "./out/encrypted_file.bin"  # Replace with the path to your encrypted file
    #encrypt_file_aes(input_file, encrypted_file, aes_key)

    target_folder="./test/"
    files_list=list_files(target_folder)
    encrypted_files_list=[]
    for files_path in files_list:
        encrypt_file_aes(files_path, files_path, aes_key)
        print(files_path)

    # Decrypt the encrypted file using AES
    for files_path in files_list:
        # Replace with the desired output file path
        decrypt_file_aes(files_path, files_path, aes_key)

if __name__ == "__main__":
    main()
