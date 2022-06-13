from user_input.find_user_input import *
from add_on.add_on import *
import platform


VULNERABILITIES = []
CONTENT_TYPE = ['application/json', 'application/xml', 'application/x-www-form-urlencoded', 'multipart/form-data']


def generate_template(path, data_file): # /target/paypal/non_authentication/1/
    # Parse base64 json from burpsutie
    requests = parse_json_burpsuite(f"{path}/{data_file}")

    # Delete duplicate requests based on method + path
    requests = delete_duplicate_request(requests)

    for id, request in zip(range(100),requests):
        # Find all user inputs in each request
        request = find_user_input(request)

        if (platform.system == 'Windows'):
            request = request.replace('\r\n', '\r        ')
        else:
            request = request.replace('\r\n', '\r\n        ')

        # Delete front-end request like js, svg, map,...
        if filter_extension(request):
            continue
        
        # Generate template from base template
        with open('xss/base_template.yaml', 'r') as f:
            base_template = f.read()
            template = base_template.format(raw_request = request)
            with open(f"{path}/{id}.yaml", 'w') as f1:
                f1.write(template)
