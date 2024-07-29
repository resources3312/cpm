#! /usr/bin/python
import asyncio
import aiohttp
import sys
import os
from termcolor import colored
from subprocess import getoutput


def check_root():
    if os.getuid() != 0:
        sys.exit("Run cpmserver only as root..")

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

        start <mode>
            Start cpm server on your machine
            Modes:
                global - Ordinary start cpm server, nothing explain to here 

                local - Start cpm server in your local network for test or debug
                

        stop 
            Stop cpm server if he`s already running


        list <package_name>
            Print all packages which have on yout machine or check
            exist of package

        add <filename>
            Add your own package on cpm server. Accept add only .h files,
            we`re want`t to cpm server will destroy, besause on disk not place,
            isn`t?)

         
        remove <package>
            Remove package from cpm server, I think you know that you doing if you 
            host repository

          """)

def start_server(mode):
    if mode == "global":
        pass
        


    elif mode == "local":
        pass
        # Local start...
    else:
        man_page()



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
    if len(sys.argv) <= 1:
       sys.exit(man_page())
    

    if "--help" in sys.argv:
        man_page()
    

    elif sys.argv[1] == "start":
        option = parse_argument("start")
        start_server(option)

    elif sys.argv[1] == "stop":
        pass
        #stop_server()
    elif sys.argv[1] == "list":
        package_name = parse_argument("list")
        if package_name == None:
            packs = show_packages() 
            print(packs)
        else:
            packs = show_packages()
            if package_name in packs:
                sys.exit(colored(f"Package was found: {package_name}" ,"green"))
            else:
                sys.exit()
    
    elif sys.argv[1] == "add":
        option = parse_argument("add")
        
        if check_input_file(option) == True:
            os.system(f"cp {option} /usr/include/ ")   # I hate myself, it`s level of corp developers
            print(colored(f"Package {option} was added in repository" ,"green"))
        else:
            edit = option.split(".")[0] + ".h"    
            print(colored(f"FileError: Invalid package, check you file, and try again.." ,"red"))
            print(colored(f"Note: Accept add only .h files, if your file is library rename file: \n {option} => {edit}" ,"yellow"))
    else:
        sys.exit("Usage: cpmserver <option> <argument> \n For get man page use '--help'")

def main():
    check_root()
    argument_handler()

if __name__ == '__main__':
    main()
