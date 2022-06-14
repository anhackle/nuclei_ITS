import pathlib
import os

BASE_PATH = '/home/target'

def get_list_program():
    return os.listdir(BASE_PATH)

def get_list_part(program):
    return os.listdir(BASE_PATH + f"/{program}")

def get_list_child_part(program, part):
    return os.listdir(BASE_PATH + f"/{program}/{part}")

def get_name_data_file(program, part, child_part):
    path = BASE_PATH + f"/{program}/{part}/{child_part}"
    return path, os.listdir(path)[0]
