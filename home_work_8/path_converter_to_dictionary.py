"""
The module takes the path to the folder and returns a list
of dictionaries with information about subfolders and files
"""

import os
from pathlib import Path


def directory_bypass(p):
    tree = os.walk(p)
    ls = []
    for i in tree:
        ls.append(i)

    lst = []
    dir_size = {}
    for i in reversed(ls):
        f = {}
        size_f = 0
        size_d = 0

        for j in i[2]:
            s = os.path.getsize(i[0] + '/' + j)
            f = {'name': Path(j).name, 'type': 'file', 'parent': Path(i[0]).name, 'size': s}
            size_f += s
            lst.append(f)
        dir_size[str(Path(i[0]))] = size_f

        for j in i[1]:
            if str(Path(i[0])) + '/' + j in dir_size:
                size_d += dir_size[str(Path(i[0])) + '/' + j]

        d = {'name': Path(i[0]).name, 'type': 'directory', 'parent': Path(str(Path(i[0])).replace(Path(i[0]).name, '')).name,
             'size': size_f + size_d}
        lst.append(d)
    return lst
