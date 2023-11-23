#!/usr/bin/env python3

def reverse(l):
    if len(l) == 0:
        return l
    return [l[-1]] + reverse(l[:-1])

from reverse_102 import reverse

def main():
    print(reverse([1,2,3]))
    print(reverse([3,4,5,6]))
    print(reverse([1,2]))

if __name__ == '__main__':
    main()
