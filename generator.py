import os
import sys


def print_dir(directory):
    for file in os.listdir(directory):
        print(file)

def full_dir(dir):
    for root, dir, file in os.walk(dir):
        for name in file:
            print(os.path.join(root,name))
        for name in dir:
            print(os.path.join(root,name))

if __name__=="__main__":
    directory = "test"
    full_dir(directory)