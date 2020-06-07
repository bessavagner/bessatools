import os


def mkdir(dirname, silent=False):
    if not os.path.exists(dirname):
        try:
            os.mkdir(dirname)
            print(f"Folder '{dirname}' was created.")
        except FileNotFoundError as err:
            print("Folder error: ", err)
    elif not silent:
        print(f"{dirname} already exists.")

def mkdirbase(dirname="newfolder", n=1, base=3, **kwargs):
    name = dirname + f"{n:0{base}d}"
    mkdir(name, **kwargs)

def rmdir(dirname="newfolder"):
    if os.path.exists(dirname):
        os.rmdir(dirname)

def dirlist(dirname="newfolder"):
    if os.path.exists(dirname):
        os.rmdir(dirname)
    else:
        print("{dirname} doesn't exist.")
        return None

