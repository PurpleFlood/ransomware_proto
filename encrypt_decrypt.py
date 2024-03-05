from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

from Crypto.Hash import HMAC, SHA256
from Crypto.Random import get_random_bytes

## GENRATE CERTIFICAT PEM ##
def generate_rsa_key_pair():
    new_key=RSA.generate(2048)
    private_key=new_key.exportKey("PEM")
    public_key=new_key.publickey().exportKey("PEM")
    fd=open("./pem/private_key.pem", "wb")
    fd.write(private_key)
    fd.close()
    return private_key, public_key

## Encrypt / Decrypt Files ##
def encrypt_file_rsa(input_file, output_file, public_key_path):
    key=RSA.import_key(open(public_key_path).read)
    cipher=PKCS1_OAEP.new(key)
    ciphertext=cipher.encrypt(input_file)
    with open(output_file, 'wb') as f:
        f.write(ciphertext)


private_key, public_key=generate_rsa_key_pair()
with open("./pem/private_key.pem", 'wb') as f:
    f.write(private_key)
with open("./pem/public_key.pem", 'wb') as f:
    f.write(public_key)

with open("./test/test.txt", 'rb') as f:
    file=f.read()
print(file)
encrypt_file_rsa(file, "./encrypt.txt", "./pem/public_key.pem")
"""
key=RSA.import_key(open("./pem/public_key.pem").read())
cipher=PKCS1_OAEP.new(key)
ciphertext=cipher.encrypt(file)
with open("./encrypt.bin", 'wb') as f:
    f.write(ciphertext)
print(ciphertext)

key=RSA.import_key(open("./pem/private_key.pem").read())
cipher=PKCS1_OAEP.new(key)
plaintext=cipher.decrypt(ciphertext)
print(plaintext)

"""