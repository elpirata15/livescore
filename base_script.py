# -*- coding:utf-8 -*-
import datetime

from bs4 import BeautifulSoup
import requests


class LiveScore(object):
    def __init__(self):
        pass
        
    def get(self, team=''):
        now = datetime.datetime.now().strftime("%Y%m%d %H%M%S")
    
        r = requests.get('http://www.livescore.co.kr/#/sports/board_view/soccer.html')
        soup = BeautifulSoup(r.text)

        return '{0}, {1} {2} vs {3} {4}'.format(now, 'Man Utd', '2', '0', 'Liverpool')
