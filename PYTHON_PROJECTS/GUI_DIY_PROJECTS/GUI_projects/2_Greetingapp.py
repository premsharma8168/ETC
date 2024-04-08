import tkinter as tk
class Greetingapp:
    def __init__(self , mainwindow):
        self.mainwindow = mainwindow

        tk.Label(mainwindow , text = 'Enter Your Name' , bg='magenta').pack()
        
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.click = tk.Button(mainwindow , text='Enter' , command=self.Greet , bg='red')
        self.click.pack()

        self.outLabel = tk.Label(mainwindow , text='' , bg='yellow')
        self.outLabel.pack()

# ========================================================================================================================================

    def Greet(self):
        data = self.name_entry.get()
        self.outLabel.config(text='Hello,'+data)
        self.name_entry.delete(0 , tk.END)

# ========================================================================================================================================

# Main code
root = tk.Tk()
exc = Greetingapp(root)
root.mainloop()