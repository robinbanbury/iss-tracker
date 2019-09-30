import requests
import time

while True:
    req = requests.get('http://api.open-notify.org/iss-now.json')

    if req.status_code == 200:
        # print(dir((req)))
        obj = req.json()
        lat = obj['iss_position']['latitude']
        lng = obj['iss_position']['longitude']
        print('ISS latitude: {}; ISS longitude: {}'.format(lat, lng))

    time.sleep(5)
