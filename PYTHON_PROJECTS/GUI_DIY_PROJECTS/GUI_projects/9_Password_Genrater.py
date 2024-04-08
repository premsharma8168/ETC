import tkinter as tk
import random

class PassGenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_label = tk.Label(root , text='Password Length:')
        self.length_label.pack()
        self.length_entry = tk.Entry(root)
        self.length_entry.pack()
        self.length_entry.insert(0 , '6')
        self.uppercase_var = tk.IntVar()
        self.lowercase_var = tk.IntVar()
        self.numbers_var = tk.IntVar() 
        self.symbols_var = tk.IntVar()


        self.uppercase_check = tk.Checkbutton(root, text="Uppercase", variable=self.uppercase_var)
        self.lowercase_check = tk.Checkbutton(root, text="Lowercase", variable=self.lowercase_var)
        self.numbers_check = tk.Checkbutton(root, text="Numbers", variable=self.numbers_var)
        self.symbols_check = tk.Checkbutton(root, text="Symbols", variable=self.symbols_var)
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def generate_password(self):
        length = int(self.length_entry.get())
        characters = ""
        if self.uppercase_check:
            characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if self.lowercase_check:
            characters += "abcdefghijklmnopqrstuvwxyz"
        if self.numbers_check:
            characters += "0123456789"
        if self.symbols_check:
            characters += "!#$%&*?@^_~"
        
        if not characters:
            self.result_label.config(text="Please select at least one character set.")
            return


        password = ""
        for i in range(length):
            password += random.choice(characters)
        self.result_label.config(text=f"Generated Password: {password}")


root = tk.Tk()
app = PassGenApp(root)
root.geometry('500x400')
root.mainloop()