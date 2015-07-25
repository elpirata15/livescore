#!/usr/bin/env python

# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests


def get_live_score():
    r = requests.get('http://www.livescore.com/soccer/england/premier-league/')
    soup = BeautifulSoup(r.text)

    _rows = soup.find_all(class_='row-gray')

    return _rows


if __name__ == '__main__':
    rows = get_live_score()
    print '\n'.join(map(lambda r: r.text, rows))
