import base64
import json

EXTENSIONS = ['svg', 'js', 'map', 'css', 'gif', 'jpg', '.ico']

def decode_base64(base64text):
    return base64.b64decode(base64text.encode('utf-8')).decode('latin1')


def parse_json_burpsuite(data_file):
    requests = []
    with open(data_file, 'r', encoding='latin1') as f:
        data = json.load(f)
        for request in data:
            #requests.append(decode_base64(request['request']))
            #requests.append(request['Request']['Headers'])
            requests.append(f"{request['Request']['Headers']}\r\n{request['Request']['Body']}")

    return list(set(requests))


def filter_extension(raw_request):
    line = raw_request.split('\r\n')[0]
    path = line.split(' ')

    for extension in EXTENSIONS:
        if extension in path[1]:
            return True

    return False


def delete_duplicate_request(requests):
    result = []
    BASE_DUPLICATE = []

    for request in requests:
        method_and_path = request.split('\r\n')[0].split(' ')[:2]

        if (method_and_path not in BASE_DUPLICATE):
            BASE_DUPLICATE.append(method_and_path)
            result.append(request)

    return result