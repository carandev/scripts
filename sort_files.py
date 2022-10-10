#!/usr/bin/python
from sys import argv
from os import listdir, getcwd, rename, mkdir, path

analyse_folder = argv[1] if len(argv) > 1 else getcwd()

if not analyse_folder.endswith('/'):
    analyse_folder = f"{analyse_folder}/"

picture_extensions = (".png", ".jpg", ".jpeg", ".svg")
doc_extensions = (".docx", ".xlsx", ".pdf", ".pptx", ".txt")
compresed_extension = (".zip", ".7z", ".rar")

picture_folder = "/home/carandev/pictures/"
wallpaper_folder = "/home/carandev/wallpapers/"
doc_folder = "/home/carandev/documents/"
compresed_folder = "/home/carandev/compresed-files/"

if not path.exists(picture_folder):
    mkdir(picture_folder)

elif not path.exists(wallpaper_folder):
    mkdir(wallpaper_folder)

elif not path.exists(doc_folder):
    mkdir(doc_folder)

elif not path.exists(compresed_folder):
    mkdir(compresed_folder)

for file in listdir(analyse_folder):
    if file.endswith(picture_extensions):
        if file.startswith("wallhaven"):
            rename(f"{analyse_folder}{file}", f"{wallpaper_folder}{file}")
        else:
            rename(f"{analyse_folder}{file}", f"{picture_folder}{file}")

    elif file.endswith(doc_extensions):
        rename(f"{analyse_folder}{file}", f"{doc_folder}{file}")

    elif file.endswith(compresed_extension):
        rename(f"{analyse_folder}{file}", f"{compresed_folder}{file}")
