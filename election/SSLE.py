from charm.toolbox.pairinggroup import PairingGroup, ZR, G1, G2, pair
import random


class SSLE:
    def __init__(self) -> None:
        self.group = PairingGroup("MNT224")
        self.sharedList = []

    def submitSecret(self, secret):
        self.sharedList.append(secret)

    def shuffle(self):
        r = self.group.random(ZR)
        for item in self.sharedList:
            item[0] = item[0] ** r
            item[1] = item[1] ** r
        random.shuffle(self.sharedList)

    def elect(self):
        r = random.randint(0, len(self.sharedList))
        return self.sharedList[r]
