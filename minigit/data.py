import os
import hashlib

GIT_DIR = ".minigit"

def init():
    os.makedirs(GIT_DIR)
    os.makedirs(f'{GIT_DIR}/objects')

def hash_object(data):
    __check_minigit_dir()
    oid = hashlib.sha1(data).hexdigest()
    print("oid is: ", oid)
    print(f'{GIT_DIR}(objects/{oid})')
    with open(f'{GIT_DIR}/objects/{oid}', 'wb') as out_file:
        out_file.write(data)
    return oid


def get_object(oid):
    with open(f'{GIT_DIR}/objects/{oid}', 'rb') as file:
        return file.read()


def __check_minigit_dir():
    #check if a .minigit dir is present
    pass
