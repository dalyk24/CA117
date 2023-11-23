#!/usr/bin/env python3

from math import sqrt

class Stack(object):
    def __init__(self):
        self.l = []

    def push(self, e):
        self.l.append(e)

    def top(self):
        return self.l[-1]

    def pop(self):
        return self.l.pop()

def calculator(line):
    binops = {'+': float.__add__,
            '-': float.__sub__,
            '*': float.__mul__,
            '/': float.__truediv__}

    uniops = {'n': float.__neg__,
            'r': sqrt}

    exp = Stack()
    list_line = line.split()

    for l in list_line:
        try:
            exp.push(float(l))
        except ValueError:
            if l in binops.keys():
                temp = exp.pop()
                exp.push(binops[l](exp.pop(), temp))
            elif l in uniops.keys():
                exp.push(uniops[l](exp.pop()))

    try:
        return exp.pop()
    except IndexError:
        return 'Invalid RPN expression'
