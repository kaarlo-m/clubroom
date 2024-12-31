import sqlite3

DB_FILE_NAME = 'reservations.db'

class ResDataBase:
    def __init__(self):
        self.con=sqlite3.connection(DB_FILE_NAME)
        self.cur=self.con.cursor()

    