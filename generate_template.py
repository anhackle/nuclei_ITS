import xml.etree.ElementTree as ET
import base64
import json

LIST_REQUESTS = []
BASE_DUPLICATE = []
EXTENSIONS = ['svg', 'js', 'map', 'css', 'gif', 'jpg', '.ico']
DATA_FILE = 'data.json'

def decode_base64(base64text):
    return base64.b64decode(base64text.encode('utf-8')).decode('utf-8')

def parse_json_burpsuite():
    with open(DATA_FILE, 'r') as f:
        requests = json.load(f)
        for request in requests:
            LIST_REQUESTS.append(decode_base64(request['request']))

    return list(set(LIST_REQUESTS))

def filter_extension(raw_request):
    line = raw_request.split('\r\n')[0]
    path = line.split(' ')

    for extension in EXTENSIONS:
        if extension in path[1]:
            return True

    return False

def delete_duplicate_request(LIST_REQUESTS):
    result = []

    for request in LIST_REQUESTS:
        method_and_path = request.split('\r\n')[0].split(' ')[:2]

        if (method_and_path not in BASE_DUPLICATE):
            BASE_DUPLICATE.append(method_and_path)
            result.append(request)

    return result
    
def generate_template():
    # Parse base64 json from burpsutie
    requests = parse_json_burpsuite()
    # Delete duplicate requests based on mtehod + path
    requests = delete_duplicate_request(requests)

    for id, request in zip(range(100),requests):
        request = request.replace('\r\n', '\r\n        ')
        # Delete front-end request like js, svg, map,...
        if filter_extension(request):
            continue
        
        # Generate template from base template
        with open('base_template.yaml', 'r') as f:
            base_template = f.read()
            template = base_template.format(raw_request = request)
            with open(f"templates/{id}.yaml", 'w') as f1:
                f1.write(template)


generate_template()

