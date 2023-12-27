pragma circom  2.1.6;
include "node_modules/circomlib/circuits/sha256/sha256.circom";
include "node_modules/circomlib/circuits/bitify.circom";

// template used to calculate sum of x[N]
template Sum(N) {
    signal input in[N];
    signal output out;
    var temp = 0;

    for (var i = 0;i < N;i++) {
        temp += in[i];
    }

    out <== temp;
}

// number transfer to 32 bits first
template Sha256Util(N) {
    var bitLength = 32;
    signal input in[N];
    signal output out[256];
    component n2b[N];
    component sha256 = Sha256(N*bitLength);
    
    for (var i = 0;i < N;i++) {
        n2b[i] = Num2Bits(bitLength);
        n2b[i].in <== in[i];
        for (var j = 0;j < bitLength;j++) {
            sha256.in[i*bitLength+j] <== n2b[i].out[j];
        }
    }
    out <== sha256.out;
}