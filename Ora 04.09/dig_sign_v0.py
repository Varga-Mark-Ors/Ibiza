from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import utils


if __name__ == "__main__":
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
    public_key = private_key.public_key()
    private_key2 = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
    public_key2 = private_key.public_key()
    message = b"Alice this is Bob"
    signature1 = private_key.sign(message, padding.PSS(mgf = padding.MGF1(hashes.SHA256()),
                                         salt_length = padding.PSS.MAX_LENGTH),
                                         hashes.SHA256())
    message2 = b"Teszt"
    signature2 = private_key2.sign(message2, padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                                                       salt_length=padding.PSS.MAX_LENGTH),
                                  hashes.SHA256())
    public_key.verify(signature1, message, padding.PSS(mgf = padding.MGF1(hashes.SHA256()),
                                         salt_length = padding.PSS.MAX_LENGTH),
                                         hashes.SHA256())

    print(public_key.verify(signature1, message, padding.PSS(mgf = padding.MGF1(hashes.SHA256()),
                                         salt_length = padding.PSS.MAX_LENGTH),
                                         hashes.SHA256()))

    print("Succesful")