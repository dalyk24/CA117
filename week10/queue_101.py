#!/usr/bin/env python3

class Queue(object):
	def __init__(self):
		self.l = []

	def enqueue(self, e):
		self.l.insert(0, e)

	def dequeue(self):
		front_q = self.l[-1]
		self.l.pop()
		return front_q

	def first(self):
		return self.l[-1]

	def __len__(self):
		return len(self.l)

	def is_empty(self):
		return len(self.l) == 0
