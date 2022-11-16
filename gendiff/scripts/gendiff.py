#!/usr/bin/env python3

from gendiff.generate_diff import generate_diff
from gendiff.cli import cli


def main():
    args = cli()
    diff = generate_diff(args.first_file, args.second_file, args.format)

    print(diff)


if __name__ == '__main__':
    main()
