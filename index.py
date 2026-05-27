import tkinter as tk
import math

# ---------- Functions ----------
def press(val):
    entry.insert(tk.END, val)

def clear():
    entry.delete(0, tk.END)

def backspace():
    entry.delete(len(entry.get())-1, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def replace(val):
    entry.delete(0, tk.END)
    entry.insert(0, str(val))

# Scientific
def sin(): replace(math.sin(math.radians(float(entry.get()))))
def cos(): replace(math.cos(math.radians(float(entry.get()))))
def tan(): replace(math.tan(math.radians(float(entry.get()))))
def sinh(): replace(math.sinh(float(entry.get())))
def cosh(): replace(math.cosh(float(entry.get())))
def tanh(): replace(math.tanh(float(entry.get())))
def log(): replace(math.log10(float(entry.get())))
def exp(): replace(math.exp(float(entry.get())))
def reciprocal(): replace(1/float(entry.get()))
def square(): replace(float(entry.get())**2)
def cube(): replace(float(entry.get())**3)
def factorial(): replace(math.factorial(int(entry.get())))
def percent(): replace(float(entry.get())/100)

def plus_minus():
    try:
        replace(-float(entry.get()))
    except:
        pass

# ---------- Window ----------
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("420x520")
root.configure(bg="#2FA4D7")

# Make grid responsive
for i in range(8):
    root.rowconfigure(i, weight=1)
for j in range(5):
    root.columnconfigure(j, weight=1)

# Entry
entry = tk.Entry(root, font=("Arial", 22), bd=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=10, pady=10)

# Button style
btn = {"bg": "white", "fg": "black", "font": ("Arial", 12)}

# Button creator (auto resize)
def make_btn(text, r, c, cmd, cs=1):
    tk.Button(root, text=text, command=cmd, **btn)\
        .grid(row=r, column=c, columnspan=cs, sticky="nsew", padx=4, pady=4)

# ---------- Buttons ----------
make_btn("R",1,0,clear)
make_btn("exp",1,1,exp)
make_btn("Sin",1,2,sin)
make_btn("Cos",1,3,cos)
make_btn("Tan",1,4,tan)

make_btn("1/X",2,0,reciprocal)
make_btn("Log",2,1,log)
make_btn("sinh",2,2,sinh)
make_btn("Cosh",2,3,cosh)
make_btn("Tanh",2,4,tanh)

make_btn("X^Y",3,0,lambda: press("**"))
make_btn("%",3,1,percent)
make_btn("C",3,2,clear)
make_btn("←",3,3,backspace)
make_btn("+",3,4,lambda: press("+"))

make_btn("X^3",4,0,cube)
make_btn("7",4,1,lambda: press("7"))
make_btn("8",4,2,lambda: press("8"))
make_btn("9",4,3,lambda: press("9"))
make_btn("-",4,4,lambda: press("-"))

make_btn("X^2",5,0,square)
make_btn("4",5,1,lambda: press("4"))
make_btn("5",5,2,lambda: press("5"))
make_btn("6",5,3,lambda: press("6"))
make_btn("*",5,4,lambda: press("*"))

make_btn("n!",6,0,factorial)
make_btn("1",6,1,lambda: press("1"))
make_btn("2",6,2,lambda: press("2"))
make_btn("3",6,3,lambda: press("3"))
make_btn("/",6,4,lambda: press("/"))

make_btn("+/-",7,0,plus_minus)
make_btn("0",7,1,lambda: press("0"))
make_btn(".",7,2,lambda: press("."))

# Big "=" button
tk.Button(root, text="=", command=calculate, bg="green", fg="white",
          font=("Arial", 14)).grid(row=7, column=3, columnspan=2,
                                   sticky="nsew", padx=4, pady=4)

# Run
root.mainloop()