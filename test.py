#! /usr/bin/env python3

# pylint:disable=all

import requests

ip_data = requests.get('https://ipinfo.io').json()
lat, lon = ip_data['loc'].split(',')
print(lat, lon)
