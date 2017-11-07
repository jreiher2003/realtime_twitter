#!/usr/bin/env python

from datetime import datetime
import re
import sys

def mapper():

    pattern = '^([\d.]+) ([\w-]+) ([\w-]+) \[(.+)\] \"(.+)\" (\d{3}) (\d+)$'
    for line in sys.stdin:
        result = re.match(pattern, line)
        if result is None:
            continue
        time_str = result.group(4)

        # Need to convert to ordinal because we want to sort by day
        date = datetime.strptime(time_str.split(" ")[0], "%d/%b/%Y:%X")

        print("{}\t1".format(date.strftime("%Y-%m-%d")))

if __name__ == "__main__":
    mapper()