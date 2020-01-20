#!/usr/bin/env python
class Calculator:
    """docstring for Calculator."""

    def __init__(self, inta,intb):
        self.a = inta
        self.b = intb
    def add(self):
        return self.a + self.b# BUG:
    def mul(self):
        return self.a * self.b# BUG:
class Scientific(Calculator):
    def power(self):
        return pow(self.a,self.b)

def quickAdd(a,b):
    return a+b
