#!/usr/bin/env python3

import sys

inp = sys.stdin.readline().strip().split()
stops = {}
stops['floors'] = int(inp[0])
stops['start'] = int(inp[1])
stops['going'] = int(inp[2])
stops['up'] = int(inp[3])
stops['down'] = int(inp[4])

building = []
i = 1

while i <= stops['floors']:
    building.append(i)
    i += 1

def going_up(stops):
    journey = building[stops['start'] - 1:stops['going']:stops['up']]
    count = 0
    count += len(journey) - 1

    while journey[-1] > 0 and journey[-1] != stops['going']:
        journey[-1] -= stops['down']
        temp = journey[-1]
        count += 1
        temp_count = 0
        while temp < stops['floors']:
            temp += stops['up']
            temp_count += 1
            if temp == stops['going']:
                return count + temp_count

    if journey[-1] == stops['going']:
        return count
    return 'Sorry Sheila!'

def going_down(stops):
    journey = building[stops['going'] - 1:stops['start']:stops['down']]
    count = 0
    count += len(journey) - 1

    while journey[0] < stops['floors'] and journey[0] != stops['going']:
        journey[0] += stops['up']
        temp = journey[0]
        count += 1
        temp_count = 0
        while temp > 0:
            temp -= stops['down']
            temp_count += 1
            if temp == stops['going']:
                return count + temp_count

    if journey[0] == stops['going']:
        return count
    return 'Sorry Sheila!'

def zero_handler(stops):
    diff = stops['going'] - stops['start']

    if stops['up'] == 0 and stops['down'] != 0 and diff < 0:
        if diff % stops['down'] == 0:
            return diff // stops['down'] * -1
    elif stops['down'] == 0 and stops['up'] != 0 and diff > 0:
        if diff % stops['up'] == 0:
            return diff // stops['up']

    return 'Sorry Sheila!'

if stops['start'] == stops['going']:
    print(0)
elif stops['up'] == 0 or stops['down'] == 0:
    print(zero_handler(stops))
elif stops['start'] < stops['going']:
    print(going_up(stops))
elif stops['start'] > stops['going']:
    print(going_down(stops))
