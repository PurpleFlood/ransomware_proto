import os
import XOR_encrypt
def list_files(target_folder):
    files_found = []

    # Parcourir tous les fichiers et sous-dossiers dans le dossier donné
    for root, dirs, files in os.walk(target_folder):
        for fichier in files:
            file_path = os.path.join(root, fichier)
            files_found.append(file_path)

    return files_found

def main():
    plain_text_file=open("./test/test.txt", "r")
    plain_text_file.read()
    

    key_file=open("./key.txt", "r")
    key_file.read()

    encrypted_text=""
    encrypted_text=XOR_encrypt.encrypt_XOR(plain_text_file, key_file)
    key_file.close()
    plain_text_file.close()

    print(f'Encrypted plaintext: {encrypted_text}')
if __name__ == "__main__":
    main()
