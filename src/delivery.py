from tkinter import*
import tkinter
class Delivery:
    def __init__(self,master):
        master.config(bg="coral")
        tkinter.Label(master, text="First Name: ",bg="coral",font=('Comic Sans MS',18)).grid(row=0,column=5)
        firstname_entry=tkinter.Entry(master,bd=3,bg="light grey")
        firstname_entry.grid(row=0,column=7)
        
        tkinter.Label(master, text="Last Name: ",bg="coral",font=('Comic Sans MS',18)).grid(row=1,column=5)
        lastname_entry=tkinter.Entry(master, bd=3,bg="light grey")
        lastname_entry.grid(row=1,column=7)
        
        tkinter.Label(master, text="Address: ",bg="coral",font=('Comic Sans MS',18)).grid(row=2,column=5)
        address_entry=tkinter.Entry(master,bd=3,bg="light grey")
        address_entry.grid(row=2,column=7)
        
        tkinter.Label(master, text="Pin Code: ",bg="coral",font=('Comic Sans MS',18)).grid(row=3,column=5)
        pc_entry=tkinter.Entry(master,bd=3,bg="light grey")
        pc_entry.grid(row=3,column=7)
        
        tkinter.Label(master, text="Email Id: ",bg="coral",font=('Comic Sans MS',18)).grid(row=4,column=5)
        ei_entry=tkinter.Entry(master,bd=3,bg="light grey")
        ei_entry.grid(row=4,column=7)
        
        tkinter.Label(master, text="Phone No: ",bg="coral",font=('Comic Sans MS',18)).grid(row=5,column=5)
        pn_entry=tkinter.Entry(master,bd=3,bg="light grey")
        pn_entry.grid(row=5,column=7)
        
        submit_btn=tkinter.Button(master,text='Submit',relief=tkinter.GROOVE,bg="orange",fg="red",width=10,font=('Comic Sans MS bold',13),activebackground="white")
        submit_btn.grid(row=6,column=7)
        
        

if __name__=='__main__':
    master=tkinter.Tk()
    Delivery(master)
    master.mainloop()
