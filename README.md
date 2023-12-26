# Crypto Algorithms
Implement some crypto algorithms in python.

## schnorrzkp
```
cd schnorrzkp
python SchnorrZkp.py
```

## comcircuit
```
cd comcircuit
docker run -it -v ./:/root/test saleel/circom:2.1.6 bash
npm list -g circomlib
circom xxx.circom --r1cs
snarkjs info -r xxx.r1cs
```