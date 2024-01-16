from SSLE import SSLE
from charm.toolbox.pairinggroup import PairingGroup, ZR, G1, G2, pair

if __name__ == "__main__":
    num = 10
    ssle = SSLE()
    group = PairingGroup("MNT224")
    g = group.random(G1)
    r = [group.random(ZR) for i in range(num)]
    x = [group.random(ZR) for i in range(num)]

    for i in range(num):
        ssle.submitSecret([g ** r[i], g ** (r[i] * x[i])])
        ssle.shuffle()

    result = ssle.elect()
    for i in range(num):
        if result[0] ** x[i] == result[1]:
            print("Leader is {}".format(i))
