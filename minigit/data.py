import os
import hashlib

GIT_DIR = ".minigit"

def init():
    os.makedirs(GIT_DIR)
    os.makedirs(f'{GIT_DIR}/objects')

def hash_object(data, type_='blob'):
    __check_minigit_dir()
    obj = type_.encode() + b'\x00' + data #prepend the object type to each file followed by a NULL byte followed by the content
    oid = hashlib.sha1(obj).hexdigest()
    with open(f'{GIT_DIR}/objects/{oid}', 'wb') as out_file:
        out_file.write(obj)
    return oid


def get_object(oid, expected='blob'):
    with open(f'{GIT_DIR}/objects/{oid}', 'rb') as file:
        obj = file.read()

    type_, _, content = obj.partition(b'\x00')
    type_ = type_.decode()
    if expected is not None:
        assert type_ == expected, f'Expected {expected}, got {type_}'
    return content


def __check_minigit_dir():
    #check if a .minigit dir is present
    pass
