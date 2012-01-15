#!/usr/bin/env python
# onlog.py: log when this script is running

import sqlite3
import time
import os.path

from settings import DB_NAME, SLEEP_TIME, DOWN_TIME

conn = sqlite3.connect(DB_NAME)

conn.execute('CREATE TABLE IF NOT EXISTS up (t REAL)')
conn.execute('CREATE TABLE IF NOT EXISTS down (t REAL)')

t = None

while True:
    new_t = time.time()

    if t is None or new_t - t > DOWN_TIME:
        conn.execute('INSERT INTO up (t) VALUES (?)', (new_t,))
        res = conn.execute('INSERT INTO down (t) VALUES (?)', (new_t,))
        rowid = res.lastrowid
    else:
        conn.execute('UPDATE down SET t = ? WHERE rowid = ?', (new_t, rowid))
    conn.commit()

    t = new_t
    time.sleep(SLEEP_TIME)
