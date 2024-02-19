import tkinter as tk

def button_click(char):
  global current
  current += str(char)
  text_input.delete(0, tk.END)
  text_input.insert(0, current)

def button_clear():
  global current
  current = ""
  text_input.delete(0, tk.END)

def button_equal():
  global current
  try:
    result = eval(current)
    current = str(result)
    text_input.delete(0, tk.END)
    text_input.insert(0, current)
  except SyntaxError:
    current = "Error"
    text_input.delete(0, tk.END)
    text_input.insert(0, current)

root = tk.Tk()
root.title("Simple Calculator")

current = ""
text_input = tk.Entry(root, width=35, borderwidth=5)
text_input.grid(columnspan=4)

buttons = [[7, 8, 9, "/"],
           [4, 5, 6, "*"],
           [1, 2, 3, "-"],
           [0, ".", "=", "+"]]

for i in range(4):
  for j in range(4):
    button = tk.Button(root, text=str(buttons[i][j]), command=lambda char=buttons[i][j]: button_click(char))
    button.grid(row=i+1, column=j)

clear_button = tk.Button(root, text="C", command=button_clear)
clear_button.grid(row=1, column=4)
equal_button = tk.Button(root, text="=", command=button_equal)
equal_button.grid(row=4, column=4)

root.mainloop()