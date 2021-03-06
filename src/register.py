'''
Created on Sep 29, 2018
@author: Rajdeep Roy Chowdhury
Licensed Under MIT
'''
import tkinter
from tkinter import messagebox
from core import services
class Register:
    def __init__(self,master):
        # Styling constants declaration starts here
        BG="light coral"
        FONT=('Comic Sans MS',13)
        FG="dark blue"
        # Styling constants ends
        self.master=master
        self.master.config(bg=BG)
        self.wrapper=tkinter.Frame(self.master)
        self.wrapper.config(bg=BG)
        self.wrapper.grid(row=0,column=0)
        tkinter.Label(self.wrapper,text='First name',font=FONT,bg=BG,fg=FG).grid(row=0,column=0)
        self.firstname_entry=tkinter.Entry(self.wrapper)
        self.firstname_entry.grid(row=0,column=1)
        tkinter.Label(self.wrapper,text='Last name',font=FONT,bg=BG,fg=FG).grid(row=1,column=0)
        self.lastname_entry=tkinter.Entry(self.wrapper)
        self.lastname_entry.grid(row=1,column=1)
        tkinter.Label(self.wrapper,text='Date of Birth',font=FONT,bg=BG,fg=FG).grid(row=2,column=0)
        self.dob=tkinter.Entry(self.wrapper)
        self.dob.grid(row=2,column=1)
        self.gender=tkinter.StringVar()
        tkinter.Label(self.wrapper,text='Gender',font=FONT,bg=BG,fg=FG).grid(row=3,column=0)
        self.male_radio=tkinter.Radiobutton(self.wrapper,text='Male',font=FONT,bg=BG,fg=FG,variable=self.gender,value='MALE')
        self.female_radio=tkinter.Radiobutton(self.wrapper,text='Female',font=FONT,bg=BG,fg=FG,variable=self.gender,value='FEMALE')
        self.male_radio.grid(row=3,column=1)
        self.female_radio.grid(row=3,column=2)
        tkinter.Label(self.wrapper,text='Address',font=FONT,bg=BG,fg=FG).grid(row=4,column=0)
        self.address_entry=tkinter.Entry(self.wrapper)
        self.address_entry.grid(row=4,column=1)
        tkinter.Label(self.wrapper,text='Contact Number',font=FONT,bg=BG,fg=FG).grid(row=5,column=0)
        self.contact_entry=tkinter.Entry(self.wrapper)
        self.contact_entry.grid(row=5,column=1)
        tkinter.Label(self.wrapper,text='Email ID',font=FONT,bg=BG,fg=FG).grid(row=6,column=0)
        self.emailid_entry=tkinter.Entry(self.wrapper)
        self.emailid_entry.grid(row=6,column=1)
        tkinter.Label(self.wrapper,text='Password',font=FONT,bg=BG,fg=FG).grid(row=7,column=0)
        self.password_entry=tkinter.Entry(self.wrapper)
        self.password_entry.grid(row=7,column=1)
        tkinter.Label(self.wrapper,text='Confirm Password',font=FONT,bg=BG,fg=FG).grid(row=8,column=0)
        self.confirmpassword_entry=tkinter.Entry(self.wrapper)
        self.confirmpassword_entry.grid(row=8,column=1)
        self.submit_btn=tkinter.Button(self.wrapper,text='Submit',command=self.submit)
        self.submit_btn.grid(row=9,column=0)
        self.reset_btn=tkinter.Button(self.wrapper,text='Reset',command=self.reset)
        self.reset_btn.grid(row=9,column=1)
        # For debugging only 
        # self.test=tkinter.Button(self.wrapper,text='Test',command=self.checkEmail)
        # self.test.grid(row=10,column=1)
        # Comment the above part at the time of production 
        
    def submit(self):
        if self.checkForm():
            # Here goes the code for inserting to database
            try:
                services.registerUser((self.firstname_entry.get(),self.lastname_entry.get(),self.dob.get(),self.gender.get(),self.contact_entry.get(),self.emailid_entry.get(),self.password_entry.get()))
                messagebox.showinfo('Success','Congratulations!! Registration Successful')
                print('Log: Successfully inserted the record in the REGISTER table')
                self.reset()
            except:
                messagebox.showerror('SQL Error','SQL Error occurred: Check the logs rajdeep B)')
        else:
            messagebox.showwarning('Warning','You didn\'t fill up all the forms fields properly')
    def checkForm(self):
        if self.checkName() and self.checkDOB() and self.checkAddress() and self.checkContact() and self.checkEmail() and self.checkPassword():
            return True
        return False
    def checkName(self):
        # print('In name')
        if self.firstname_entry.get()!='' and self.lastname_entry.get()!='': #@ TODO: Check numbers and special characters
            return True
        return False
    def checkDOB(self):
        # print('In dob')
        if self.dob.get()!='':
            return True
        return False
    def checkAddress(self):
        if self.address_entry.get()!='':
            return True
        return False
    def checkContact(self):
        if self.contact_entry.get()!='':
            phone=int(self.contact_entry.get())
            if phone<10**9 and phone>10**10:
                return False
            return True
        return False
        
    def checkEmail(self):
        # Check if contains @ and .
        if self.emailid_entry.get()!='' and self.emailid_entry.get().find('@')!=-1 and self.emailid_entry.get().find('.')!=-1:
            # print('First Condition passed')
            # Check Positions
            pieces=self.emailid_entry.get().split('@')
            # print(pieces)
            if pieces[1].find('.')<3 and pieces[1].rfind('.')<3: # Two birds in one arrow
                # print('Not valid Email')
                return False
            # print('Valid Email')
            return True
        # print('Invalid email')
        return False
            
            
    def checkPassword(self):
        # @TODO: Check whether password contains alphanumeric values and special characters
        if self.password_entry.get()!='' and self.confirmpassword_entry.get()!='':
            if self.password_entry.get()==self.confirmpassword_entry.get():
                return True
        return False

    def reset(self):
        self.firstname_entry.delete(0,last=tkinter.END)
        self.lastname_entry.delete(0,last=tkinter.END)
        self.dob.delete(0,last=tkinter.END)
        self.address_entry.delete(0,last=tkinter.END)
        self.contact_entry.delete(0,last=tkinter.END)
        self.emailid_entry.delete(0,last=tkinter.END)
        self.password_entry.delete(0,last=tkinter.END)
        self.confirmpassword_entry.delete(0,last=tkinter.END)


if __name__=='__main__':
    root=tkinter.Tk()
    Register(root)
    root.mainloop()