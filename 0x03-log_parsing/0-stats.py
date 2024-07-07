#!/usr/bin/python3
import sys
import signal

total_size = 0
status_counts = {}
line_count = 0

def print_stats():
    print("File size: {}".format(total_size))
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print("{}: {}".format(status, status_counts[status]))

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

valid_status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

for line in sys.stdin:
    parts = line.split()
    if len(parts) < 7:
        continue
    try:
        file_size = int(parts[-1])
        status_code = int(parts[-2])
        if status_code not in valid_status_codes:
            continue
    except ValueError:
        continue

    total_size += file_size
    if status_code not in status_counts:
        status_counts[status_code] = 0
    status_counts[status_code] += 1

    line_count += 1
    if line_count % 10 == 0:
        print_stats()
