import sqlite3
conn = sqlite3.connect('Group3Lab5PostLAb.db')
cur = conn.cursor()
cur.execute("Select * from Reservation")
row = cur.fetchall()
for row in row:
    print(row)