from argparse import ArgumentParser
from domain import *
import sys


if __name__ == '__main__':
    parser = ArgumentParser(prog='Task', description='Task taking')
    parser.add_argument('command', type=str)
    match sys.argv[1]:
        case 'add':
            parser.add_argument('value', type=str)
        case 'rm':
            parser.add_argument('value', type=int)
    args = parser.parse_args()
    try:
        eval(f'{args.command}(args.value)')
    except AttributeError:
        eval(f'{args.command}()')
    except NameError:
        print('Invalid command')
