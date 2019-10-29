#!/usr/bin/python3
#Usage: mail_validator.py <file name> <domain>
from validate_email import validate_email
import sys


def main():

    f = open(str(sys.argv[1]), 'r')
    endFile = open("results",'w')

    for line in f:
        line = line.rstrip('\n')
        mail = validate_email(line, verify=True,)
        if mail is True:
            print(line + " is valid")
            endFile.write(line + " is valid\n")
        else:
            print(line + " is not valid")
            endFile.write(line + " is not valid\n")


if __name__ == "__main__":

    main()