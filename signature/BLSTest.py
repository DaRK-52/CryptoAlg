from BLS import BLS

if __name__ == "__main__":
    bls = BLS()
    message = "Test Message!"
    sig = bls.sign(message)
    print("Verifity result is", bls.verifySign(message, sig))
