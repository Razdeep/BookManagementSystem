'''
Created on Oct 04, 2018
@author: Rajdeep Roy Chowdhury
Licensed Under MIT
'''
import tkinter
from tkinter import ttk
from tkinter import messagebox
from core import services
from core.services import registerUser
from register import Register

class Admin:
    def __init__(self,master):
        self.master=master
        show_all_users_btn=tkinter.Button(master,text='Show all users',command=self.showAllUsers,width=15,height=2)
        show_all_users_btn.grid(row=0,column=0)
        add_user_btn=tkinter.Button(master,text='Add user',command=self.showAddUser,width=15,height=2)
        add_user_btn.grid(row=1,column=0)
        delete_user_btn=tkinter.Button(master,text='Delete User',command=self.showDeleteUser,width=15,height=2)
        delete_user_btn.grid(row=2,column=0)
        view_order_btn=tkinter.Button(master,text='View Orders',command=self.showViewOrders,width=15,height=2)
        view_order_btn.grid(row=4,column=0)
        add_book_btn=tkinter.Button(master,text='Add Book',command=self.showAddBook,width=15,height=2)
        add_book_btn.grid(row=5,column=0)
        delete_book_btn=tkinter.Button(master,text='Delete Book',command=self.showDeleteBook,width=15,height=2)
        delete_book_btn.grid(row=6,column=0)
        self.subFrame=tkinter.Frame(master,bg='red')
        self.subFrame.grid(row=0,column=1,rowspan=7)
    
    #Bunch of button callbacks
    def showAllUsers(self):
        self.subFrame.destroy()
        self.subFrame=tkinter.Frame(self.master,bg='red')
        tkinter.Label(self.subFrame,text='Showing all users...').grid(row=0,column=1) # Here goes the subFrame
        tree=ttk.Treeview(self.subFrame,columns=('FIRST_NAME','LAST_NAME','DOB','GENDER','CONTACT','EMAIL_ID','PASSWORD'))
        tree.heading('FIRST_NAME',text='Name')
        tree.heading('LAST_NAME',text='Surname')
        tree.heading('DOB',text='DOB')
        tree.heading('GENDER',text='Sex')
        tree.heading('CONTACT',text='Contact')
        tree.heading('EMAIL_ID',text='Email')
        tree.heading('PASSWORD',text='Password')
        tree.column('#0',width=2)
        tree.column('FIRST_NAME',width=20)
        tree.column('LAST_NAME',width=20)
        tree.column('DOB',width=10)
        tree.column('GENDER',width=10)
        tree.column('CONTACT',width=10)
        tree.column('EMAIL_ID',width=10)
        tree.column('PASSWORD',width=10)
        # tree.insert('','end',values=('data1','data2'))
        userDataList=services.fetchUsers()
        for data in userDataList:
            tree.insert('','end',values=data)
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
        self.email_entry=tkinter.Entry(self.subFrame)
        self.email_entry.grid(row=0,column=1)
        cancel_btn=tkinter.Button(self.subFrame,text='Cancel',command=self.cancel)
        cancel_btn.grid(row=1,column=0)
        proceed_btn=tkinter.Button(self.subFrame,text='Proceed',command=self.deleteUser)
        proceed_btn.grid(row=1,column=1)
        self.subFrame.grid(row=0,column=1,rowspan=7)
    def showViewOrders(self):pass # @TODO: TO BE IMPLEMENTED AS SOON AS TREEVIEW IS SORTED OUT
    def showAddBook(self):
        self.subFrame.destroy()
        self.subFrame=tkinter.Frame(self.master,borderwidth=1,relief='solid')
        tkinter.Label(self.subFrame,text='Enter Book Name to be added').grid(row=0,column=0)
        self.book_name_entry=tkinter.Entry(self.subFrame)
        self.book_name_entry.grid(row=0,column=1)
        tkinter.Label(self.subFrame,text='Enter Book Author').grid(row=1,column=0)
        self.book_author_entry=tkinter.Entry(self.subFrame)
        self.book_author_entry.grid(row=1,column=1)
        tkinter.Label(self.subFrame,text='Enter Amount').grid(row=2,column=0)
        self.amount_entry=tkinter.Entry(self.subFrame)
        self.amount_entry.grid(row=2,column=1)
        proceed_btn=tkinter.Button(self.subFrame,text='Proceed',command=self.addBook)
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
        cancel_btn=tkinter.Button(self.subFrame,text='Cancel',command=self.cancel)
        cancel_btn.grid(row=3,column=0)
        proceed_btn=tkinter.Button(self.subFrame,text='Proceed')
        proceed_btn.grid(row=3,column=1)
        
        self.subFrame.grid(row=0,column=1,rowspan=7)
    def showUpdateBook(self):pass
    def cancel(self):
        self.subFrame.destroy()

    #bunch of actions called by the callbacks
    def deleteUser(self):
        if self.email_entry.get()!='':
            # Making a tuple
            arg=(self.email_entry.get(),)
            if(services.deleteUser(arg)):
                messagebox.showinfo('Success','Record having email '+self.email_entry.get()+' has been deleted ')
            else:
                messagebox.showerror('Failed','Couldn\'t delete the record. Contact support team')
        else:
            messagebox.showinfo('Missing field','Please check that you have filled all the fields correctly.')
    def addBook(self):
        if self.book_name_entry.get()!='' and self.book_author_entry!='' and self.amount_entry!='':
            # Here goes the code for code module
            # Creating the argument tuple
            book=(self.book_name_entry.get(),self.book_author_entry.get(),self.amount_entry.get())
            services.addBook(book)
        else:
            messagebox.showinfo('Missing field','Please check that you have filled all the fields correctly.')


if __name__=='__main__':
    master=tkinter.Tk()
    admin=Admin(master)
    master.mainloop()
