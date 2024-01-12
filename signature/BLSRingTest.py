from BLSRing import BLSRing

if __name__ == "__main__":
    blsRing = BLSRing()
    message = "Test Message!"
    sig = blsRing.sign(message, 0)
    print("Verifity result is", blsRing.verifySign(message, sig))
