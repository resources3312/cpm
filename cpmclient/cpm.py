import requests
import sys
import os
from termcolor import colored
from subprocess import getoutput


def man_page():
    print(f"""

CPM v1.0

Coded by: ViCoder32

C-Package-Manager, or CPM is most badly package manager for C libraries, 
which was written on Python ironic isn`t?) Maybe my little project will useful
for people, which want understand how work package manager on simple example.
Course, pm how apt or pacman much more difficult than my dwarf, but the principle
is the same. You can run CPM server, and choose need cpm server via client. Also
you can add you own library for one command, read man page.. In general, 
have fun :>>


Command:
        -h --help
            Print man page in terminal

        
        install <package> 
            Run cpm server with options

        connect <ServerAddress>
            Connect to CPM server, you can do this if edit config, 
            but is most simple and quick way

        stop 
            Stop cpm server if him already running


        list <package>
            Print all packages which have on your machine or check
            exist of package

        add <filename>
            Add your own package on cpm server. Accept add only .h files,
            even not try send other files

         
        remove <package>
            Remove package on your machine. But please, not need remove 
            libs how unistd.h or stdio.h or?)



          """)


def parse_argument(key):
    try: 
        index = sys.argv.index(key) + 1
        option = sys.argv[index]
        return option
    
    except:
        return None




def show_packages():
    out = getoutput("ls /usr/include/").split()
    raw = [i for i in out if i.endswith(".h")]
    data = ' \t\n\t'.join(raw)
    result = colored(f"Package list: \n {data}", 'green')
    return result

        


def check_input_file(filename):
    artifact = ["#include", "#define", "#ifdef", "#elif", "#endif", "defined"]
    if filename.endswith(".h"):
        with open(filename, "r") as f:
            raw = f.read()
            for i in range(len(artifact)):
                if raw.find(artifact[i]) != -1: 
                    return True

        
            return False
    



def argument_handler():
    if len(sys.argv) < 2:
        man_page()
    if "--help" in sys.argv:
        man_page()
    if sys.argv[1] == "install":
        pass 

    if sys.argv[1] == "remove":
        pass
    if sys.argv[1] == "list":
        package_name = parse_argument("list")
        if package_name == None:
            packs = show_packages() 
            print(packs)
        else:
            packs = show_packages()
            if package_name in packs:
                sys.exit(colored(f"Package was found: {package_name}" ,"green"))
            else:
                sys.exit(colored(f"Package not found..", "red"))
    
    if sys.argv[1] == "add":
        option = parse_argument("add")
        
        if check_input_file(option) == True:
            #upload_package(option)
            print(colored(f"Package {option} was added in repository" ,"green"))
        else:
            edit = option.split(".")[0] + ".h"    
            print(colored(f"FileError: Invalid package, check you file, and try again.." ,"red"))
            print(colored(f"Note: Accept add only .h files, if your file is library rename file: \n {option} => {edit}" ,"yellow"))
    else:
        sys.exit()


def main():
    argument_handler()

if __name__ == '__main__':
    main()
