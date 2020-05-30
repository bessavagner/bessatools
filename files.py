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
