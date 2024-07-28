# Test project

## Problem Statement

Imagine a file in the following fixed format:

`<url><white_space><long value>`

e.g.

http://api.tech.com/item/121345 9

http://api.tech.com/item/122345 350

http://api.tech.com/item/123345 25

http://api.tech.com/item/124345 231

http://api.tech.com/item/125345 111


Write a program that reads from 'stdin' the absolute path of a file expected
to be in this format and outputs a list of the urls associated with the 10
largest values in the right-most column. For example, given the input data
above if the question were to output the 2 largest values the output would
be:

http://api.tech.com/item/122345

http://api.tech.com/item/124345

Your solution should take into account extremely large files.

## Comments:
> Read the assignment carefully

:white_check_mark:

> Use the programming language of your choice

python as my daily scripting language

> The program may use any recent stable version of the language, but
should compile / run using official binaries / runtime (such as Oracle
JDK or OpenJDK for Java)

python 3.11

> For any chosen language, only the standard included libraries may be
used.

:white_check_mark:

> Describe how to build and run your code, optionally including some
build or make file.

included [below](#build)

> If you make some assumptions or decisions about used algorithms, please
explain them briefly.

As we are taking into account extremely large files to process, we should avoid sorting all the data in memory, which results in an average complexity of `O(n log n)`.

Quick googling reveals that the Python standard library [heapq](https://docs.python.org/3.11/library/heapq.html) implements a heap queue algorithm, which is very suitable for our case as the smallest item in the heap is always `heap[0]`. This allows us to maintain a heap that is never larger than N (the number of top items, with a default of 10).

> Think about how to verify / test this application and include a
description or code.

Unit test is included.

Launched by the command [below](#test)

## Build

```bash
docker build -t test-app .
```

## Test

```bash
docker run -it --rm -v "$(pwd)":/app:ro test-app -m unittest discover tests
```

## Run
| Args | Required | Deafult |
|:----:|:--------:|:-------:|
|path_to_script|No|./process.py|
|path_to_file|No|./lines.txt|

```bash
docker run -it --rm -v "$(pwd)":/app:ro test-app ${path_to_script} ${path_to_file}
```

## Generate test data
By default `genearate.py` writes 10M lines to the `lines.txt` file.

```bash
docker run -it --rm -v "$(pwd)":/app: test-app genearate.py
```




<sub>A minute of self-bragging</sub>

<sub>Hoovering through my Github repos, I just sumbled over [another test exercise](https://github.com/kostyaplis/toptal-test) implemented a couple of years ago. Don't hesitate to take a look if you wish. It seems to be more suitable for an Infra Engineer position. Thanks!</sub>
