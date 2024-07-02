


## encrypt function

def encrypt_XOR(text, key):

    encrypted_text=""

    for i in range(len(text)):
        encrypted_text+=chr(ord(text[i]) ^ ord(key[i % len(key)]))
    return encrypted_text


char_to_encrypt1=11100
XOR_key1=10011

plain_text="Test du chiffrement par XOR"

key="786898EA8676739827387"

encrypted_text=encrypt_XOR(plain_text, key)
print(f'Encypted text : {encrypted_text}')
