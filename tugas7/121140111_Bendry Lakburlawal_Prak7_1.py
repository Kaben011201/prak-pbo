import tkinter as tk
from tkinter import messagebox

def celcius():
    try:
        check = entry.get()
        if not check:
            raise ValueError("Masukkan Nilai Suhu")
        f = (float(entry.get()) * 9/5) + 32
        r = (float(entry.get()) * 4/5)
        k = (float(entry.get()) + 273.15)
        result.config(text="Reamur : " + str(r) + "\nFaranheit : " + str(f) + "\nKelvin : " + str(k))
    except ValueError as err:
        messagebox.showerror("Error",str(err))

def reamur():
    try:
        check = entry.get()
        if not check:
            raise ValueError("Masukkan Nilai Suhu")
        c = (float(entry.get()) * 5/4)
        f = (float(entry.get()) * 9/4) + 32
        k = (float(entry.get()) * 5/4) + 273.15
        result.config(text="Celcius : " + str(c) + "\nFaranheit : " + str(f) + "\nKelvin : " + str(k))
    except ValueError as err:
        messagebox.showerror("Error",str(err))

def faranheit():
    try:
        check = entry.get()
        if not check:
            raise ValueError("Masukkan Nilai Suhu")
        c = (float(entry.get()) - 32) * 5/9
        r = (float(entry.get()) - 32) * 4/9
        k = ((float(entry.get()) - 32) * 5/9) + 273.15
        result.config(text="Celcius : " + str(c) + "\nReamur : " + str(r) + "\nKelvin : " + str(k))
    except ValueError as err:
        messagebox.showerror("Error",str(err))
    
def kelvin():
    try:
        check = entry.get()
        if not check:
            raise ValueError("Masukkan Nilai Suhu")
        c = (float(entry.get()) - 273.15)
        r = (float(entry.get()) - 273.15) * 4/5
        f = ((float(entry.get()) - 273.15) * 9/5)+32
        result.config(text="Celcius : " + str(c) + "\nReamur : " + str(r) + "\nFaranheit : " + str(f))
    except ValueError as err:
        messagebox.showerror("Error",str(err))
    

root = tk.Tk()
root.title("Konversi Suhu")
root.geometry("300x190")

label1 = tk.Label(root, text="Masukkan suhu:", font=("Arial", 10))
label1.pack()
entry = tk.Entry(root)
entry.pack()
label2 = tk.Label(root, text="Asal Suhu:", font=("Arial", 10))
label2.pack()
buttonframe  = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)

button1 = tk.Button(buttonframe, text="Celcius", font=("Arial", 10), bg="silver", command=celcius)
button1.grid(row=1, column=0, sticky='we')
button2 = tk.Button(buttonframe, text="Reamur", font=("Arial", 10), bg="silver", command=reamur)
button2.grid(row=1, column=1, sticky='we')
button3 = tk.Button(buttonframe, text="Faranheit", font=("Arial", 10), bg="silver", command=faranheit)
button3.grid(row=1, column=2, sticky='we')
button4 = tk.Button(buttonframe, text="Kelvin", font=("Arial", 10), bg="silver", command=kelvin)
button4.grid(row=1, column=3, sticky='we')
buttonframe.pack()

label3 = tk.Label(root, text="Hasil", font=("Arial", 10))
label3.pack()
result = tk.Label(root, font=("Arial", 10))
result.pack()

root.mainloop()
