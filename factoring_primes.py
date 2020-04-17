# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 22:10:20 2020

@author: Nil
"""


import numpy as num
import time
import matplotlib.pyplot as plt


def possiblePrimes(n):
    primers = []
    natural = 2
    isPrime = True

    while natural <= n:
        for i in primers:
            if natural % i == 0:
                isPrime = False
                break
        if isPrime:
            primers.append(natural)

        natural += 1
        isPrime = True

    return primers


def nextFactor(n, possibleFactors):
    for i in possibleFactors:
        if n % i == 0:
            return i
    return n


def factorize(n, possibleFactors):
    a = n
    if possibleFactors == 0:
        possibleFactors = possiblePrimes(int(num.sqrt(n)))
    factors = []
    while a != 1:
        b = nextFactor(a, possibleFactors)
        factors.append(int(b))
        a /= b
    return factors


counter = 1
times = []
count = []
start = 0
end = 0

possibleFactors = possiblePrimes(int(num.sqrt(200000)))
while counter < 1000000:
    if counter % 10000 == 0:
        start = time.time()
    factors = factorize(counter, possibleFactors)
    if counter % 10000 == 9999:
        end = time.time()
        count.append(counter)
        times.append(end - start)
    counter += 1

plt.scatter(count, times, s=2)
