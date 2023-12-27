pragma circom  2.1.6;

include "node_modules/circomlib/circuits/comparators.circom";

template Relu() {
    signal input x;
    signal output out;
    component lt = LessThan(32);
    
    lt.in[0] <== 0;
    lt.in[1] <== x;
    out <== x * lt.out;
}