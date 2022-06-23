import json
import xml.etree.ElementTree as ET

# json_post coding
def item_generator(json_input):
    if isinstance(json_input, dict):
        if(len(json_input)) == 0:
            json_input.update({"key":"{{fuzz}}"})
        for k, v in json_input.items():
            if isinstance(v, (list, dict)):
                item_generator(v)    
            else:          
                json_input[k] = "{{fuzz}}"
    
    elif isinstance(json_input, (list)):
        if(len(json_input)) == 0:
            json_input.append("{{fuzz}}")
        for item in json_input:
            if isinstance(item, (list, dict)):
                item_generator(item) # recursive
            else:
                i = json_input.index(item) # check idex
                json_input[i] = "{{fuzz}}" # other type
    return json_input

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
    newline = '\r\n'
    req = raw_request.split(newline)
    _header = newline.join(req[0:-2])
    _body = req[-1]
    try:
        dict_input = json.loads(_body)
        item_generator(dict_input)
        str_input = json.dumps(dict_input)
        raw_request = _header + newline * 2 + str_input
    except:
        pass
    return raw_request