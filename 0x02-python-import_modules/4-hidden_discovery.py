#!/usr/bin/python3
import hidden_4


def main():
    for aa in dir(hidden_4):
        if aa[0:2] != "__":
            print(aa)


if __name__ == "__main__":
    main()
