import json
import xml.etree.ElementTree as ET

def traditional_post(raw_request):
    lines = raw_request.split('\r\n')
    # all_lines[0] = GET /login?username=abc&password=abc HTTP/1.1
    parameters = lines[-1].split('&')

    for id, parameter in zip(range(len(parameters)), parameters):
        parameters[id] = parameter[:parameter.find('=') + 1] + "{{fuzz}}"

    lines[-1] = '&'.join(parameters)
    raw_request = '\r\n'.join(lines)

    return raw_request

def json_post(raw_request):
    return raw_request