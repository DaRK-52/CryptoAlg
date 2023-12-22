from SchnorrZkp import SchnorrZkp
from charm.toolbox.pairinggroup import PairingGroup, ZR

class SchnorrZkpTest:
    def __init__(self) -> None:
        self.schnorrZkp = SchnorrZkp()

    def setup(self, n):
        self.schnorrZkp.setup(n)
    
    def generateSecret(self, n):
        self.secret = self.schnorrZkp.generateSecret(n)
    
    def generateStatement(self):
        return self.schnorrZkp.generateStatement(self.secret)
    
    def generateProof(self):
        return self.schnorrZkp.generateProof(self.secret)

    def zkpTest(self):
        n = 10
        self.setup(n)
        self.generateSecret(n)
        statement = self.generateStatement()
        R, z = self.generateProof()
        print("Verify result is", self.schnorrZkp.verifyProof(R, z, statement))

if __name__ == '__main__':
    test = SchnorrZkpTest()
    test.zkpTest()