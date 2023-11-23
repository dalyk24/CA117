#!/usr/bin/env python3

def formatter(duration):
	mins = duration // 60
	secs = duration % 60

	return mins, secs

class MP3Track(object):
	def __init__(self, title, duration, artists=None):
		if artists == None:
			artists = []

		self.title = title
		self.duration = duration
		self.artists = artists

	def __str__(self):
		mins, secs = formatter(self.duration)
		rl = []
		rl.append('Title: {}'.format(self.title))
		rl.append('By: {}'.format(', '.join(self.artists)))
		rl.append('Duration: {}:{:02d}'.format(mins, secs))

		return '\n'.join(rl)

from mp3track_v3_122 import MP3Track

def main():
    t1 = MP3Track('Fools Gold', 604, ['The Stone Roses'])
    t2 = MP3Track('Shallow', 197, ['Lady Gaga', 'Bradley Cooper'])
    t3 = MP3Track('Telephone', 220, ['Beyonce', 'Lady Gaga'])
    t4 = MP3Track('Her Majesty', 34, ['The Beatles'])
    t5 = MP3Track('Seven Seconds', 7, ['Neneh Cherry'])

    print(t1)
    print(t2)
    print(t3)
    print(t4)
    print(t5)

if __name__ == '__main__':
    main()