# -*- coding: utf-8 -*-

__author__ = 'Ghazal_Azadi'
__email__ = '@ghazal.azadi@nmbu.no'


class LCGRand:
    a = 7 ** 5
    m = (2 ** 31) - 1

    def __init__(self, seed):
        self.seed = seed

    def rand(self):
        self.seed = (LCGRand.a * self.seed) % LCGRand.m
        return self.seed


class ListRand:

    def __init__(self, mylist):
        self.mylist = mylist
        self.index = -1

    def rand(self):
        self.index += 1
        if self.index >= len(self.mylist):
            raise RuntimeError("The Last item has already been called")

        return self.mylist[self.index]
