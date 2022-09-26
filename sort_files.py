#!/usr/bin/python
from sys import argv
from os import listdir, getcwd, rename, mkdir, path

analyse_folder = argv[1] if len(argv) > 1 else getcwd()

picture_extensions = (".png", ".jpg", ".jpeg", ".svg")
picture_folder = "/home/carandev/pictures/"
wallpaper_folder = "/home/carandev/wallpapers/"

if not path.exists(picture_folder):
    mkdir(picture_folder)

elif not path.exists(wallpaper_folder):
    mkdir(wallpaper_folder)

for file in listdir(analyse_folder):
    if file.endswith(picture_extensions):
        if file.startswith("wallhaven"):
            rename(f"{analyse_folder}{file}", f"{wallpaper_folder}{file}")
        else:
            rename(f"{analyse_folder}{file}", f"{picture_folder}{file}")