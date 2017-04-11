#!/usr/bin/python


"""
| ~~~~~~~~~~~~~~~~~~~~~~~~ | ~~~~~~~~~~~~~~~~~~~ |
| Built By Boris Bakshiyev |       v1.1          |
| ~~~~~~~~~~~~~~~~~~~~~~~~ | ~~~~~~~~~~~~~~~~~~~ |
"""

import os, argparse

parser = argparse.ArgumentParser()
parser.add_argument("--service", required=True)
parser.add_argument("--cpu", required=False,action='store_true')
parser.add_argument("--ram", required=False,action='store_true')
args = parser.parse_args()


def main():
    temp = 'top -b -n 6 -d 1 | grep ' + args.service + '> service.txt'
    os.system( temp )
    check = open ('service.txt' ,'r')
    lines = check.read().split('\n')
    if senity_check() == 2:
        if not args.ram:
            if not args.cpu:
                check_all(lines,check)
            else:
                check_cpu(lines,check)
        else:
            check_ram(lines,check)
    else:
        close_file(check)
        exit

def senity_check():
    if os.stat("service.txt").st_size == 0:
        print "The service name wrong or the service arent running"
        return 1
    else:
        return 2


def check_all(lines,check):
    sum1 = 0
    sum2 = 0
    for line in lines:
        word = line.split()
        if not word:
            pass
        else:
            sum1 += float(word[8])
            sum2 += float(word[9])
    print sum1/(len(lines)-1),sum2/(len(lines)-1)
    close_file(check)


def check_cpu(lines,check):
    cpu = 0
    for line in lines:
        word = line.split()
        if not word:
            pass
        else:
            cpu += float(word[8])
    print cpu/(len(lines)-1)
    close_file(check)


def check_ram(lines,check):
    ram = 0
    for line in lines:
        word = line.split()
        if not word:
            pass
        else:
            ram += float(word[8])
    print ram/(len(lines)-1)
    close_file(check)


def close_file(check):
    check.close()
    os.system('rm -rf service.txt')

if __name__ == "__main__":
    main()
