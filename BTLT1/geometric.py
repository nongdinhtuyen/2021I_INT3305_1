# -*- coding: utf-8 -*-

import math

def prob(n, p):
    return ((1-p)**(n-1))*p;

def infoMeasure(n, p):
    return -math.log(prob(n, p), 2);

def sumProb(N, p):
    sumprob = 0;
    for i in range(1, N + 1):
        sumprob += prob(i, p);
    return sumprob;

def approEntropy(N, p):
    sum = 0;
    for i in range(1, N + 1):
        sum += prob(i, p) * infoMeasure(i, p);
    return sum;