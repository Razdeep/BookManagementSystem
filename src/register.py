'''
Created on Sep 29, 2018
@author: Rajdeep Roy Chowdhury
Licensed Under MIT
'''
import tkinter
class Register:
    def __init__(self,master):
        root=master
        # @TODO: Modification of fields
        tkinter.Label(root,text='First name').grid(row=0,column=0)
        firstname_entry=tkinter.Entry(root)
        firstname_entry.grid(row=0,column=1)
        tkinter.Label(root,text='Last name').grid(row=1,column=0)
        lastname_entry=tkinter.Entry(root)
        lastname_entry.grid(row=1,column=1)
        tkinter.Label(root,text='Date of Birth').grid(row=2,column=0)
        dob=tkinter.Entry(root)
        dob.grid(row=2,column=1)
        var=tkinter.IntVar()
        tkinter.Label(root,text='Gender').grid(row=3,column=0)
        male_radio=tkinter.Radiobutton(root,text='Male',variable=var,value=1)
        female_radio=tkinter.Radiobutton(root,text='Female',variable=var,value=2)
        male_radio.grid(row=3,column=1)
        female_radio.grid(row=3,column=2)
        tkinter.Label(root,text='Email ID').grid(row=4,column=0)
        emailid_entry=tkinter.Entry(root)
        emailid_entry.grid(row=4,column=1)
        tkinter.Label(root,text='Password').grid(row=5,column=0)
        password_entry=tkinter.Entry(root)
        password_entry.grid(row=5,column=1)
        tkinter.Label(root,text='Confirm Password').grid(row=6,column=0)
        confirmpassword_entry=tkinter.Entry(root)
        confirmpassword_entry.grid(row=6,column=1)
        submit_btn=tkinter.Button(root,text='Submit')
        submit_btn.grid(row=7,column=0)
        reset_btn=tkinter.Button(root,text='Reset')
        reset_btn.grid(row=7,column=1)

if __name__=='__main__':
    root=tkinter.Tk()
    Register(root)
    root.mainloop()