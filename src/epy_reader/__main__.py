import curses
import multiprocessing
import sys

import epy_reader.cli as cli
import epy_reader.reader as reader


def main():
    # On Windows, calling this method is necessary
    # On Linux/OSX, this method does nothing
    multiprocessing.freeze_support()
    filepath, dump_only, scale_times = cli.find_file()
    if dump_only:
        sys.exit(cli.dump_ebook_content(filepath, scale_times))

    while True:
        try:
            filepath = curses.wrapper(reader.start_reading, filepath, scale_times)
        except curses.error as e:
            pass


# https://setuptools.pypa.io/en/latest/userguide/entry_point.html
if __name__ == "__main__":
    main()
