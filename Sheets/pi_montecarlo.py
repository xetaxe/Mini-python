# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 20:57:23 2020

@author: Nil
"""


import random as rd
import numpy as num
import matplotlib.pyplot as plt

total_counts = 0
circle_counts = 0
points_x = []
points_y = []
aprox_pi = 0

while total_counts < 30000000:
    x = rd.uniform(0, 1)
    y = rd.uniform(0, 1)
    total_counts += 1
    if x**2 + y**2 <= 1:
        circle_counts += 1
    if total_counts % 100000 == 0:
        aprox_pi = 4 * (float(circle_counts) / total_counts)
        points_x.append(total_counts)
        points_y.append(aprox_pi)

plt.plot(points_x, points_y)
plt.axhline(y=num.pi, color='r', linestyle='-')
print("iteracions: {}, aprox de pi: {}\n".format(total_counts, aprox_pi))
