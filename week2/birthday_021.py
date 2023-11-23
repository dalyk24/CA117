#!/usr/bin/env python3

import sys
import calendar

poetry = ["Monday's child is fair of face.",
	"Tuesday's child is full of grace.",
	"Wednesday's child is full of woe.",
	"Thursday's child has far to go.",
	"Friday's child is loving and giving.",
	"Saturday's child works hard for a living.",
	"Sunday's child is fair and wise and good in every way."]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def dates(date):
	date = date.split()
	return calendar.weekday(int(date[2]), int(date[1]), int(date[0]))

for date in sys.stdin.readlines():
	weekday = dates(date)
	print("You were born on a " + days[weekday] + " and " + poetry[weekday])
