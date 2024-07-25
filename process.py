import os
import argparse
import logging
import logging.config
from heapq import heappush, heappop

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

            # Push the Value, URL tuple to the heap
            heappush(heap, (value, url))

            # If the heap size exceeds n, pop the smallest value
            if len(heap) > n:
                heappop(heap)

    # Get URLs from the heap and sort by values in descending order
    top_lines = sorted(heap, key=lambda x: x[0], reverse=True)
    return [url for _, url in top_lines]


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
