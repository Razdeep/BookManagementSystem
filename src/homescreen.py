import tkinter
from core.config import *
from fiction import fiction_books
from nonfiction import nonfiction_books
from submit import Submit
from delivery import Delivery

class HomeScreen:
    def __init__(self,master):
        self.master=master
        self.master.config(bg="yellow green")
        navbar=tkinter.Frame(self.master)
        fictn_nav=tkinter.Button(navbar,text='Fictional Books',relief=tkinter.RAISED,bg="gold",activebackground="white",fg="dark blue",height=2,font=('Comic Sans MS bold',10),command=self.showfictionHere,width=20)
        fictn_nav.grid(row=0,column=0)
        
        nonfictn_nav=tkinter.Button(navbar,text='Non-Fictional Books',relief=tkinter.RAISED,bg="gold",activebackground="white",fg="dark blue",height=2,font=('Comic Sans MS bold',10),command=self.shownonfictionHere,width=20)
        nonfictn_nav.grid(row=1,column=0)
        submit_nav=tkinter.Button(navbar,text='Submit/Request Books',relief=tkinter.RAISED,bg="gold",activebackground="white",fg="dark blue",height=2,font=('Comic Sans MS bold',10),command=self.showsubmitHere,width=20)
        submit_nav.grid(row=2,column=0)
        del_nav=tkinter.Button(navbar,text='Delivery of Books',relief=tkinter.RAISED,bg="gold",activebackground="white",fg="dark blue",height=2,font=('Comic Sans MS bold',10),command=self.showdeliveryHere,width=20)
        del_nav.grid(row=3,column=0)
        navbar.grid(row=0,column=0)
        self.body=tkinter.Frame(self.master)
        self.body.grid(row=0,column=1)

    def showfictionHere(self):
        self.body.destroy()
        self.body=tkinter.Frame(self.master)
        fiction_books(self.body)
        self.body.grid(row=0,column=1)

    def shownonfictionHere(self):
        self.body.destroy()
        self.body=tkinter.Frame(self.master)
        nonfiction_books(self.body)
        self.body.grid(row=0,column=1)

    def showdeliveryHere(self):
        self.body.destroy()
        self.body=tkinter.Frame(self.master)
        Delivery(self.body)
        self.body.grid(row=0,column=1)
    def showsubmitHere(self):
        self.body.destroy()
        self.body=tkinter.Frame(self.master)
        Submit(self.body)
        self.body.grid(row=0,column=1)


if __name__=='__main__':
    root=tkinter.Tk()
    HomeScreen(root)
    root.mainloop()