import argparse
from math import ceil, floor, log


parser = argparse.ArgumentParser()

parser.add_argument('--type', choices=['annuity', 'diff'])
parser.add_argument('--payment')
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--interest')

args = parser.parse_args()

if args.type == 'annuity':
    if args.principal and args.periods and args.interest:
        p = int(args.principal)
        n = int(args.periods)
        i = float(args.interest) / (12 * 100)

        a = ceil((p * ((i * (pow(1 + i, n))) / (pow(1 + i, n) - 1))))
        print(f'Your monthly payment = {a}!')
    elif args.payment and args.periods and args.interest:
        a = int(args.payment)
        n = int(args.periods)
        i = float(args.interest) / (12 * 100)

        p = floor(a / ((i * (pow(1 + i, n))) / (pow(1 + i, n) - 1)))
        print(f'Your loan principal = {p}!')

        overpay = ceil((p * ((i * (pow(1 + i, n))) / (pow(1 + i, n) - 1))))
        print('Overpayment =', overpay * n - p)
    elif args.principal and args.payment and args.interest:
        p = int(args.principal)
        a = int(args.payment)
        i = float(args.interest) / (12 * 100)

        argument = a / (a - i * p)
        n = ceil(log(argument, 1 + i))

        if n % 12 == 0:
            print(f'It will take {n // 12} years to repay this loan!')
        else:
            print(f'It will take {n // 12} years and {n % 12} '
                  f'months to repay this loan!')

        overpay = ceil((p * ((i * (pow(1 + i, n))) / (pow(1 + i, n) - 1))))
        print('Overpayment =', a * n - p)
    else:
        print('Incorrect parameters')
elif args.type == 'diff':
    if args.principal and args.periods and args.interest:
        p = int(args.principal)
        n = int(args.periods)
        i = float(args.interest) / (12 * 100)

        result = 0
        for m in range(1, int(args.periods) + 1):
            d = p / n + i * (p - ((p * (m - 1)) / n))
            print(f'Month {m}: payment is {ceil(d)}')
            result += ceil(d)

        print('')
        print('Overpayment =', result - p)
    else:
        print('Incorrect parameters')
else:
    print('Incorrect parameters')
