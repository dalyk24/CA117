#!/usr/bin/env python3

counter = 0

def count(s):
    global counter
    if s == "":
        temp = counter
        counter = 0
        return temp
    counter += 1
    return count(s[:-1])

def main():
    len = None
    print(count('cat'))
    print(count('catastrophe'))
    print(count(''))

if __name__ == '__main__':
    main()
