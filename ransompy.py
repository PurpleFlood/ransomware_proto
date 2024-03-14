from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_OAEP
import os
import zlib
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

def encrypt_file_rsa(input_file, output_file, pub_key_path):
    with open(pub_key_path, 'r') as f:
        pub_key = RSA.import_key(f.read())
    # Initialisation du chiffrement avec la clé publique
    cypher_rsa=PKCS1_OAEP.new(pub_key)

    # Lecture du contenu du fichier d'entré
    with open(input_file, 'rb') as f:
        data=f.read()
    data_encrypt=cypher_rsa.encrypt(data)

    with open(output_file, 'wb') as f:
        f.write(data_encrypt)

def decrypt_file_rsa(input_file, output_file, priv_key_path):
    with open(priv_key_path, 'r') as f:
        priv_key=RSA.import_key(f.read())
    cypher_rsa=PKCS1_OAEP.new(priv_key)
    with open(input_file, 'rb') as f:
        data=f.read()    
    data_decrypt=cypher_rsa.decrypt(data)
    
    with open(output_file, 'wb') as f:
        f.write(data_decrypt)

"""
def encrypt_file_aes(input_file, output_file, aes_key):
    
    # Encrypts a file using AES-256.
    
    cipher = AES.new(aes_key, AES.MODE_EAX)
    with open(input_file, 'rb') as f_in:
        data = f_in.read()
        ciphertext, tag = cipher.encrypt_and_digest(data)
    with open(output_file, 'wb') as f_out:
        f_out.write(cipher.nonce)
        f_out.write(tag)
        f_out.write(ciphertext)
"""
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
            file_path = os.path.join(root, fichier)
            files_found.append(file_path)

    return files_found

def main():

    # Generate AES key
    
    # Generate RSA key pair
    # Generate AES key
    aes_key = generate_aes_key()
        # Generate RSA key pair
    private_key, public_key = generate_rsa_key_pair()

    priv_key_path="./pem/private_key.pem"
    pub_key_path="./pem/public_key.pem"
    if os.path.isfile(priv_key_path) == False and os.path.isfile(pub_key_path) == False:
        # Save RSA keys to files
        with open(priv_key_path, "wb") as f:
            f.write(private_key)
        with open(pub_key_path, "wb") as f:
            f.write(public_key)

    # Encrypt a file using AES
    # Replace with the path to your input file
    #encrypted_file = "./out/encrypted_file.bin"  # Replace with the path to your encrypted file
    #encrypt_file_aes(input_file, encrypted_file, aes_key)

    target_folder="./test/"
    files_list=list_files(target_folder)
    print(files_list)
    for files in files_list:
        encrypt_file_rsa(files, files, pub_key_path)
    choice=int(input("Déchiffrer ? (1/0)"))
    if choice == 1:
        for files in files_list:
            decrypt_file_rsa(files, files, priv_key_path)
    elif choice == 0:
        return
    elif type(choice) == str:
        print("Choice must be int")
        choice=input("Déchiffrer ? (1/0)")
    else:
        while choice != 0 and choice != 1:
            choice=input("Déchiffrer ? (1/0)")


    
if __name__ == "__main__":
    main()
