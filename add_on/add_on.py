import base64
import json

LIST_REQUESTS = []
BASE_DUPLICATE = []
EXTENSIONS = ['svg', 'js', 'map', 'css', 'gif', 'jpg', '.ico']

def decode_base64(base64text):
    return base64.b64decode(base64text.encode('utf-8')).decode('utf-8')


def parse_json_burpsuite(data_file):
    with open(data_file, 'r') as f:
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