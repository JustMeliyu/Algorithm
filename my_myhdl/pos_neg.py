# -*- coding: utf-8 -*-

"""
Author: Road36
Date: 2021-01-15
Describe:
"""


from myhdl import block, Signal, delay, always, now, always_comb


@block
def HelloWorld():

    clk = Signal(0)

    @always(delay(10))
    def drive_clk():
        clk.next = not clk
        print("drive clk, %s" % now())

    @always(clk.posedge)
    def say_hello():
        print("posedge %s" % now())

    @always(clk.negedge)
    def sys_bay():
        print("negedge %s" % now())

    return drive_clk, say_hello, sys_bay


inst = HelloWorld()
inst.run_sim(50)
