import tkinter
class Submit:
    def __init__(self,master):
        self.master=master
        master.config(bg="yellow")
        tkinter.Label(master, text="Book Name: ",bg="yellow").grid(row=0,column=0)
        bookname_entry=tkinter.Entry(master, bd=2)
        bookname_entry.grid(row=0,column=1)
        tkinter.Label(master, text="Book Author: ",bg="yellow").grid(row=1,column=0)
        author_entry=tkinter.Entry(master, bd=2)
        author_entry.grid(row=1,column=1)
        tkinter.Label(master, text="Quanity: ",bg="yellow").grid(row=2,column=0)
        quantity_entry=tkinter.Entry(master, bd=2)
        quantity_entry.grid(row=2,column=1)
        tkinter.Label(master, text="Price(Rs): ",bg="yellow").grid(row=3,column=0)
        price_entry=tkinter.Entry(master, bd=2)
        price_entry.grid(row=3,column=1)
        submit_btn=tkinter.Button(master,text='Submit',relief=tkinter.GROOVE,bg="orange", fg="red")
        submit_btn.grid(row=4,column=0)
        request_btn=tkinter.Button(master,text='Request',relief=tkinter.GROOVE,bg="orange", fg="red")
        request_btn.grid(row=4,column=1)
        exit_btn=tkinter.Button(master,text='Exit',relief=tkinter.GROOVE,bg="orange", fg="red")
        exit_btn.grid(row=4,column=2)

if __name__=='__main__':
    master=tkinter.Tk()
    Submit(master)
    master.mainloop()
