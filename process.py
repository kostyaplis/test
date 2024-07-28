import os
import argparse
import logging
import logging.config
from heapq import heappush, heappushpop

# Why don't I just use print for a single log line?
logging.config.fileConfig(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "logger.conf")
)
logger = logging.getLogger()


def get_top_lines(file_path: str, n: int) -> list:
    """
    Reads a file containing lines with URLs and associated values, and returns a list of URLs associated with the top 'n' largest values.

    Args:
        file_path (str): The absolute path to the input file.
        n (int): The number of top lines to retrieve based on the largest values.

    Returns:
        list: A list of URLs corresponding to the top 'n' largest values.
    """
    heap = []
    position = 1
    with open(file_path, "r") as file:
        # Read the file by line
        for line in file:
            # Split the line into URL and value parts
            line_split = line.split()
            url = line_split[0]
            try:
                value = int(line_split[1])
            # Just to be safe
            except ValueError:
                logger.warning(f"Invalid value in line: {line}")
                continue

            # We can ensure FIFO order by using the line position in the file as a tie-breaker
            item = (value, -position, url)

            if len(heap) <= n - 1:
                # Push an item to the heap
                heappush(heap, item)
            else:
                # If the heap size is going to exeed n, push an item and pop the smallest value
                heappushpop(heap, item)
            position += 1

    # Sort the heap in descending order
    heap.sort(reverse=True)
    return [url for _, _, url in heap]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="Specify the path to the file", type=str)
    args = parser.parse_args()

    top_lines = get_top_lines(file_path=args.file_path, n=10)

    # Print the top URLs
    for line in top_lines:
        print(line)


if __name__ == "__main__":
    main()
