from add_on.find_data_path import *
from add_on.find_data_path import get_list_child_part
from add_on.find_data_path import get_name_data_file
from generate_template import *


programs = get_list_program()

for program in programs:
    parts = get_list_part(program)
    for part in parts:
        child_parts = get_list_child_part(program, part)
        for child_part in child_parts:
            path, data_file = get_name_data_file(program, part, child_part)
            if ('.json' in data_file):
                generate_template(path, data_file)
            else: 
                continue
