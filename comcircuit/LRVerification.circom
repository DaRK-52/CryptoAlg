pragma circom  2.1.6;
include "Utils.circom";
include "node_modules/circomlib/circuits/sha256/sha256.circom";
include "node_modules/circomlib/circuits/sha256/sha256_2.circom";

// verification process of linear regression
template LRVerification(N) {
    signal input x[N];
    signal input y[N];
    signal input w;
    signal input b;
    signal temp[N];
    signal yPred[N];
    signal loss[N];
    signal output score;

    for (var i = 0;i < N;i++) {
        temp[i] <== w * x[i];
        yPred[i] <== temp[i] + b;
        loss[i] <== (y[i] - yPred[i]) * (y[i] - yPred[i]);
    }
    component sum = Sum(N);
    sum.in <== loss;
    score <== sum.out / N;
}

component main = LRVerification(10);