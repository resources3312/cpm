#! /usr/bin/python
from subprocess import getoutput
from termcolor import colored
def check_list():
    out = getoutput("python cpm.py list")
    if "Package" in out:
        out = getoutput("python cpm.py list stdio.h")
        if "found" in out:
            print(colored("[INFO] Success, package list working correctly" ,"yellow"))
            return True
        else:
            return False
    else:
        print(colored("[ERROR] Error, package list not working.." ,"red"))
        return False

def check_help():
    out = getoutput("python cpm.py --help")
    if ":>>" in out:
        print(colored("[INFO] Success, man page working correctly" ,"yellow"))
        return True        
    else:
        print(colored("[ERROR] Error, package man page not working.." ,"red"))
        return False

def output():
    num = []
    if check_list() == True:
        num.append("list")
    elif check_help() == True:
        num.append("help")
    tests = len(num)
    print(colored(f"{tests}/2 passed", "green"))
    
def main():
    output()
if __name__ == '__main__':
    main()

    
   

