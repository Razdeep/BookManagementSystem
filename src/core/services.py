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
    try:
        conn=sqlite3.connect('data.db') # @TODO: replaced by global variable
        conn.execute('insert into register values(?,?,?,?,?,?,?)',user)
        conn.commit()
        conn.close()
        return True
    except:
        return False
    # @TODO: test

def deleteUser(emailID):
    '''For deleting user from REGISTER table
    Important: object must be a tuple, and not strings
    '''
    try:
        conn=sqlite3.connect('data.db') # @TODO: replaced by global variable
        conn.execute('delete from "REGISTER" where "EMAIL_ID"=?;',emailID)
        # argument must be a tuple like ('rrajdeeproychowdhury@gmail.com',)
        conn.commit()
        conn.close()
        return True
    except:
        return False

def createDatabase():
    '''Creates an empty database'''
    conn=sqlite3.connect('data.db') # @TODO: replaced by global variable
    conn.execute('CREATE TABLE IF NOT EXISTS "REGISTER" ("FIRST_NAME" TEXT,"LAST_NAME" TEXT,"DOB" TEXT,"GENDER" TEXT, "CONTACT" TEXT,"EMAIL_ID" TEXT NOT NULL UNIQUE, "PASSWORD" TEXT, PRIMARY KEY("EMAIL_ID"))')
    conn.commit()
    conn.close()

def createSampleDatabaseWithDummyData():
    '''Creates dummy a sample database with dummy data'''
    createDatabase()
    userList=[('Rajdeep','Roy Chowdhury','21-07-2000','MALE','9674810029','rrajdeeproychowdhury@gmail.com','password'),
                ('Bishakha', 'Jain','01-01-1999','FEMALE','7397472323','bishakhaajain@gmail.com','password'),
                ('Riya','Garg','01-01-1999','FEMALE','217863821','riyagargsomething@gmail.com','password')]
    conn=sqlite3.connect('data.db') # @TODO: replaced by global variable
    # conn.executemany('insert into REGISTER values(?,?,?,?,?,?,?)',userList)
    for user in userList:
        conn.execute('insert into REGISTER values(?,?,?,?,?,?,?)',user)
    conn.commit()
    conn.close()
    # In case of failure use for loops

def addBook(book): # Corrupted function here... FIX THIS
    '''For adding book to BOOK table'''
    # NOTE: HERE 'book' is a tuple. Handle it carefully
    try:
        conn=sqlite3.connect('data.db') # @TODO: replaced by global variable
        conn.execute(';',book) # @TODO: IMPLEMENT ASAP
        # argument must be a tuple like SOMETHING
        conn.commit()
        conn.close()
        return True
    except:
        return False

def deleteBook():
    pass

def changePassword(object):
    '''For updating password in the REGISTER table
         Argument(object) must be a tuple like (newPassword,email)'''
    try:
        conn=sqlite3.connect('data.db') # @TODO: replaced by global variable
        conn.execute('UPDATE "REGISTER" SET "PASSWORD"=? WHERE "EMAIL_ID"=?;',object)
        # argument must be a tuple like SOMETHING
        conn.commit()
        conn.close()
        return True
    except:
        return False

if __name__=='__main__':
    # For testing only
    if isValidCredential('raj','raj'):
        print('User ID : raj')
        print('Password : raj')
        print('are available in the the table')
    else:
        print('User ID : raj')
        print('Password : raj')
        print('are not available in the the table')