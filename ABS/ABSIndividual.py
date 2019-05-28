# -*- coding: utf-8 -*- 

__author__ = "Road36"
__date__ = "19-5-28"

"""
Describe:
"""
import numpy as np
import ObjFunction


class ABSIndividual:

    """
    individual of artificial bee swarm algorithm
    """

    def __init__(self,  vardim, bound):
        """
        vardim: dimension of variables
        bound: boundaries of variables
        """
        self.vardim = vardim
        self.bound = bound
        self.fitness = 0.
        self.trials = 0

    def generate(self):
        """
        generate a random chromsome for artificial bee swarm algorithm
        """
        rnd = np.random.random(size=self.vardim)
        self.chrom = np.zeros(self.vardim)
        for i in range(0, self.vardim):
            self.chrom[i] = self.bound[0, i] + \
                (self.bound[1, i] - self.bound[0, i]) * rnd[i]

    def calculateFitness(self):
        """
        calculate the fitness of the chromsome
        """
        self.fitness = ObjFunction.GrieFunc(
            self.vardim, self.chrom, self.bound)
