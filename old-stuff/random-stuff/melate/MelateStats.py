"""
Most frequent picked numbers in Melate (kinda lottery in MX)
"""

import requests
from collections import defaultdict

URL = 'http://www.pronosticos.gob.mx/Documentos/Historicos/Melate.csv'

class MelateStats:
    def __init__(self):
        self.data = requests.get(URL)

    def most_freq_num(self, start=1, end=7):
        cnt = defaultdict(lambda: 0)
        lines = self.data.iter_lines()
        next(lines)  # ignore header
        for line in lines:
            tok = str(line).split(',')
            if len(tok) != 11:
                break
            for i in range(1+start, 2+end):
                cnt[int(tok[i])] += 1
        num = list(range(57))
        num.sort(key=lambda x: cnt[x], reverse=True)
        for x in num:
            print("%02d %02d" % (x, cnt[x]))

MelateStats().most_freq_num(1,3)
