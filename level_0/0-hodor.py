#!/usr/bin/python3
"""
function to continually add input to form
uses requests: r.url, r.status_code, r.headers, r.text
"""
import requests
import time

url = 'http://54.221.6.249/level0.php'
headers = {'content-type': 'application/x-www-form-urlencoded'}
data = {
    'id': '123',
    'holdthedoor': 'submit',
    }
mission = "<td>\n123    </td>\n    <td>\n1024    </td>"

r = requests.get(url, params=data)
while mission not in r.text:
    r = requests.post(url, data=data, headers=headers)
    time.sleep(2)
