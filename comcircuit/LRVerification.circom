pragma circom  2.1.6;
include "Utils.circom";
include "node_modules/circomlib/circuits/sha256/sha256.circom";

// verification process of linear regression
template LRVerification(N) {
    signal input x[N], y[N];
    signal input w, b;
    signal temp[N];
    signal yPred[N];
    signal loss[N];
    signal output score;
    signal output hashW[256];
    signal output hashB[256];
    signal output hashX[256];
    signal output hashY[256];

    for (var i = 0;i < N;i++) {
        temp[i] <== w * x[i];
        yPred[i] <== temp[i] + b;
        loss[i] <== (y[i] - yPred[i]) * (y[i] - yPred[i]);
    }
    component sum = Sum(N);
    sum.in <== loss;
    score <== sum.out / N;

    component sha256W = Sha256Util(1), sha256B = Sha256Util(1);
    component sha256X = Sha256Util(N), sha256Y = Sha256Util(N);
    sha256W.in[0] <== w;
    sha256B.in[0] <== b;
    sha256X.in <== x;
    sha256Y.in <== y;
    hashW <== sha256W.out;
    hashB <== sha256B.out;
    hashX <== sha256X.out;
    hashY <== sha256Y.out;
}

component main = LRVerification(10);