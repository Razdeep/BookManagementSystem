from tkinter import *
import tkinter
class Delivery:
    def __init__(self,master):
        tkinter.Label(master, text="First Name: ").grid(row=0,column=5)
        firstname_entry=tkinter.Entry(master, bd=2)
        firstname_entry.grid(row=0,column=7)
        
        tkinter.Label(master, text="Last Name: ").grid(row=1,column=5)
        lastname_entry=tkinter.Entry(master, bd=2)
        lastname_entry.grid(row=1,column=7)
        
        tkinter.Label(master, text="Address: ").grid(row=2,column=5)
        address_entry=tkinter.Entry(master, bd=2)
        address_entry.grid(row=2,column=7)
        
        tkinter.Label(master, text="Pin Code: ").grid(row=3,column=5)
        pc_entry=tkinter.Entry(master, bd=2)
        pc_entry.grid(row=3,column=7)
        
        tkinter.Label(master, text="Email Id: ").grid(row=4,column=5)
        ei_entry=tkinter.Entry(master, bd=2)
        ei_entry.grid(row=4,column=7)
        
        tkinter.Label(master, text="Phone No: ").grid(row=5,column=5)
        pn_entry=tkinter.Entry(master, bd=2)
        pn_entry.grid(row=5,column=7)
        
        submit_btn=tkinter.Button(master,text='Submit',relief=GROOVE)
        submit_btn.grid(row=6,column=5)
        
        exit_btn=tkinter.Button(master,text='Exit',relief=GROOVE)
        exit_btn.grid(row=6,column=6)

if __name__=='__main__':
    master=tkinter.Tk()
    Delivery(master)
    master.mainloop()
