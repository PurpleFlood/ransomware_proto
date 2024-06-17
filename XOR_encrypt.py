


## encrypt function

def encrypt_XOR(XOR_key, char_to_encrypt):
    output = char_to_encrypt ^ XOR_key
    return output


char_to_encrypt1=11100
XOR_key1=10011

print(encrypt_XOR(XOR_key1, char_to_encrypt1))
