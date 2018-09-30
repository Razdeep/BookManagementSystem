import sqlite3
class LoginService:
    def __init__(self):pass
    
    def isValidCredential(self,userId,password):
        conn=sqlite3.connect('data.db')
        rs=conn.execute('select * from register where USER_ID=? and PASSWORD=?',(userId,password))
        if rs.fetchone()!=None:
            print(rs)
            return True
        else:
            return False

if __name__=='__main__':
    loginService=LoginService()
    if loginService.isValidCredential('raj','raj'):
        print('User ID : raj')
        print('Password : raj')
        print('are available in the the table')
    else:
        print('User ID : raj')
        print('Password : raj')
        print('are not available in the the table')