#!/usr/bin/env python3

class Point(object):
	def set_attributes(self, x, y):
		self.x = x
		self.y = y

	def print_attributes(self):
		x = float(self.x)
		y = float(self.y)

		print("x: {:.2f}".format(self.x))
		print("y: {:.2f}".format(self.y))

	def reflect(self):
		self.x *= -1
		self.y *= -1
