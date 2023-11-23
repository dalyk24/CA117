#!/usr/bin/env python3

import math

class Point(object):
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def distance(self1, self2):
		return math.sqrt((self2.x - self1.x)**2 + (self2.y - self1.y)**2)

	def withdraw(self, amount):
		if amount <= self.balance:
			self.balance -= amount

	def __str__(self):
		return "({:.1f}, {:.1f})".format(self.x, self.y)
