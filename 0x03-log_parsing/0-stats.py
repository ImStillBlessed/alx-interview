#!/usr/bin/python3
"""
This script reads log lines from standard
input and computes statistics on file sizes and status codes.

Log line format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Metrics Computed:
1. Total file size.
2. Number of occurrences of specific status codes
(200, 301, 400, 401, 403, 404, 405, 500).

The script prints the metrics after every 10 lines
processed or when interrupted by a keyboard signal (CTRL+C).

Usage:
    ./0-generator.py | ./0-stats.py
"""

import sys
import re
from collections import defaultdict

# Regular expression to match the log line format
log_pattern = re.compile(
    r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] '
    r'"GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
)

# Initialize metrics
total_size = 0
status_counts = defaultdict(int)
line_count = 0


def print_metrics():
    """
    Print the accumulated metrics:
    - Total file size.
    - Number of occurrences of each status code.

    The status codes are printed in ascending order.
    """
    global total_size, status_counts
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")


try:
    for line in sys.stdin:
        line = line.strip()
        match = log_pattern.match(line)

        if match:
            status_code = match.group(3)
            file_size = match.group(4)

            try:
                file_size = int(file_size)
            except ValueError:
                continue

            total_size += file_size
            status_counts[status_code] += 1
            line_count += 1

            if line_count % 10 == 0:
                print_metrics()

except KeyboardInterrupt:
    print_metrics()
