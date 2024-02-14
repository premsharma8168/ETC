import tkinter as tk
class bmi_app:
    def __init__(self , mainwindow):
        self.mainwindow = mainwindow
        mainwindow.configure()
        tk.Label(root , text='Height').grid(row=0 , column=0 , padx=5 , pady=5)
        tk.Label(root , text='Weight').grid(row=1 , column=0 , padx=5 , pady=5)

        self.weight_entry = tk.Entry(root)
        self.weight_entry.grid(row=0 , column=1 , padx=5 , pady=5 )

        self.height_entry = tk.Entry(root)
        self.height_entry.grid(row=1 , column=1 , padx=5 , pady=5)

        self.click=tk.Button(root , text='Calculate' , command=self.action)
        self.click.grid(row=2 , column=2 , columnspan=2)
        
        self.outLabel = tk.Label(mainwindow , text='' , bg='yellow')
        self.outLabel.grid()

# ======================================================================================================================
    def action(self):

        weight = float(self.weight_entry.get())
        height = float(self.height_entry.get())
        bmi=weight/(height**2)
        self.outLabel.configure(text=f'your bmi is {bmi:.2f}')

# ====================================================================================================================

# Main code
root = tk.Tk()
exc = bmi_app(root)
root.mainloop()