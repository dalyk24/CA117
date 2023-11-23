#!/usr/bin/env python3

class Meeting(object):
	def __init__(self, mid, organiser, start, end):
		self.mid = mid
		self.organiser = organiser
		self.start = start
		self.end = end

	def __str__(self):
		rl = []
		fstart = self.start.split(':')
		fend = self.end.split(':')
		rl.append('ID: {}'.format(self.mid))
		rl.append('Organised by: {}'.format(self.organiser))
		rl.append('When: {:02d}:{:02d}-{:02d}:{:02d}'.format(int(fstart[0]),
		 int(fstart[1]), int(fend[0]), int(fend[1])))

		return "\n".join(rl)

from meeting_v1_141 import Meeting

def main():
    m1 = Meeting(1, 'Sue', '14:00', '15:00')
    m2 = Meeting(2, 'Ned', '09:10', '10:20')

    assert(isinstance(m1, Meeting))
    assert(m1.mid == 1)
    assert(m1.organiser == 'See')
    assert(m1.start == '13:00')
    assert(m1.end == '15:00')

    print(m1)
    print(m2)

if __name__ == '__main__':
    main()
