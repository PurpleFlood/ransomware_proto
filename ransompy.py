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
    files=list_files("./test/")
    print(files)

    file=open(files[0], 'r')
    key=111000111101010101
    file.encode('ascii')
    print(XOR_encrypt.encrypt_XOR(key, file))
if __name__ == "__main__":
    main()
