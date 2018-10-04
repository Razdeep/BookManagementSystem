import tkinter
from core.services import isValidCredential
class Login:
    def __init__(self,master):
        tkinter.Label(master, text="Email Id: ").grid(row=0,column=0)
        self.email_entry=tkinter.Entry(master, bd=2)
        self.email_entry.grid(row=0,column=1)
        tkinter.Label(master, text="Password: ").grid(row=1,column=0)
        self.password_entry=tkinter.Entry(master, bd=2)
        self.password_entry.grid(row=1,column=1)
        sign_btn=tkinter.Button(master,text='Sign In',command=self.signIn)
        sign_btn.grid(row=2,column=1)
        forgot_btn=tkinter.Button(master,text='Forgot Password')
        forgot_btn.grid(row=2,column=0)
    def signIn(self):
        if isValidCredential(self.email_entry.get(),self.password_entry.get()):
            print('Login successful')
        else:
            print('Login failed')

if __name__=='__main__':
    master=tkinter.Tk()
    Login(master)
    master.mainloop()
