import argparse


DESCRIPTION = 'Compares two configuration files and shows a difference.'
HELP = 'set format of output'
FIRST_FILE = 'first_file'
SECOND_FILE = 'second_file'


def cli():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument(FIRST_FILE, type=str)
    parser.add_argument(SECOND_FILE, type=str)
    parser.add_argument('-f', '--format', type=str, default='stylish',
                        choices=['stylish', 'plain', 'json'],
                        help=HELP)
    return parser.parse_args()
