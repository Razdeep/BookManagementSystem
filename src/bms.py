'''
Created on Sep 29, 2018
@author: Rajdeep Roy Chowdhury
Licensed Under MIT
'''
# This is the kickstarter
import tkinter
from core.config import *
from register import Register
from login import Login
from admin import Admin
from homescreen import HomeScreen
class MainWindow:
    def __init__(self,master):
        self.master=master
        master.title(TITLE)
        master.geometry(str(DISPLAY_WIDTH)+'x'+str(DISPLAY_HEIGHT))
        master.resizable(0,0)

        navbar=tkinter.Frame(master)
        login_nav=tkinter.Button(navbar,text='Login Here',command=self.showLoginHere)
        login_nav.grid(row=0,column=0)
        register_nav=tkinter.Button(navbar,text='Register Here',command=self.showRegisterHere)
        register_nav.grid(row=0,column=1)
        admin_nav=tkinter.Button(navbar,text='Admin Portal',command=self.showAdminPortal)
        admin_nav.grid(row=0,column=2)
        navbar.place(x=0,y=0)

        self.body=tkinter.Frame(master,borderwidth=1,relief='solid')
        Login(self.body)
        self.body.place(x=X_WINDOW,y=Y_WINDOW)

    def showRegisterHere(self):
        self.body.destroy()
        self.body=tkinter.Frame(self.master,borderwidth=1,relief='solid')
        Register(self.body)
        self.body.place(x=X_WINDOW,y=Y_WINDOW)
    def showLoginHere(self):
        self.body.destroy()
        self.body=tkinter.Frame(self.master,borderwidth=1,relief='solid')
        Login(self.body)
        self.body.place(x=X_WINDOW,y=Y_WINDOW)
    def showAdminPortal(self):
        self.body.destroy()
        self.body=tkinter.Frame(self.master,borderwidth=1,relief='solid')
        Admin(self.body)
        self.body.place(x=X_WINDOW,y=Y_WINDOW)

if __name__=='__main__':
    root=tkinter.Tk()
    MainWindow(root)
    root.mainloop()