import tkinter
from tkinter import messagebox
from core.services import isValidCredential
from forgot_password import Forgot_Pswd
from homescreen import HomeScreen
from submit import Submit
class Login:
    def __init__(self,master):
        self.master=master
        self.master.config(bg="yellow green")
        self.wrapper=tkinter.Frame(self.master)
        self.wrapper.config(bg="yellow green")
        tkinter.Label(self.wrapper,text="Email Id: ",bg="yellow green",font=('Comic Sans MS',13)).grid(row=0,column=0)
        self.email_entry=tkinter.Entry(self.wrapper, bd=3,bg="light grey")
        self.email_entry.grid(row=0,column=1)
        tkinter.Label(self.wrapper, text="Password: ",bg="yellow green",font=('Comic Sans MS',13)).grid(row=1,column=0)
        self.password_entry=tkinter.Entry(self.wrapper, bd=2)
        self.password_entry.config(show="*")
        self.password_entry.grid(row=1,column=1)
        sign_btn=tkinter.Button(self.wrapper,text='Sign In',bg="light steel blue",activebackground="white",fg="dark blue",width=13,font=('Comic Sans MS bold',10),command=self.signIn)
        sign_btn.grid(row=2,column=1)
        forgot_btn=tkinter.Button(self.wrapper,text='Forgot Password',bg="light steel blue",activebackground="white",fg="dark blue",width=13,font=('Comic Sans MS bold',10),command=self.showForgotPassword)
        forgot_btn.grid(row=2,column=0)
        self.wrapper.grid(row=0,column=0)
    def signIn(self):
        if isValidCredential(self.email_entry.get(),self.password_entry.get()):
            print('Login successful')
            self.showHomeScreen()
        else:
            messagebox.showwarning('Login Failed', 'Incorrect credentials provided. Please try again')
            print('Login failed')
    def showForgotPassword(self):
        self.wrapper.destroy()
        self.wrapper=tkinter.Frame(self.master)
        Forgot_Pswd(self.wrapper)
        self.wrapper.grid(row=0,column=0)
    def showHomeScreen(self):
        self.wrapper.destroy()
        self.wrapper=tkinter.Frame(self.master)
        HomeScreen(self.wrapper)
        # Submit(self.wrapper)
        self.wrapper.grid(row=0,column=0)
            

if __name__=='__main__':
    master=tkinter.Tk()
    Login(master)
    master.mainloop()
