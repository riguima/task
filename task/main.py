from argparse import ArgumentParser
from domain import *


def run_command(args) -> None:
    if args.command in ['rm']:
        eval(f'{args.command}(int(args.value))')
    else:
        eval(f'{args.command}(args.value)')


if __name__ == '__main__':
    parser = ArgumentParser(prog='Task', description='Task taking')
    parser.add_argument('command', type=str)
    parser.add_argument('value')
    args = parser.parse_args()
    try:
        run_command(args)
    except NameError:
        print('Invalid command')
