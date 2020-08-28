# -*- coding: utf-8 -*-

"""
Author: Road36
Date: 2020-03-29
Describe:
"""

global counter


def doLotsOfStuff():
    for i in (1, 2, 3):
        counter += 1


doLotsOfStuff()
print(counter)
