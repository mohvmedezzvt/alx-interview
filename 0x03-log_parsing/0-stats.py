#!/usr/bin/python3
"""Log parsing"""

import sys

if __name__ == "__main__":
    filesize = 0
    count = 0
    stats = {"200": 0, "301": 0, "400": 0, "401": 0,
             "403": 0, "404": 0, "405": 0, "500": 0}

    def print_stats(stats: dict, file_size: int):
        """Prints the stats"""
        print("File size: {}".format(file_size))
        for key, value in sorted(stats.items()):
            if value:
                print("{}: {}".format(key, value))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass
            try:
                filesize += int(data[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                print_stats(stats, filesize)
        print_stats(stats, filesize)
    except KeyboardInterrupt:
        print_stats(stats, filesize)
        raise
