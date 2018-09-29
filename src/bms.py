'''
Created on Sep 29, 2018
@author: Rajdeep Roy Chowdhury
Licensed Under MIT
'''
# This is the kickstarter
import tkinter
from core.config import *
from ui.register import Register

class MainWindow:
    def __init__(self,master):
        self.master=master
        master.title(TITLE)
        master.geometry(str(DISPLAY_WIDTH)+'x'+str(DISPLAY_HEIGHT))
        master.resizable(0,0)


if __name__=='__main__':
    root=tkinter.Tk()
    MainWindow(root)
    root.mainloop()