import os
import json
import argparse

from script_parser import parse_lines
from models import JSONSerialiser

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dir")

    args = parser.parse_args()

    with open(args.dir, "r") as file:
        labels = parse_lines(file.readlines())

    serialiser = JSONSerialiser()
    data = [label.accept(serialiser) for label in labels]
    pass



if __name__ == '__main__':
    main()