#!/usr/bin/python3
import sys


def main():
    count = len(sys.argv)
    print('{:d} argument{:}'.format(count - 1, '.' if count == 1 else
                                    (':' if count == 2 else 's:')))
    ind = 1
    for arg in sys.argv[1:]:
        print("{:d}: {}".format(ind, arg))
        ind += 1


if __name__ == "__main__":
    main()
