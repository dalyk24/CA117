#!/usr/bin/env python3

class Student(object):
	def set_attributes(self, sid, name, modlist):
		self.sid = sid
		self.name = name
		self.modlist = modlist

	def print_attributes(self):
		print("ID: {:d}".format(self.sid))
		print("Name: {:s}".format(self.name))
		print("Modules: "+ ", ".join(self.modlist))

	def add_module(self, mod):
		if mod not in self.modlist:
			self.modlist.append(mod)

	def del_module(self, mod):
		if mod in self.modlist:
			self.modlist.remove(mod)
