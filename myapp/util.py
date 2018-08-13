# -*- coding: utf-8 -*-
from geoip import geolite2
import json
import os

WORDS = []


def get_user_info(request):
    # get user ip address
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # WARNING: this code work correctly only on the server. If you run app localy - you get
    # wrong (local) ip address: "127.0.0.1"
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    data = {
        'ip': ip,
        'browser': request.user_agent.browser.family + ' ' + request.user_agent.browser.version_string,
        'oc': request.user_agent.os.family + ' ' + request.user_agent.os.version_string,
        'device': request.user_agent.device.family
    }

    try:
        match = geolite2.lookup(str(ip))
        data['timezone'] = match.timezone
        data['country'] = match.get_info_dict()['country']['names']['en']
        data['city'] = match.get_info_dict()['city']['names']['en']
    except AttributeError:
        data['country'] = None
        data['timezone'] = None
        data['city'] = None

    if request.COOKIES:
        cookies = []
        for cookie in request.COOKIES:
            cookies.append(cookie)
        data['cookies'] = cookies

    return data


def write_to_json(data):
    file_path= os.path.abspath(os.curdir) + '/media/files/hashes.json'
    with open(file_path, 'w') as fp:
        json.dump(data, fp)
    return file_path
