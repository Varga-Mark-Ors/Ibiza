from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.PublicKey import RSA
from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import ECC
from Cryptodome.Signature import DSS, __all__
from Cryptodome.PublicKey import DSA
from Cryptodome.Signature import pkcs1_15
import pyotp


class User:
    def __init__(self, name, private_key, public_key):
        self.name = name
        self.private_key = private_key
        self.public_key = public_key
        secret_key = pyotp.random_base32()
        self.otp = pyotp.TOTP(secret_key, interval=180)


    def __str__(self):
        return f"User : {self.name}\nPrivate key: {self.private_key}\nPublic Key: {self.public_key}"

    def getOtp(self):
        return self.otp.now()

def create_rsa_key():
    key = RSA.generate(2048)
    print(str(key.e))
    print(str(key.d))
    return key



def create_text_file():
    file_name = input("Adja meg a file nevét: ")
    try:
        with open(file_name, 'w') as file:
            print(f"A(z) '{file_name}' létrehozva!")
    except Exception as e:
        print(e)


def create_rsa_signature(private_key, input_file, output_file):
    if not isinstance(private_key, RSA.RsaKey) or not private_key.has_private():
        print("Menj a faszba")
        return
    try:
        with open(input_file, 'rb') as file_to_sign:
            data = file_to_sign.read()
            hash_obj = SHA256.new(data)
            signature = pkcs1_15.new(private_key).sign(hash_obj)
        with open(output_file, 'wb') as signed_file:
            signed_file.write(signature)

    except Exception as e:
        print(e)

def verify_signature(key, input_file, signature_file):
    if not isinstance(key, RSA.RsaKey):
        print("Hibás nyilvános kulcs!")
        return
    public_key = key.public_key()

    with open(signature_file, "rb") as sig_file:
        signature = sig_file.read()
    with open(input_file, "rb") as original_file:
        data = original_file.read()
        hash_obj = SHA256.new(data)

    try:
        pkcs1_15.new(public_key).verify(hash_obj, signature)
        print("Aláírás valid")
    except:
        print("Aláírás nem valid")



if __name__ == '__main__':
    Alicekey = create_rsa_key()
    Alice = User("Alice", Alicekey.d, Alicekey.e)
    # print(str(Alice))
    # Bobkey = create_rsa_key()
    # Bob = User("Bob", Bobkey.d, Bobkey.e)

    # create_text_file()
    # input_file = input("Add meg ay aláírandó nevét:")
    # print("A(z) {} nevű file létrehozva".format(input_file))
    # signature_file = input("Adja meg az aláírás file-ját:")

    # create_rsa_signature(Alicekey, input_file, signature_file)
    # print("Digitális aláírás létrehozva {} file-ban.".format(signature_file))
    # verify_signature(Alicekey, input_file, signature_file)

    print("Jelenlegi OTP::", Alice.getOtp())
    alairando = input("Adja meg az aláírandó nevét:")
    alairas = input("Adja meg az aláírás milyen nevű file-ban tárolja:")
    otp = input("Adja meg ay egyszerhasználatos jelszó!")

    if otp == Alice.getOtp():
        create_rsa_signature(Alicekey, alairando, alairas)
    else:
        print("Nem megfelelő.")

    verify_signature(Alicekey, alairando, alairas)