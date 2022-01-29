#!/usr/bin/python
from time import sleep
from os import getcwd, scandir
from subprocess import check_output
from sys import argv

path = argv[1] if len(argv) > 1 else getcwd()

def main(path = getcwd()):
    while True:
        for img in scandir(path):
            command = f"feh --bg-fill {path}/{img.name}"
            if img.name.endswith(".jpg") or img.name.endswith(".png"):
                check_output(command, shell=True)
                sleep(300)

main(path)
