#!/usr/bin/env python3

import sys
import math

def num_size(nth_num):
    digits = int(math.log2(nth_num))
    return digits, nth_num - 2 ** digits

def num_calc(magic_num, loops):
    rem_digits = len(magic_num)
    i = -1

    while rem_digits > 0:
	    rem_digits -= 1
	    if loops > 2 ** (rem_digits):
		    loops = int(loops - 2 ** (rem_digits))
		    magic_num[i] = "9"
	    i -= 1

    for k in range(loops):
	    p = magic_num.index("3")
	    magic_num[:p] = ["3"] * p
	    magic_num[p] = "9"

    return magic_num

def main():
    nth_num = int(sys.stdin.readline()) + 1
    digits, loops = num_size(nth_num)
    magic_num = num_calc(["3"] * digits, loops)
    print("".join(magic_num[::-1]))

if __name__ == '__main__':
    main()
