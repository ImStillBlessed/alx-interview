#!/usr/bin/python3
"""
This module perfomrs a simple stdin manipulation
"""

import sys
import re
import signal

total_file_size = 0
status_codes = {
    200: 0, 
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0
pattern = re.compile(
    r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2} \+\d{4})\] "GET /projects/\d+ HTTP/1\.1" (\d{3}) (\d+)$'
)

def print_stats():
    """Function to print the current statistics"""
    print('File size: {}'.format(total_file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print('{}: {}'.format(code, status_codes[code]))

def signal_handler(sig, frame):
    """Handle keyboard interruption"""
    print_stats()
    print('done')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    match = pattern.match(line)

    if match:
        status_code = int(match.group(3))
        file_size = int(match.group(4))

        total_file_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1
        line_count += 1

    if line_count == 10:
        print_stats()
        line_count = 0

print_stats()
print('done')
