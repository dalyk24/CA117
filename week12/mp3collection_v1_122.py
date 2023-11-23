#!/usr/bin/env python3

class MP3Track(object):
	def __init__(self, title, duration):
		self.title = title
		self.duration = duration

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

from mp3collection_v1_122 import MP3Track, MP3Collection

def main():
    t1 = MP3Track('Fools Gold', 604)
    t2 = MP3Track('Shallow', 197)
    t3 = MP3Track('Telephone', 220)

    c = MP3Collection()

    c.add(t1)
    c.add(t2)
    c.add(t3)

    t = c.lookup('Fools Gold')
    assert(isinstance(t, MP3Track))
    assert(t.title == 'Fools Gold')
    assert(t.duration == 604)

    c.remove('Fools Gold')
    t = c.lookup('Fools Gold')
    assert(t is None)

if __name__ == '__main__':
    main()
