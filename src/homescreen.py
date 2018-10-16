'''
Created on Oct 13, 2018
@author: Rajdeep Roy Chowdhury
Licensed under MIT
'''
import tkinter
class HomeScreen:
    def __init__(self,master):
        self.master=master
        tkinter.Label(self.master,text="Welcome to Book Management System").grid(row=1,column=1)

if __name__=='__main__':
    root=tkinter.Tk()
    HomeScreen(root)
    root.mainloop()