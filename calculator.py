
import tkinter as tk

def add():
    result.set(float(e1.get()) + float(e2.get()))

def sub():
    result.set(float(e1.get()) - float(e2.get()))

def mul():
    result.set(float(e1.get()) * float(e2.get()))

def div():
    try:
        result.set(float(e1.get()) / float(e2.get()))
    except:
        result.set("Error")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")

tk.Label(root, text="Number 1").pack()
e1 = tk.Entry(root)
e1.pack()

tk.Label(root, text="Number 2").pack()
e2 = tk.Entry(root)
e2.pack()

result = tk.StringVar()
tk.Label(root, text="Result").pack()
tk.Entry(root, textvariable=result).pack()

tk.Button(root, text="Add", command=add).pack()
tk.Button(root, text="Subtract", command=sub).pack()
tk.Button(root, text="Multiply", command=mul).pack()
tk.Button(root, text="Divide", command=div).pack()

root.mainloop()
