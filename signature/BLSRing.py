from charm.toolbox.pairinggroup import PairingGroup, ZR, G1, G2, pair
from BLS import BLS
from math import prod


class BLSRing:
    # Since idk how to map G2 to G1, i use SS512 as a
    # symmetric pairing group where G1 = G2
    # we need to notice that g1 = g2 in this situation
    # because we need to construct the equation of
    # H(m)^{1-a1x1-a2x2-...}
    def __init__(self, n=10):
        self.group = PairingGroup("SS512")
        self.g1 = self.g2 = self.group.random(G1)
        self.ring = [BLS(group=self.group, g2=self.g2) for _ in range(n)]

    def sign(self, message, j):
        sig = []
        h = self.group.hash(message, G1)
        for i in range(len(self.ring)):
            if i != j:
                a_i = self.group.random(ZR)
                sig.append(self.g1**a_i)
                h = h / (self.ring[i].pk ** a_i)
        sig.insert(j, h ** (1 / self.ring[j].sk))
        return sig

    def verifySign(self, message, sig):
        h = self.group.hash(message, G1)
        return pair(h, self.g2) == self.prod_pair(sig)

    def prod_pair(self, sig):
        return prod(pair(sig[i], self.ring[i].pk) for i in range(len(self.ring)))
