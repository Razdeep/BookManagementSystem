'''
Created on Sep 29, 2018
@author: Rajdeep Roy Chowdhury
Licensed Under MIT
'''
import sqlite3
    
def isValidCredential(emailId,password):
    '''It shall be used for login'''
    conn=sqlite3.connect('data.db') # @TODO: replaced by global variable
    rs=conn.execute('select * from register where EMAIL_ID=? and PASSWORD=?',(emailId,password))
    if rs.fetchone()!=None:
        # print('Login successful')
        return True
    else:
        return False
    conn.close()

def registerUser(user):
    '''For putting a tuple in Register Table'''
    conn=sqlite3.connect('data.db') # @TODO: replaced by global variable
    conn.execute('insert into register values(?,?,?,?,?,?,?)',user)
    conn.close()
    # @TODO: test

def updateUser(object):
    '''For updating user'''
    # to be implemented at last

def deleteUser(object):
    '''For deleting user from REGISTER table'''
    # @TODO

def createDatabase():
    '''Creates an empty database'''
    conn=sqlite3.connect('data.db') # @TODO: replaced by global variable
    conn.execute('create table REGISTER(FIRST_NAME varchar(20),LAST_NAME varchar(20),DATE_OF_BIRTH varchar(20),GENDER varchar(10),CONTACT varchar(12),EMAIL_ID varchar(30),PASSWORD varchar(30)')
    conn.close()

def createSampleDatabaseWithDummyData():
    '''Creates dummy a sample database with dummy data'''
    createDatabase()
    userList=[('Rajdeep','Roy Chowdhury','21-07-2000','MALE','9674810029','rrajdeeproychowdhury@gmail.com','password'),
                ('Bishakha', 'Jain','01-01-1999','FEMALE','7397472323','bishakhaajain@gmail.com','password'),
                ('Riya','Garg','01-01-1999','FEMALE','217863821','riyagargsomething@gmail.com','password')]
    conn=sqlite3.connect('data.db') # @TODO: replaced by global variable
    conn.executemany('insert into REGISTER values(?,?,?,?,?,?,?)',userList)
    conn.close()
    # @TODO: test
    # In case of failure use for loops

def addBook():
    pass

def updateBook():
    pass

def deleteBook():
    pass

if __name__=='__main__':
    if isValidCredential('raj','raj'):
        print('User ID : raj')
        print('Password : raj')
        print('are available in the the table')
    else:
        print('User ID : raj')
        print('Password : raj')
        print('are not available in the the table')