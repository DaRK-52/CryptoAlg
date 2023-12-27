pragma circom  2.1.6;
include "node_modules/circomlib/circuits/sha256/sha256.circom";

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