import tkinter as tk
class Prime_check_app:
    def __init__(self , mainwindow):
        self.mainwindow = mainwindow

        tk.Label(mainwindow , text = 'Enter the Number' , bg='magenta').pack()
        
        self.number_entry = tk.Entry(root)
        self.number_entry.pack()

        self.click = tk.Button(mainwindow , text='Check' , command=self.prime_or_not , bg='red')
        self.click.pack()

        self.outLabel = tk.Label(mainwindow , text='' , bg='yellow')
        self.outLabel.pack()

# ================================================================================================================

    def prime_or_not(self):
        try:
            data = int(self.number_entry.get())
            prime = True

            if data <= 1:
                prime = False
            else:
                for i in range(2, int(data**0.5) + 1):
                    if data % i == 0:
                        prime = False
                        break

            if prime:
                self.outLabel.config(text="This is prime")
            else:
                self.outLabel.config(text="This number is not prime")

        except ValueError:
            self.outLabel.config(text="Please enter a valid integer")

# ====================================================================================================================

# Main code
root = tk.Tk()
exc = Prime_check_app(root)
root.mainloop()