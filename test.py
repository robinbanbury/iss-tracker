#! /usr/bin/env python3

# pylint:disable=all

import datetime
import requests
from pprint import pprint

ip_data = requests.get('https://ipinfo.io').json()
lat, lon = ip_data['loc'].split(',')
print(lat, lon)

pass_data = requests.get(
    'http://api.open-notify.org/iss-pass.json?lat={}&lon={}'.format(lat, lon)).json()
pprint(pass_data)

