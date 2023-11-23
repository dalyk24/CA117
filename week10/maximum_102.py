#!/usr/bin/env python3

def maximum(l):
    if len(l) == 1:
        return l[0]
    l = sorted(l)
    return maximum(l[1:])
