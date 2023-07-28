import os
from collections import namedtuple
from pathlib import Path


def directory_bypass(path):
    tree = os.walk(path)
    ls = []
    for i in tree:
        ls.append(i)

    My_tuple = namedtuple('My_tuple', ['name',
                                       'file_extension', 'type', 'parent'])
    list_object = []
    for i in reversed(ls):
        for j in i[2]:
            obj_file = My_tuple(Path(j).name, Path(j).suffixes, 'file', Path(i[0]).name)
            list_object.append(obj_file)
        obj_dir = My_tuple(Path(i[0]).name, 'None', 'directory', Path(i[0]).name)
        list_object.append(obj_dir)
    return list_object
