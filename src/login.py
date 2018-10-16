import tkinter
from core.services import isValidCredential
# from bms import MainWindow
# Broken
class Login:
    # def call(self):
    #     tkinter.messagebox.showinfo("Reset","Password is Reset")
    # def Forgot_Pswd(self):
    #     self.master.destroy()
    #     tkinter.Label(master, text="New Password ").grid(row=0,column=0)
    #     newpswd_entry=tkinter.Entry(master, bd=2)
    #     newpswd_entry.grid(row=0,column=1)
    #     tkinter.Label(master, text="Confirm New Password: ").grid(row=1,column=0)
    #     cnfpswd_entry=tkinter.Entry(master, bd=2)
    #     cnfpswd_entry.grid(row=1,column=1)
    #     reset_btn=tkinter.Button(master,text='Reset Password',command=self.call,relief=tkinter.RAISED)
    #     reset_btn.grid(row=2,column=0)
    #     exit_btn=tkinter.Button(master,text='Exit',relief=tkinter.RAISED)
    #     exit_btn.grid(row=2,column=1)
    def __init__(self,master):
        self.master=master
        tkinter.Label(master, text="Email Id: ").grid(row=0,column=0)
        self.email_entry=tkinter.Entry(master, bd=2)
        self.email_entry.grid(row=0,column=1)
        tkinter.Label(master, text="Password: ").grid(row=1,column=0)
        self.password_entry=tkinter.Entry(master, bd=2)
        self.password_entry.config(show="*")
        self.password_entry.grid(row=1,column=1)
        sign_btn=tkinter.Button(master,text='Sign In',command=self.signIn)
        sign_btn.grid(row=2,column=1)
        forgot_btn=tkinter.Button(master,text='Forgot Password')#,command=self.Forgot_Pswd)
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
