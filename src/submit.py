from tkinter import messagebox
import tkinter
class Submit:
    def submit(self):
        MsgBox = messagebox.askquestion ('SUBMIT','Are you sure you want to Submit?',icon = 'warning')
        if MsgBox == 'yes':
            messagebox.showinfo('Save','Submitted.......')
        else:
            messagebox.showinfo('Return','Returning to the page..........')
    def request(self):
        messagebox.showinfo('REQUEST','Your Request has been recorded.......')
    def __init__(self,master):
        master.config(bg="light steel blue")
        tkinter.Label(master, text="Book Name: ",bg="light steel blue",font=('Comic Sans MS',18)).grid(row=1,column=0)
        bookname_entry=tkinter.Entry(master, bd=3,bg="light grey")
        bookname_entry.grid(row=1,column=1)
        tkinter.Label(master, text="Book Author: ",bg="light steel blue",font=('Comic Sans MS',18)).grid(row=2,column=0)
        author_entry=tkinter.Entry(master, bd=3,bg="light grey")
        author_entry.grid(row=2,column=1)
        tkinter.Label(master, text="Quanity: ",justify=tkinter.LEFT,bg="light steel blue",font=('Comic Sans MS',18)).grid(row=3,column=0)
        quantity_entry=tkinter.Entry(master, bd=3,bg="light grey")
        quantity_entry.grid(row=3,column=1)
        tkinter.Label(master, text="Price(Rs): ",bg="light steel blue",font=('Comic Sans MS',18)).grid(row=4,column=0)
        price_entry=tkinter.Entry(master, bd=3,bg="light grey")
        price_entry.grid(row=4,column=1)
        submit_btn=tkinter.Button(master,text='Submit',relief=tkinter.GROOVE,bg="orange",activebackground="white",command=self.submit,fg="red",width=10,font=('Comic Sans MS bold',13))
        submit_btn.grid(row=5,column=0)
        request_btn=tkinter.Button(master,text='Request',relief=tkinter.GROOVE,bg="orange",activebackground="white",command=self.request,fg="red",width=10,font=('Comic Sans MS bold',13))
        request_btn.grid(row=5,column=1)
        canvas =tkinter.Canvas(master,width = 350, height = 450,bd=4,highlightbackground="black")
        canvas.grid(row=1,column=6,rowspan=5,padx=20,pady=10)
        self.img = tkinter.PhotoImage(file="images/books1.gif")
        canvas.create_image(0,0,anchor=tkinter. N,image=self.img)      
    

if __name__=='__main__':
    master=tkinter.Tk()
    Submit(master)
    master.mainloop()
