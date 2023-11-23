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

class Circle:
	def __init__(self, centre=None, radius=1):
		if centre is None:
			temp_obj = Point()
			centre = temp_obj

		self.centre = centre
		self.radius = radius

	def __str__(self):
		return 'Centre: {:s}\nRadius: {:d}'.format(str(self.centre), self.radius)
