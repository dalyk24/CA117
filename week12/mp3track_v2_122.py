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
		rl.append('By: {}'.format(', '.join(self.artists)))
		rl.append('Duration: {}'.format(self.duration))

		return '\n'.join(rl)

from mp3track_v2_122 import MP3Track

def main():
    t1 = MP3Track('Fools Gold', 604, ['The Stone Roses'])
    t2 = MP3Track('Shallow', 197, ['Lady Gaga', 'Bradley Cooper'])
    t3 = MP3Track('Telephone', 220, ['Beyonce', 'Lady Gaga'])

    print(t1)
    print(t2)
    print(t3)

if __name__ == '__main__':
    main()
