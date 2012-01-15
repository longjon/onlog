#!/usr/bin/env python
# readlog.py: read the onlog and output a text file with data

import sqlite3

from settings import DB_NAME

conn = sqlite3.connect(DB_NAME)

up_res = conn.execute('SELECT * FROM up ORDER BY t')
down_res = conn.execute('SELECT * FROM down ORDER BY t')

for up, down in zip(list(up_res), list(down_res)):
    print up[0], down[0]

conn.close()
