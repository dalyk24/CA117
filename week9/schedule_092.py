#!/usr/bin/env python3

class Meeting(object):
	def __init__(self, hour, minute, duration):
		self.hour = hour
		self.minute = minute
		self.duration = duration

	def __str__(self):
		return '{:02d}:{:02d} ({:d} minutes)'.format(self.hour, self.minute, self.duration)

class Schedule(object):
	def __init__(self):
		self.d = {}

	def add(self, m):
		self.d[m.hour] = m

	def __str__(self):
		lines = []
		lines.append('Schedule')
		lines.append('--------')
		for k, v in sorted(self.d.items()):
			lines.append('{}'.format(v))
		lines.append('Meetings today: {:d}'.format(len(self.d)))
		return '\n'.join(lines)

from schedule_092 import Meeting, Schedule

def main():
    schedule = Schedule()

    m = Meeting(13, 0, 15)
    schedule.add(m)

    m = Meeting(9, 5, 30)
    schedule.add(m)

    m = Meeting(16, 30, 5)
    schedule.add(m)

    print(schedule)

if __name__ == '__main__':
    main()
