#!/usr/bin/env python3

class Stack(object):
	def __init__(self):
		self.l = []

	def push(self, e):
		self.l.append(e)

	def top(self):
		return self.l[-1]

	def pop(self):
		return self.l.pop()

	def __len__(self):
		return len(self.l)

	def is_empty(self):
		return len(self.l) == 0

def matcher(brackets):
    d = {')' : '(', ']' : '[', '}' : '{',}

    s = Stack()

    for b in brackets:
        if b in d.values():
            s.push(b)
        elif b in d.keys() and not s.is_empty() and d[b] == s.top():
            s.pop()
        else:
            return False

    return s.is_empty()
