#!/usr/bin/env python3

import math

class Student(object):
	def __init__(self, sid=0, name="", modlist=None):
		if modlist is None:
			modlist = []

		self.sid = sid
		self.name = name
		self.modlist = modlist

	def add_module(self, module):
		self.modlist.append(module)

	def del_module(self, module):
		if module in self.modlist:
			self.modlist.remove(module)

	def __str__(self):
		return "ID: {:d}\nName: {:s}\nModules: {:s}".format(self.sid, 
			self.name, ", ".join(sorted(self.modlist)))
