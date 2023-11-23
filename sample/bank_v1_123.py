#!/usr/bin/env python3

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
