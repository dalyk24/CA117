#!/usr/bin/env python3

class Point:
	def __init__ (self, x=0, y=0):
		self.x = x
		self.y = y

	def midpoint(self, other):
		mid_x = (self.x + other.x) / 2
		mid_y = (self.y + other.y) / 2
		return Point(mid_x, mid_y)

	def __str__(self):
		return '({:.1f}, {:.1f})'.format(self.x, self.y)
