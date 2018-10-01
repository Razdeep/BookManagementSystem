import tkinter
from core.loginService import LoginService
class Login:
    def __init__(self,master):
        tkinter.Label(master, text="Username: ").grid(row=0,column=0)
        username_entry=tkinter.Entry(master, bd=2)
        username_entry.grid(row=0,column=1)
        tkinter.Label(master, text="Password: ").grid(row=1,column=0)
        password_entry=tkinter.Entry(master, bd=2)
        password_entry.grid(row=1,column=1)
        sign_btn=tkinter.Button(master,text='Sign In')
        sign_btn.grid(row=2,column=1)
        forgot_btn=tkinter.Button(master,text='Forgot Password')
        forgot_btn.grid(row=2,column=0)

if __name__=='__main__':
    master=tkinter.Tk()
    Login(master)
    master.mainloop()
