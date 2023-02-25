from argparse import ArgumentParser
from domain import add, rm


if __name__ == '__main__':
    parser = ArgumentParser(prog='Task', description='Task taking')
    parser.add_argument('command', type=str)
    parser.add_argument('value', type=str)
    args = parser.parse_args()
    match args.command:
        case 'add':
            add(args.value)
        case 'rm':
            rm(int(args.value))
        case _:
            print('Invalid command!')
