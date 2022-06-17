from add_on.find_data_path import *
from generate_template import *


programs = get_list_program()

for program in programs:
    assets = get_list_asset(program)
    for asset in assets:
        parts = get_list_part(program, asset)
        for part in parts:
            child_parts = get_list_child_part(program, asset, part)
            for child_part in child_parts:
                path, data_file = get_name_data_file(program, asset, part, child_part)
                if ('.bak' in data_file):
                    continue
                elif ('.json' in data_file):
                    generate_template(path, data_file)
                else: 
                    continue
