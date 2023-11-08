#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""


import sys
import signal
from collections import defaultdict

# Define a dictionary to store status code counts
status_code_counts = defaultdict(int)
total_file_size = 0
line_count = 0

# Define a signal handler to print the statistics on CTRL+C
def print_statistics(sig, frame):
    print("Total file size:", total_file_size)
    for status_code in sorted(status_code_counts.keys()):
        print(f"{status_code}: {status_code_counts[status_code]}")
    sys.exit(0)

# Register the signal handler for CTRL+C
signal.signal(signal.SIGINT, print_statistics)

try:
    for line in sys.stdin:
        line = line.strip()
        if line:
            parts = line.split()
            if len(parts) >= 8:
                status_code = parts[7]
                total_file_size += int(parts[-1])
                status_code_counts[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_statistics(None, None)
except KeyboardInterrupt:
    # Handle CTRL+C without printing statistics
    pass

