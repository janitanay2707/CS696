import sys
import argparse

def compute(**kwargs):
    input = kwargs['input']
    if all(isinstance(item, int) for item in input) == False:
        print("input is not a list of integer!")
    else:
        if kwargs['action'] == 'sum':
            x = sum(input)
        if kwargs['action'] == 'mean':
            x = sum(input)/len(input)
        if kwargs.get('return_float',True):
            x = float(x)
    return x


if __name__== '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-m', '--multiply', help='', type=int)
    parser.add_argument('-s', '--sum', help='', action='store_true')
    parser.add_argument('remainder', help='', nargs=argparse.REMAINDER)

    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        sys.exit(1)



    if args.sum:
        print(sum([int(x) for x in args.remainder]))

    if args.multiply:
        for number in [int(x) for x in args.remainder]:
            print(number * args.multiply)


print(compute(input=[0,1,2,3], action = 'sum', return_float=True))