# @TODO
import tkinter
from core.services import registerUser
class Admin:
    def __init__(self,master):
        self.master=master
        show_all_users_btn=tkinter.Button(master,text='Show all users')
        show_all_users_btn.grid(row=0,column=0)
        add_user_btn=tkinter.Button(master,text='Add user')
        add_user_btn.grid(row=1,column=0)
        delete_user_btn=tkinter.Button(master,text='Delete User')
        delete_user_btn.grid(row=2,column=0)
        update_user_btn=tkinter.Button(master,text='Update User')
        update_user_btn.grid(row=3,column=0)
        view_order_btn=tkinter.Button(master,text='View Orders')
        view_order_btn.grid(row=4,column=0)
        add_book_btn=tkinter.Button(master,text='Add Book')
        add_book_btn.grid(row=5,column=0)
        delete_book_btn=tkinter.Button(master,text='Delete Book')
        delete_book_btn.grid(row=6,column=0)
        update_book_btn=tkinter.Button(master,text='Update Book')
        update_book_btn.grid(row=7,column=0)
        self.subFrame=tkinter.Frame(master,bg='red')
        tkinter.Label(self.subFrame,text='hello').pack() # Here goes the subFrame
        self.subFrame.grid(row=0,column=1,rowspan=7)
    
    #Bunch of button callbacks
    def showAllUsers(self):
        self.subFrame.destroy()
        self.subFrame=tkinter.Frame(master,bg='red')
        tkinter.Label(self.subFrame,text='hello').pack() # Here goes the subFrame
        self.subFrame.grid(row=0,column=1,rowspan=7)
    def showAddUser(self):pass
    def showDeleteUser(self):pass
    def showUpdateUser(self):pass
    def showViewOrders(self):pass
    def showAddBook(self):pass
    def showDeleteBook(self):pass
    def showUpdateBook(self):pass



if __name__=='__main__':
    master=tkinter.Tk()
    admin=Admin(master)
    master.mainloop()
