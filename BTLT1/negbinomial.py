# -*- coding: utf-8 -*-

import math


 #Tính n!
def fac(n):
    if n <= 1:
        return 1;
    else:
        return n * fac(n - 1);

#Tính C(i, n)
def combi(i, N):
    return fac(N)/(fac(i)*fac(N - i));

def prob(n, p, r):
    return combi(n - r + 1, n)*(p ** n)*(1 - p)**r;


#lượng tin tương ứng với symbol 
def infoMeasure(n, p, r):
    return -math.log(prob(n, p, r), 2);

#Tính tổng của xác suất của tất cả các symbol từ 1 đến N
def sumProb(N, p, r):
    sumprob = 0;
    for i in range(1, N + 1):
        sumprob += prob(i, p, r);
    return sumprob;

#Tính entropy với p=0.5
def approxEntropy(N, p, r):
    sum = 0;
    for i in range(1, N + 1):
        sum += prob(i, p, r)*infoMeasure(i, p, r);
    return sum;

print(approxEntropy(6, 0.5, 2));