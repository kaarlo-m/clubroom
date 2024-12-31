import calendar
import time
import sqlite3

DB_FILE_NAME = 'reservations.db'

class Reservation:
    def __init__(self,res_time,host):
        self.res_time=res_time
        self.host=host


res1=Reservation(0,115)



print(res1.host, res1.res_time)