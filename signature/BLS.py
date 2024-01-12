from charm.toolbox.pairinggroup import PairingGroup, ZR, G1, G2, pair


class BLS:
    def __init__(self, group=None, g2=None, sk=None):
        self.group = group if group is not None else PairingGroup("MNT224")
        self.g2 = g2 if g2 is not None else self.group.random(G2)
        self.sk = sk if sk is not None else self.group.random(ZR)
        self.pk = self.g2**self.sk

    def sign(self, message):
        h = self.group.hash(message, G1)
        sig = h ** (1 / self.sk)
        return sig

    def verifySign(self, message, sig):
        return pair(self.group.hash(message, G1), self.g2) == pair(sig, self.pk)
