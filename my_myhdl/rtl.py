# -*- coding: utf-8 -*-

"""
Author: Road36
Date: 2021-01-23
Describe:
"""

import random
from myhdl import block, always_comb, Signal, instance, intbv, delay
import pickle
import yaml

@block
def mux(z, a, b, sel):
    """ Multiplexer.
    z -- mux output
    a, b -- data inputs
    sel -- control input: select a if asserted, otherwise b
    """

    @always_comb
    def comb():
        if sel == 1:
            z.next = a
        else:
            z.next = b

    return comb


random.seed(5)
randrange = random.randrange


@block
def test_mux():
    z, a, b, sel = [Signal(intbv(0)) for i in range(4)]

    mux_1 = mux(z, a, b, sel)

    @instance
    def stimulus():
        print("z a b sel")
        for i in range(12):
            a.next, b.next, sel.next = randrange(8), randrange(8), randrange(2)
            yield delay(10)
            print("%s %s %s %s" % (z, a, b, sel))

    return mux_1, stimulus


tb = test_mux()
tb.run_sim()
