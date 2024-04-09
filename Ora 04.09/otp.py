import pyotp

if __name__ == "__main__":
    secret_key = pyotp.random_base32()
    otp = pyotp.TOTP(secret_key, interval = 81)
    print(secret_key)
    print((otp.now()))
    user_otp = input("Enter otp:")
    if (otp.verify(user_otp)):
        print("Great succes")
    else:
        print("Bozoooooo")