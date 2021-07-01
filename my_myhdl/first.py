# -*- coding: utf-8 -*-

"""
Author: Road36
Date: 2021-03-30
Describe:
"""


from myhdl import block, now, delay, always


@block
def first():

    @always(delay(10))
    def say_first():
        print("first, now: {}".format(now()))

    return say_first


if __name__ == '__main__':
    inst = first()
    inst.run_sim(30)
