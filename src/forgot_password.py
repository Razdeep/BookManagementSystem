import tkinter
from tkinter import messagebox
#master=tkinter.Tk()
class Forgot_Pswd:
        def call(self):
                if(self.cnfpswd_entry.get() != "" and self.cnfpswd_entry.get()== self.newpswd_entry.get()):
                        MsgBox = messagebox.askquestion ('New Password','Are you sure you want to save the password',icon = 'warning')
                        if MsgBox == 'yes':
                                messagebox.showinfo('Save','Changes are saved')
                                self.master.destroy()
                        else:
                                messagebox.showinfo('Return','You will now return to the application')
                elif(self.cnfpswd_entry.get()=="" or self.newpswd_entry.get()==""):
                        messagebox.showerror('Error','Please Enter a password')
        def Exit(self):
                MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
                if MsgBox == 'yes':
                        self.master.destroy()
                else:
                        messagebox.showinfo('Return','You will now return to the application screen')


        def __init__(self,master):
                self.master=master
                self.subbody=tkinter.Frame(self.master)
                self.subbody.config(bg='yellow3')
                self.subbody.pack()
                tkinter.Label(self.subbody, text="New Password ",bg='yellow3').grid(row=0,column=0)
                self.newpswd_entry=tkinter.Entry(self.subbody, bd=2)
                self.newpswd_entry.grid(row=0,column=1)
                tkinter.Label(self.subbody, text="Confirm New Password: ",bg='yellow3').grid(row=1,column=0)
                self.cnfpswd_entry=tkinter.Entry(self.subbody, bd=2)
                self.cnfpswd_entry.grid(row=1,column=1)
                reset_btn=tkinter.Button(self.subbody,text='Reset Password',command=self.call,relief=tkinter.RAISED)
                reset_btn.grid(row=2,column=0)
                exit_btn=tkinter.Button(self.subbody,text='Exit',relief=tkinter.RAISED,command=self.Exit)
                exit_btn.grid(row=2,column=1)
                        
if __name__=='__main__':
    master=tkinter.Tk()
    Forgot_Pswd(master)
    master.mainloop()


