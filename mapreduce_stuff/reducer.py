#!/usr/bin/env python

from datetime import datetime
import sys

def reducer():

	count = 0
	old_date = None
	for line in sys.stdin:
		data = line.strip().split("\t")
		if len(data) != 2:
			continue

		this_date, _ = data

		if old_date and old_date != this_date:
			# date_str = datetime.fromordinal(int(this_date)).date()
			weekday = datetime.strptime(this_date, '%Y-%m-%d %H:%M:%S').weekday()
			print("{}\t{}".format(weekday, count))

			count = 0
		old_date = this_date
		count += 1


if __name__ == "__main__":
	reducer()