#!/usr/bin/env python3

import os
import argparse
from gendiff.generate_diff import generate_diff

desc = 'Compares two configuration files and shows a difference.'


def main():
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str, help='set format of output')
    args = vars(parser.parse_args())

    # print(1, os.path.dirname(os.path.abspath(__file__)))
    # print(2, os.path.abspath(os.getcwd()))
    # print(3, os.path.join(os.path.abspath(os.getcwd()), args["first_file"]))

    diff = generate_diff(args["first_file"], args["second_file"])
    print(diff)


if __name__ == '__main__':
    main()
