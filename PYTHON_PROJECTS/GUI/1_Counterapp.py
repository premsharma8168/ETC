import tkinter as tk

class counterApp:
    def __init__(self, mainwindow):
        self.mainwindow=mainwindow
        mainwindow.geometry('2000x1000')
        mainwindow.title('Counter App')
        mainwindow.maxsize(200 , 100) 
        mainwindow.maxsize(800 , 800)
        mainwindow.minsize(50 , 50)
        self.var=tk.IntVar(value=0)

# ===================================================================================================================================

        # add widget
        self.lbl1 = tk.Label(mainwindow, bg='yellow' , textvariable=self.var,font=('BOLD',60))
        self.lbl1.pack()


        self.btn1=tk.Button(mainwindow, text='Increment', command=self.increment , bg='green' , font=('BOLD',30))
        self.btn1.pack(side=tk.LEFT)

        self.btn2=tk.Button(mainwindow,text='Decrement',command=self.decrement , bg='red' , font=('BOLD',30))
        self.btn2.pack(side=tk.RIGHT)
        root.configure(bg='black')

# ====================================================================================================================================

    #actions
    def increment(self):
        data = self.var.get()+1
        self.var.set(data)
        if  data >= 10:
            self.lbl1.config(fg='green')
        else:
            self.lbl1.config(fg='blue')


    def decrement(self):
        data = self.var.get()-1
        self.var.set(data)
        if data <= 0:
            self.lbl1.config(fg='red')
        elif data <= -10:
            self.lbl1.config(fg='orange')
        else:
            self.lbl1.config(fg='magenta')

# ==============================================================================================================

root =tk.Tk()
exc = counterApp(root)
root.mainloop()
