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

newCalculator = Calculator(10,20)
print 'a+b: %d'%newCalculator.add()
print 'a*b: %d'%newCalculator.mul()

newPower = Scientific(2,3)
print 'a+b %d'%newPower.add()
print 'a+b %d'%newPower.mul()
print 'a power b %d'%newPower.power()
