from operator import mul
from functools import wraps, reduce
from charm.toolbox.pairinggroup import PairingGroup, ZR, G1, pairing

class SchnorrZkp:
    benchMarkFlag = True

    def __init__(self):    
        self.group = PairingGroup('MNT224')
        

    def benchMarkGenerator(enable = False):
        def decorater(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                if not enable:
                    return func(self, *args, **kwargs)
                
                self.startBenchmark()
                result = func(self, *args, **kwargs)
                self.endAndOutputBenchmark()
                return result
            return wrapper
        return decorater
    
    def startBenchmark(self):
        try:
            self.group.StartBenchmark(["CpuTime", "RealTime", "Add", "Sub", "Mul", "Div", "Exp", "Pair", "Granular"])
        except:
            self.group.InitBenchmark()
            self.group.StartBenchmark(["CpuTime", "RealTime", "Add", "Sub", "Mul", "Div", "Exp", "Pair", "Granular"])
    
    def endAndOutputBenchmark(self):
        self.group.EndBenchmark()
        print(self.group.GetGeneralBenchmarks())

    @benchMarkGenerator(benchMarkFlag)
    def setup(self, n = 1):
        self.g = []
        for i in range(n):
            self.g.append(self.group.random(G1))

    @benchMarkGenerator(benchMarkFlag)
    def generateSecret(self, n = 1):
        secret = []
        for i in range(n):
            secret.append(self.group.random(ZR))
        return secret

    @benchMarkGenerator(benchMarkFlag)
    def generateStatement(self, secret = None):
        if len(secret) != len(self.g):
            raise Exception("Length of secret not equal to length of public parameter!")
        
        statement = reduce(mul, (g_i ** secret_i for g_i, secret_i in zip(self.g, secret)), 1)
        return statement

    @benchMarkGenerator(benchMarkFlag)
    def generateProof(self, secret = None):
        if len(secret) != len(self.g):
            raise Exception("Length of secret not equal to length of public parameter!")
        
        r = [self.group.random(ZR) for _ in secret]
        R = reduce(mul, (g_i ** r_i for g_i, r_i in zip(self.g, r)), 1)
        c = self.group.hash([R], ZR)
        z = [r_i + c*secret_i for r_i, secret_i in zip(r, secret)]
        return R, z
    
    @benchMarkGenerator(benchMarkFlag)
    def verifyProof(self, R = None, z = None, statement = None):
        if len(z) != len(self.g):
            raise Exception("Length of proof not equal to length of public parameter!")
        
        c = self.group.hash([R], ZR)
        lhs = R * (statement ** c)
        rhs = reduce(mul, (g_i ** z_i for g_i, z_i in zip(self.g, z)), 1)
        return lhs == rhs