#!/usr/bin/env python

from datetime import datetime
import sys

def reducer():

	count = 0
	old_day = None
	dayOfWeek = {}
	for line in sys.stdin:
		data = line.strip().split("\t")
		if len(data) != 2:
			continue

		day, hits = data
        if old_day and old_day != day:
            print old_day, "\t", count
            old_day = day
            count = 0

        old_day = day
        count += float(hits)


if __name__ == "__main__":
	reducer()