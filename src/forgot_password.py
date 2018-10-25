import tkinter
from tkinter import messagebox
from core import services
#master=tkinter.Tk()
class Forgot_Pswd:
        def __init__(self,master):
                self.master=master
                self.subbody=tkinter.Frame(self.master)
                self.subbody.config(bg='yellow3')
                self.subbody.pack()
                tkinter.Label(self.subbody, text="Email ID ",bg='yellow3').grid(row=0,column=0)
                self.email_entry=tkinter.Entry(self.subbody,bd=2)
                self.email_entry.grid(row=0,column=1)
                tkinter.Label(self.subbody, text="New Password ",bg='yellow3').grid(row=1,column=0)
                self.newpswd_entry=tkinter.Entry(self.subbody, bd=2)
                self.newpswd_entry.grid(row=1,column=1)
                tkinter.Label(self.subbody, text="Confirm New Password: ",bg='yellow3').grid(row=2,column=0)
                self.cnfpswd_entry=tkinter.Entry(self.subbody, bd=2)
                self.cnfpswd_entry.grid(row=2,column=1)
                reset_btn=tkinter.Button(self.subbody,text='Reset Password',command=self.changePassword,relief=tkinter.RAISED)
                reset_btn.grid(row=3,column=0)
        def changePassword(self):
                if self.email_entry.get()!='' and self.newpswd_entry.get()==self.cnfpswd_entry.get():
                        object=(self.newpswd_entry.get(),self.email_entry.get())
                        if services.changePassword(object):
                                messagebox.showinfo('Success','Successfully changed password')
                        else:
                                messagebox.showerror('Failed','Couldn\'t delete book. Contact support team')
                else:
                        messagebox.showinfo('Missing field','Please check that you have filled all the fields correctly.')
                
                        
if __name__=='__main__':
    master=tkinter.Tk()
    Forgot_Pswd(master)
    master.mainloop()


