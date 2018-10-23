'''
Created on Oct 04, 2018
@author: Rajdeep Roy Chowdhury
Licensed Under MIT
'''
import tkinter
from tkinter import ttk
from core import services
from core.services import registerUser
from register import Register
class Admin:
    def __init__(self,master):
        self.master=master
        show_all_users_btn=tkinter.Button(master,text='Show all users',command=self.showAllUsers)
        show_all_users_btn.grid(row=0,column=0)
        add_user_btn=tkinter.Button(master,text='Add user',command=self.showAddUser)
        add_user_btn.grid(row=1,column=0)
        delete_user_btn=tkinter.Button(master,text='Delete User',command=self.showDeleteUser)
        delete_user_btn.grid(row=2,column=0)
        update_user_btn=tkinter.Button(master,text='Update User',command=self.showUpdateUser)
        update_user_btn.grid(row=3,column=0)
        view_order_btn=tkinter.Button(master,text='View Orders',command=self.showViewOrders)
        view_order_btn.grid(row=4,column=0)
        add_book_btn=tkinter.Button(master,text='Add Book',command=self.showAddBook)
        add_book_btn.grid(row=5,column=0)
        delete_book_btn=tkinter.Button(master,text='Delete Book',command=self.showDeleteBook)
        delete_book_btn.grid(row=6,column=0)
        update_book_btn=tkinter.Button(master,text='Update Book',command=self.showUpdateBook)
        update_book_btn.grid(row=7,column=0)
        self.subFrame=tkinter.Frame(master,bg='red')
        self.subFrame.grid(row=0,column=1,rowspan=7)
    
    #Bunch of button callbacks
    def showAllUsers(self):
        self.subFrame.destroy()
        self.subFrame=tkinter.Frame(self.master,bg='red')
        tkinter.Label(self.subFrame,text='Showing all users...').grid(row=0,column=1) # Here goes the subFrame
        tree=ttk.Treeview(self.subFrame,columns=('col1','col2'))
        tree.heading('col1',text='cola')
        # tree['columns']=('cola','colb')
        tree.insert('','end',values=('Hello',''))
        tree.grid(row=1,column=1)
        self.subFrame.grid(row=0,column=1,rowspan=7)
        # self.subFrame.place(x=100,y=100,height=1000,width=100)
    def showAddUser(self):
        self.subFrame.destroy()
        self.subFrame=tkinter.Frame(self.master)
        #Register Window shall open here
        Register(self.subFrame)
        self.subFrame.grid(row=0,column=1,rowspan=7)
    def showDeleteUser(self):
        self.subFrame.destroy()
        self.subFrame=tkinter.Frame(self.master)
        tkinter.Label(self.subFrame,text='Enter user email ID to delete').grid(row=0,column=0)
        email_entry=tkinter.Entry(self.subFrame)
        email_entry.grid(row=0,column=1)
        cancel_btn=tkinter.Button(self.subFrame,text='Cancel')
        cancel_btn.grid(row=1,column=0)
        proceed_btn=tkinter.Button(self.subFrame,text='Proceed')
        proceed_btn.grid(row=1,column=1)
        self.subFrame.grid(row=0,column=1,rowspan=7)
    def showUpdateUser(self): pass # Hard to be implemented
        # self.subFrame.destroy()
        # self.subFrame=tkinter.Frame(self.master)
        # tkinter.Label(self.subFrame,text='Enter user email ID to delete').grid(row=0,column=0)
        # self.subFrame.grid(row=0,column=1,rowspan=7)
    def showViewOrders(self):pass
    def showAddBook(self):
        self.subFrame.destroy()
        self.subFrame=tkinter.Frame(self.master,borderwidth=1,relief='solid')
        tkinter.Label(self.subFrame,text='Enter Book Name to be added').grid(row=0,column=0)
        book_name_entry=tkinter.Entry(self.subFrame)
        book_name_entry.grid(row=0,column=1)
        tkinter.Label(self.subFrame,text='Enter Book Author').grid(row=1,column=0)
        book_author_entry=tkinter.Entry(self.subFrame)
        book_author_entry.grid(row=1,column=1)
        tkinter.Label(self.subFrame,text='Enter Amount').grid(row=2,column=0)
        amount_entry=tkinter.Entry(self.subFrame)
        amount_entry.grid(row=2,column=1)
        proceed_btn=tkinter.Button(self.subFrame,text='Proceed')
        proceed_btn.grid(row=3,column=0)
        reset_btn=tkinter.Button(self.subFrame,text='Reset')
        reset_btn.grid(row=3,column=1)
        self.subFrame.grid(row=0,column=1,rowspan=7)
        # @TODO: enhancements

    def showDeleteBook(self):
        self.subFrame.destroy()
        self.subFrame=tkinter.Frame(self.master,borderwidth=1,relief='solid')
        tkinter.Label(self.subFrame,text='Enter Book Name to delete').grid(row=0,column=0)
        book_name_entry=tkinter.Entry(self.subFrame)
        book_name_entry.grid(row=0,column=1)
        proceed_btn=tkinter.Button(self.subFrame,text='Proceed')
        proceed_btn.grid(row=3,column=0)
        reset_btn=tkinter.Button(self.subFrame,text='Reset')
        reset_btn.grid(row=3,column=1)
        self.subFrame.grid(row=0,column=1,rowspan=7)
    def showUpdateBook(self):pass

    #bunch of actions called by the callbacks
    



if __name__=='__main__':
    master=tkinter.Tk()
    admin=Admin(master)
    master.mainloop()
