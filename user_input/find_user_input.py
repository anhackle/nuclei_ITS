from user_input.find_body_input import *
from user_input.find_get_input import *

# Determine whether request has Content-Type header
def determine_content_type(raw_request):
    headers = raw_request.split('\r\n')[0:-1]
    for header in headers:
        if ('Content-Type' in header):
            return header.split(':')[1].strip()
        else:
            continue
    return "No header"


# Replace all user input in body part to {{}}
def determine_body_data(raw_request, content_type):
    if (content_type == 'No header'):
        return raw_request
    else:
        if (content_type == 'application/x-www-form-urlencoded'):
            return traditional_post(raw_request)
        elif (content_type == 'application/json'):
            return json_post(raw_request)
    return raw_request


def find_user_input(raw_request):
    content_type = determine_content_type(raw_request)
    raw_request = determine_body_data(raw_request, content_type)
    raw_request = determine_get_parameter(raw_request)
    return raw_request