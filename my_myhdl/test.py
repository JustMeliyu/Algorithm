# -*- coding: utf-8 -*-

"""
Author: Road36
Date: 2021-01-23
Describe:
"""

from myhdl import intbv, modbv, Signal

real = Signal(0)
imag = Signal(0)

data_bus = intbv(0)[8:0]
real.next = data_bus[8:4].signed()
imag.next = data_bus[4:].signed()
