#!/usr/bin/python
from sys import argv
from os import listdir, getcwd, rename, mkdir, path

analyse_folder = argv[1] if len(argv) > 1 else getcwd()

if not analyse_folder.endswith('/'):
    analyse_folder = f"{analyse_folder}/"

picture_extensions = (".png", ".jpg", ".jpeg", ".svg")
doc_extensions = (".docx", ".xlsx", ".pdf", ".pptx", ".txt")
compresed_extension = (".zip", ".7z", ".rar")
dev_extensions = (".py", ".json", ".js", ".java")

folders = {
    "picture_folder": "/home/carandev/pictures/",
    "wallpaper_folder": "/home/carandev/wallpapers/",
    "doc_folder": "/home/carandev/documents/",
    "compresed_folder": "/home/carandev/compresed-files/",
    "dev_folder": "/home/carandev/dev-files/"
}

for folder in folders.values():
    if not path.exists(folder):
        mkdir(folder)

for file in listdir(analyse_folder):
    if file.endswith(picture_extensions):
        if file.startswith("wallhaven"):
            rename(f"{analyse_folder}{file}",
                   f"{folders['wallpaper_folder']}{file}")
        else:
            rename(f"{analyse_folder}{file}",
                   f"{folders['picture_folder']}{file}")

    elif file.endswith(doc_extensions):
        rename(f"{analyse_folder}{file}", f"{folders['doc_folder']}{file}")

    elif file.endswith(compresed_extension):
        rename(f"{analyse_folder}{file}",
               f"{folders['compresed_folder']}{file}")

    elif file.endswith(dev_extensions):
        rename(f"{analyse_folder}{file}", f"{folders['dev_folder']}{file}")
