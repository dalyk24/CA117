#!/usr/bin/env python3

class Student(object):
	def __init__(self, name, sid, modmarks=None):
		if modmarks == None:
			modmarks = []

		self.name = name
		self.sid = sid
		self.modmarks = modmarks

	def avg_mark(self, modmarks):
		total = 0

		for k, v in modmarks:
			total += v

		return round(total / len(modmarks))

	def get_modules(self, modules=None):
		lines = []

		if modules == None:
			modules = []

		for k, v in modules:
			lines.append(k)

		return sorted(lines)

	def __str__(self):
		lines = []
		lines.append('Name: {:s}'.format(self.name))
		lines.append('ID: {:d}'.format(self.sid))
		lines.append('Modules: {:s}'.format(', '.join(self.get_modules(self.modmarks))))
		lines.append('Average mark: {:d}'.format(self.avg_mark(self.modmarks)))

		return '\n'.join(lines)
