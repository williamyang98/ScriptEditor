import os
import argparse

from script_parser import parse_lines

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dir")

    args = parser.parse_args()

    with open(args.dir, "r") as file:
        parse_lines(file.readlines())

if __name__ == '__main__':
    main()