import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class RegistrationForm():
   
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Form")
        self.root.geometry("400x300")

        self.create_frames()
        self.create_title_label()
        self.create_name_entry()
        self.create_email_entry()
        self.create_password_entry()
        self.create_terms_checkbox()
        self.create_submit_button()

    def create_frames(self):
        self.title_frame = ttk.Frame(self.root)
        self.title_frame.pack(pady=10)
        self.details_frame = ttk.Frame(self.root)
        self.details_frame.pack(pady=10)
        self.button_frame = ttk.Frame(self.root)
        self.button_frame.pack(pady=10)

    def create_title_label(self):
        self.title_label = ttk.Label(self.title_frame,
                                     text="Registration Form",
                                     font=("Arial", 16))
        self.title_label.pack()

    def create_name_entry(self):
        self.name_label = ttk.Label(self.details_frame, text="Full Name:")
        self.name_label.pack()
        self.name_entry = ttk.Entry(self.details_frame, width=30)
        self.name_entry.pack()

    def create_email_entry(self):
        self.email_label = ttk.Label(self.details_frame, text="Email:")
        self.email_label.pack()
        self.email_entry = ttk.Entry(self.details_frame, width=30)
        self.email_entry.pack()

    def create_password_entry(self):
        self.password_label = ttk.Label(self.details_frame, text="Password:")
        self.password_label.pack()
        self.password_entry = ttk.Entry(self.details_frame, width=30, show="*")
        self.password_entry.pack()
        self.show_password_checkbox_var = tk.IntVar()
        self.show_password_checkbox = ttk.Checkbutton(self.details_frame,
                                                       text="Show Password",
                                                       variable=self.show_password_checkbox_var,
                                                       command=self.toggle_password_visibility)
        self.show_password_checkbox.pack()

    def create_terms_checkbox(self):
        self.terms_label = ttk.Label(self.details_frame,
                                      text="I agree to the terms and conditions:")
        self.terms_label.pack()
        self.terms_checkbox_var = tk.IntVar()
        self.terms_checkbox = ttk.Checkbutton(self.details_frame, variable=self.terms_checkbox_var)
        self.terms_checkbox.pack()

    def create_submit_button(self):
        self.submit_button = ttk.Button(self.button_frame,
                                         text="Submit",
                                         command=self.validate_and_submit)
        self.submit_button.pack()

    def toggle_password_visibility(self):
        if self.show_password_checkbox_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def validate_and_submit(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()

        if not name:
            messagebox.showerror("Error", "Please enter your full name.")
            return
        if not email or "@" not in email:
            messagebox.showerror("Error", "Please enter a valid email address.")
            return
        if not password:
            messagebox.showerror("Error", "Please enter a password.")
            return
        if not self.terms_checkbox_var.get():
            messagebox.showerror("Error", "Please agree to the terms and conditions.")
            return

        print(
            f"Registration successful!\nName: {name}\nEmail: {email}\nPassword: {password}"
        )
        messagebox.showinfo("Success", "Thank you for registering! Your information has been submitted.")

        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.terms_checkbox_var.set(0)


if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationForm(root)
    root.mainloop()
