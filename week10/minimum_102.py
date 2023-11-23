#!/usr/bin/env python3

def minimum(l):
    if len(l) == 1:
        return l[0]
    l = sorted(l)
    return minimum(l[:-1])
