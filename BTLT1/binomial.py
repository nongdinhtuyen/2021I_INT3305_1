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

def prob(n, p, N):
    return combi(n, N)*(p ** n)*(1 - p)**(N - n);


#lượng tin tương ứng với symbol 
def infoMeasure(n, p, N):
    return -math.log(prob(n, p, N), 2);

#Tính tổng của xác suất của tất cả các symbol từ 1 đến N
def sumProb(N, p):
    sumprob = 0 ;
    for i in range(1, N + 1):
        sumprob += prob(i, p, N);

    return sumprob;

#Tính entropy với p=0.5
def approxEntropy(N, p):
    sum = 0;
    for i in range(1, N + 1):
        sum += prob(i, p, N)*infoMeasure(i, p, N);
    return sum;

print(approxEntropy(6, 0.5));