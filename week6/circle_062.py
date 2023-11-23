#!/usr/bin/env python3

import math

def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
    try:
        int(x1 + y1 + r1 + x2 + y2 + r2)
    except TypeError:
        return "Please Enter Valid Numbers"

    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if d >= r1 + r2:
        return False
    else:
        return True
