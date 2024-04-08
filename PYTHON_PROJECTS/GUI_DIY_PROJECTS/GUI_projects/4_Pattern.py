import tkinter as tk
class Pattern_app:
    def __init__(self , mainwindow):
        self.mainwindow = mainwindow

        tk.Label(mainwindow , text = 'Enter the Number for ROW' , bg='magenta').pack()
        
        self.number_entry = tk.Entry(root)
        self.number_entry.pack()

        self.click = tk.Button(mainwindow , text='Print Pattern' , command=self.design , bg='red')
        self.click.pack()

        self.outLabel = tk.Label(mainwindow , text='' , bg='yellow')
        self.outLabel.pack()
        root.configure(bg='black')

# ======================================================================================================================

    def design(self):
        try:
            data = int(self.number_entry.get())
            pattern = ''
            
            for i in range(1, data+1):
                pattern += '*' * i + '\n'
            
            self.outLabel.config(text=pattern)

        except ValueError:
            self.outLabel.config(text="Please enter a valid integer")

# ===============================================================================================================

# Main code
root = tk.Tk()
exc = Pattern_app(root)
root.mainloop()