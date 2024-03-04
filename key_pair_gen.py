from Crypto.PublicKey import RSA

def generate_rsa_key_pair():
    """
    Generates an RSA key pair.
    """
    key = RSA.generate(2048)  # Generate a 2048-bit RSA key pair
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def main():
    # Generate RSA key pair
    private_key, public_key = generate_rsa_key_pair()

    # Save RSA keys to files
    with open("./pem/private_key.pem", "wb") as f:
        f.write(private_key)
    with open("./pem/public_key.pem", "wb") as f:
        f.write(public_key)

    print("RSA key pair generated and saved successfully.")

if __name__ == "__main__":
    main()
