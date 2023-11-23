#!/usr/bin/env python3

class MP3Track(object):
	def __init__(self, title, duration, artists=None):
		if artists == None:
			artists = []

		self.title = title
		self.duration = duration
		self.artists = artists

	def __str__(self):
		rl = []
		rl.append('Title: {}'.format(self.title))
		rl.append('Duration: {}'.format(self.duration))

		return '\n'.join(rl)

class MP3Collection(object):
	def __init__(self):
		self.d = {}

	def add(self, t):
		self.d[t.title] = t

	def remove(self, title):
		del(self.d[title])

	def lookup(self, title):
		if title in self.d.keys():
			return self.d[title]
		return None

	def __add__(self, other):
		c = MP3Collection()
		for mp3 in self.d.values():
			c.add(MP3Track(mp3.title, mp3.duration, mp3.artists[:]))
		for mp3 in other.d.values():
			c.add(MP3Track(mp3.title, mp3.duration, mp3.artists[:]))

		return c

from mp3collection_v2_122 import MP3Track, MP3Collection

def main():
    t1 = MP3Track('Fools Gold', 604, ['The Stone Roses'])
    t2 = MP3Track('Shallow', 197, ['Lady Gaga', 'Bradley Cooper'])
    t3 = MP3Track('Telephone', 220, ['Beyonce', 'Lady Gaga'])

    c1 = MP3Collection()
    c1.add(t1)
    c1.add(t2)

    c2 = MP3Collection()
    c2.add(t3)

    # Make a new collection from two existing ones
    c3 = c1 + c2
    assert(isinstance(c3, MP3Collection))
    assert(c3 is not c1)
    assert(c3 is not c2)

if __name__ == '__main__':
    main()