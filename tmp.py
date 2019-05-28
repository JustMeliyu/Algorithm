# -*- coding: utf-8 -*- 

"""
Author: Road36
Date: 19-5-17
Describe:
"""

import numpy as np

a = [1, 2, 3]
print(np.eye(4))
b = np.array([a])

d = [[0, 1, 2, 10],
     [12, 13, 100, 101],
     [102, 110, 112, 113]]
c = np.array(d, int)

print(b)
print(c)
print("=======")
print(c.ndim)
print(c.shape)
print("---")

print("=======")
x = np.empty([3, 2], dtype=int)
print(x)
print(x[0])
print(x[0][0])

x = np.zeros([3, 2], dtype=int)
print(x)
print(x[0])
print(x[0][0])

x = np.ones(5)
print(x)
print(x[0])

x = np.arange(10)
s = slice(2, 7, 2)
print(x)
print(x[2:7:2])

x = np.array([[1, 2], [3, 4], [5, 6]])
y = x[[0, 1, 2], [0, 1, 0]]
print(y)
print(type(y))
print(list(y))

x = np.arange(32).reshape((8, 4))
print(x)

a = np.random.random_integers(5, size=(3, 2))
# b = np.random.random_integers(5, size=(3, 2))
print(a)

# a = np.random.randint(8, size=(2,2,3), dtype='int64')
# print(a)
