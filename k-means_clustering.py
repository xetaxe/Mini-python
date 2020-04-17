# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 08:45:24 2020

@author: Nil
"""


import random as rd
import numpy as num
import matplotlib.pyplot as plt


def x_var(x):
    if x > 0.5:
        return rd.uniform(0.55, 1)
    else:
        return rd.uniform(0, 0.45)


def clustering(x, y, n):
    cmap = plt.cm.Spectral
    norm = plt.Normalize(vmin=1, vmax=n)

    cluster = []
    means = num.zeros((n, 2))
    for i in x:
        cluster.append(rd.randint(1, n))

    plt.scatter(x, y, c=cmap(norm(cluster)))
    
    for i in range(20):
        for j in range(n):
            var_x = []
            var_y = []
            for k in range(len(x)):
                if cluster[k] == j+1:
                    var_x.append(x[k])
                    var_y.append(y[k])
            means[j][0] = num.mean(var_x)
            means[j][1] = num.mean(var_y)

        for j in range(len(x)):
            cluster_distance = []
            for k in range(n):
                cluster_distance.append((x[j]-means[k][0])**2 + (y[j]-means[k][1])**2)
            cluster[j] = num.argmin(cluster_distance)+1

        plt.scatter(x, y, c=cmap(norm(cluster)))


x = []
y = []

for i in range(100):
    x.append(x_var(rd.uniform(0, 1)))
    y.append(rd.uniform(0, 1))

for i in range(2, 3):
    clustering(x, y, i)
