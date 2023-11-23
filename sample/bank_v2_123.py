#!/usr/bin/env python3

def sort_on(c):
    return c.number

class Customer(object):
    def __init__(self, name, number, balance = 0):
        self.name = name
        self.number = number
        self.balance = balance

    def lodge(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

    def __str__(self):
        rl = []
        rl.append('Name: {}'.format(self.name))
        rl.append('Number: {}'.format(self.number))
        rl.append('Balance: {:.2f}'.format(self.balance))

        return '\n'.join(rl)

class Bank(object):
    def __init__(self):
        self.d = {}

    def add(self, c):
        self.d[c.number] = c

    def remove(self, number):
        del(self.d[number])

    def lookup(self, number):
        if number in self.d.keys():
            return self.d[number]
        return None

    def __str__(self):
        funds = 0
        for m in self.d:
            funds += self.d[m].balance
        rl = ['{}'.format(t) for t in sorted(self.d.values(), key=sort_on)]
        rl.append('Total funds: {:.2f}'.format(funds))
        return '\n'.join(rl)
