#!/usr/bin/env python

import datetime
import sys
import blinkt

# Color defaults to red unless otherwise specified. Colors are set at a given time
# of day and last until changed (or midnight when the default resumes)
# Script is designed to run via cron. Run as often as you want granularity for
# setting times. Since it takes virtually no time, running at minute intervals is
# not problematic as long as cron doesn't email you for each run

now = datetime.datetime.now()

red = (16, 0, 0)
green = (0, 16, 0)
blue = (0, 0, 16)

# Set times at which to set a color.
sunday = [
{'time': now.replace(hour=6, minute=30), 'color':green},
{'time': now.replace(hour=18, minute=30), 'color':red},
]

monday = [
{'time': now.replace(hour=6, minute=30), 'color':green},
{'time': now.replace(hour=18, minute=30), 'color':red},
]

tuesday = [
{'time': now.replace(hour=6, minute=30), 'color':green},
{'time': now.replace(hour=18, minute=0), 'color':red},
]

wednesday = [
{'time': now.replace(hour=6, minute=30), 'color':green},
{'time': now.replace(hour=18, minute=30), 'color':red},
]

thursday = [
{'time': now.replace(hour=6, minute=30), 'color':green},
{'time': now.replace(hour=18, minute=0), 'color':red},
]

friday = [
{'time': now.replace(hour=6, minute=30), 'color':green},
{'time': now.replace(hour=18, minute=30), 'color':red},
]

saturday = [
{'time': now.replace(hour=6, minute=30), 'color':green},
{'time': now.replace(hour=18, minute=30), 'color':red},
]

program = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]

def main():
	color = red
	blinkt.set_clear_on_exit(False)
	for time in program[now.weekday()]:
		if time['time'] <= now:
			color = time['color']
			# print("Color: %s" % color)
	if color:
		blinkt.set_all(color[0], color[1], color[2])
		blinkt.show()


if __name__ == '__main__':
	main()
