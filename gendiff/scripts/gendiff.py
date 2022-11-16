#!/usr/bin/env python3

import argparse
from gendiff.generate_diff import generate_diff

desc = 'Compares two configuration files and shows a difference.'


def main():
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str, default='stylish',
                        choices=['stylish', 'plain', 'json'],
                        help='set format of output')
    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file, args.format)
    print('result:')
    print(diff)


if __name__ == '__main__':
    main()
