import xml.etree.ElementTree as ET
import base64
import json

LIST_REQUESTS = []
EXTENSIONS = ['svg', 'js', 'map', 'css', 'gif', 'jpg']

# def parse_xml_burpsuite():

#     tree = ET.parse('test.txt')
#     root = tree.getroot()

#     for child in root:
#         LIST_REQUESTS.append(child[8].text)
    
#     return LIST_REQUESTS

def parse_json_burpsuite():
    with open('data.json', 'r') as f:
        requests = json.load(f)
        for request in requests:
            LIST_REQUESTS.append(request['request'])
    return list(set(LIST_REQUESTS))

def decode_base64(base64text):
    return base64.b64decode(base64text.encode('utf-8')).decode('utf-8')

def filter_extension(raw_request):
    line = raw_request.split('\r\n')[0]
    path = line.split(' ')

    for extension in EXTENSIONS:
        if extension in path[1]:
            return True
    return False
    
def generate_template():
    requests = parse_json_burpsuite()

    for id, request in zip(range(100),requests):
        request_decoded = decode_base64(request).replace('\r\n', '\r\n        ')

        # Delete front-end request like js, svg, map,...
        if filter_extension(request_decoded):
            continue
        
        # Generate template from base template
        with open('base_template.yaml', 'r') as f:
            base_template = f.read()
            template = base_template.format(raw_request = request_decoded)
            with open(f"templates/{id}.yaml", 'w') as f1:
                f1.write(template)


generate_template()

