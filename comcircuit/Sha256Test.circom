pragma circom  2.1.6;
include "node_modules/circomlib/circuits/sha256/sha256.circom";

template Sha256Test() {
    signal input a;
    signal output out[256];
    component sha256 = Sha256(8);
    sha256.in[0] <== a;
    sha256.in[1] <== a;
    sha256.in[2] <== a;
    sha256.in[3] <== a;
    sha256.in[4] <== a;
    sha256.in[5] <== a;
    sha256.in[6] <== a;
    sha256.in[7] <== a;
    out <== sha256.out;
}

component main = Sha256Test();