#!/usr/bin/env python3
from validate_email import validate_email
from argparse import ArgumentParser, RawDescriptionHelpFormatter
import sys

def ParseNames(inputFile,domainNames, outputFile):
    f = open(inputFile,'r')
    for line in f:
        line = line.replace(" ", ".")
        line = line.replace("'","-")
        line = line.rstrip('\n')
        if len(domainNames) == 1:
            line += domainNames[0]
            mail = validate_email(line, verify=True)
            if mail is True:
                print(line + " is valid")
                outputFile.write(line + " is valid\n")
            else:
                print(line + " is not valid")
                outputFile.write(line + " is not valid\n")
        else:
            for dom in domainNames:
                line += dom
                mail = validate_email(line, verify=True)
                if mail is True:
                    print(line + " is valid")
                    outputFile.write(line + " is valid\n")
                else:
                    print(line + " is not valid")
                    outputFile.write(line + " is not valid\n")

def MailOnly(inputFile, outputFile):
    f = open(inputFile, 'r')
    for line in f:
        line = line.rstrip('\n')
        mail = validate_email(line, verify=True)
        if mail is True:
            print(line + " is valid")
            outputFile.write(line + " is valid\n")
        else:
            print(line + " is not valid")
            outputFile.write(line + " is not valid\n")

def main():
    parser = ArgumentParser()

    parser.add_argument("--file","-f",dest='input_file',help="Input data file")
    parser.add_argument("--parse-names","-n", action="store_true", dest='name_parser',help="Parse names from file to e-mail addresses")
    parser.add_argument("--domains","-d",nargs='+',dest='domains',help="Specify domains to test")

    args = parser.parse_args()
    endFile = open("results",'w')

    if args.name_parser and args.domains:
        for i in range(len(args.domains)):
            args.domains[i] = "@" + str(args.domains[i])
        ParseNames(args.input_file,args.domains,endFile)
    elif args.input_file:
        MailOnly(args.input_file, endFile)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()