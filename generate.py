import random

# Number of lines to generate
num_lines = 10000000

# Range for random numbers
random_range = 10000000

with open("lines.txt", "w") as file:
    for _ in range(num_lines):
        line = f"http://api.tech.com/item/{random.randint(0, random_range)} {random.randint(0, random_range)}\n"
        file.write(line)

print(f"{num_lines} lines written to lines.txt")
