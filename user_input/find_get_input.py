# Replace all get parameter value to {{}}
def determine_get_parameter(raw_request):
    line = raw_request.split('\r\n')
    # line[0] = GET /login?username=abc&password=abc HTTP/1.1
    parts = line[0].split(' ')
    # parts[1] = /login?username=abc&password=abc
    path = parts[1].split('?')
    # path[1] = username=abc&password=abc
    if (len(path) == 1):
        return raw_request
    else:
        parameters = path[1].split('&')
        for id, parameter in zip(range(len(parameters)), parameters):
            parameters[id] = parameter[:parameter.find('=') + 1] + "{{fuzz}}" 

        path[1] = '&'.join(parameters) # userame={{fuzz}}&password={{fuzz}}
        parts[1] = '?'.join(path)
        line[0] = ' '.join(parts)
        raw_request = '\r\n'.join(line)

    return raw_request