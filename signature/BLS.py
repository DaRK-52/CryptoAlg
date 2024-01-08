from charm.toolbox.pairinggroup import PairingGroup, ZR, G1, G2, pair


class BLS:
    def __init__(self):
        self.group = PairingGroup("MNT224")
        self.g2 = self.group.random(G2)
        self.sk = self.group.random(ZR)
        self.pk = self.g2**self.sk

    def sign(self, message):
        h = self.group.hash(message, G1)
        sig = h ** (1 / self.sk)
        return sig

    def verifySign(self, message, sig):
        return pair(self.group.hash(message, G1), self.g2) == pair(sig, self.pk)
