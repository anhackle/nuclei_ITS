import os

BASE_PATH = '/home/anhackle/target'

def get_list_program():
    return os.listdir(BASE_PATH)

def get_list_asset(program):
    return os.listdir(BASE_PATH + f"/{program}")

def get_list_part(program, asset):
    return os.listdir(BASE_PATH + F"/{program}/{asset}")

def get_list_child_part(program, asset, part):
    return os.listdir(BASE_PATH + f"/{program}/{asset}/{part}")

def get_name_data_file(program, asset, part, child_part):
    path = BASE_PATH + f"/{program}/{asset}/{part}/{child_part}"
    return path, os.listdir(path)[0]
