pragma circom  2.1.6;

// template used to calculate sum of x[N]
template Sum(N) {
    signal input x[N];
    signal output sum;
    var temp = 0;

    for (var i = 0;i < N;i++) {
        temp += x[i];
    }

    sum <== temp;
}

// template used to calculate function's 
// taylor expansion of order n
template TaylorExp(N) {
    signal input x;
    signal input c[N];
    signal powerOfX[N]; // x^i
    signal polyTerm[N]; // c_i * x^i
    signal output result;

    powerOfX[0] <== 1;
    polyTerm[0] <== powerOfX[0] * c[0];
    for (var i = 1; i < N; i++) {
        powerOfX[i] <== powerOfX[i-1] * x;
        polyTerm[i] <== powerOfX[i] * c[i];
    }
    component sum = Sum(N);
    sum.x <== polyTerm;

    result <== sum.sum;
}

component main = TaylorExp(5);