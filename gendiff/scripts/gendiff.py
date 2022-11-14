#!/usr/bin/env python3

import argparse
from gendiff.generate_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str, help='set format of output')
    args = vars(parser.parse_args())

    print('args', args)

    diff = generate_diff(args["first_file"], args["second_file"])
    print(diff)


if __name__ == '__main__':
    main()
