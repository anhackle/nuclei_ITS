from user_input.find_user_input import *
from add_on.add_on import *
import os
import platform
from datetime import date


VULNERABILITIES = []
CONTENT_TYPE = ['application/json', 'application/xml', 'application/x-www-form-urlencoded', 'multipart/form-data']


def generate_template(path, data_file): # /target/paypal/non_authentication/1/
    # Get current day
    current_day = date.today().strftime("%d-%m-%Y")

    # Parse base64 json from burpsutie
    file_name = f"{path}/{data_file}"
    requests = parse_json_burpsuite(file_name)

    # Rename after parsing 
    os.rename(file_name, f"{path}/{current_day}.json.bak")

    # Delete duplicate requests based on method + path
    requests = delete_duplicate_request(requests)

    # Delete front-end request like js, svg, map,...
    requests = filter_extension(requests)

    for id, request in zip(range(1,100),requests):
        # Find all user inputs in each request
        request = find_user_input(request)

        if (platform.system() == 'Windows'):
            request = request.replace('\r\n', '\r        ')
        else:
            request = request.replace('\r\n', '\r\n        ')
        
        # Generate template from base template
        for vuln in os.listdir('./vuln'):
            with open(f"./vuln/{vuln}/base_template.yaml", 'r') as f:
                base_template = f.read()
                template = base_template.format(raw_request = request)
                
                template_name = f"{current_day}_{id}_{vuln}"
                with open(f"{path}/{template_name}.yaml", 'w') as f1:
                    f1.write(template)
