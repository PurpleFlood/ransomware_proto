from Crypto.Cipher import AES
import os
import key_pair_gen
import list_dir
def generate_aes_key():
    """
    Generates a random AES key.
    """
    return os.urandom(32)  # 256-bit key for AES-256

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

def main():
    i=0
    for i in range(len(table_dir)-1):
        input_file=table_dir[i]
        encrypted_file = "encrypted_file",i,".bin"
        encrypt_file_aes(input_file, encrypted_file, public_key)
        i=i+1
    # Encrypt a file using AES
    input_file = "list_dir.py"  # Replace with the path to your input file
    encrypted_file = "encrypted_file.bin"  # Replace with the path to your encrypted file
    encrypt_file_aes(input_file, encrypted_file, public_key)

    # Decrypt the encrypted file using AES
    decrypted_file = "decrypted_file.txt"  # Replace with the desired output file path
    decrypt_file_aes(encrypted_file, decrypted_file, private_key)

    print("File encrypted and decrypted successfully.")

if __name__ == "__main__":
    main()
