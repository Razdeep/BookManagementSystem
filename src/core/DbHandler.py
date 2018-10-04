'''
Created on Sep 29, 2018
@author: Rajdeep Roy Chowdhury
Licensed Under MIT
'''

# This class must implemented if concurrent connections fail

import sqlite3
class DbHandler:
    def __init__(self):
        self.conn=sqlite3.connect('data.db')
    def getConnection(self): pass


# Driver code
if __name__=='__main__':
    dbHandler=DbHandler()
