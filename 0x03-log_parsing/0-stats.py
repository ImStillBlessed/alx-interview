#!/usr/bin/python3
"""
simple log parsing algorithm
"""
import sys
import signal
import re


total_file_size = 0
status_code_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_counter = 0


log_pattern = re.compile(
    r'^\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
)


def print_stats():
    """Prints the statistics collected so far"""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")


def signal_handler(sig, frame):
    """Handles the keyboard interruption signal"""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    while True:
        line = sys.stdin.readline()
        match = log_pattern.match(line)
        if not match:
            continue
        try:
            status_code = int(match.group(1))
            file_size = int(match.group(2))

            total_file_size += file_size
            if status_code in status_code_count:
                status_code_count[status_code] += 1
            line_counter += 1

            if line_counter % 10 == 0:
                print_stats()

        except (ValueError, IndexError):
            continue

    print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
