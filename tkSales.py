import tkinter as tk
import matplotlib.pyplot as plt
from datetime import datetime

root = tk.Tk()
root.geometry("700x300")
ent = tk.Entry()
ent2 = tk.Entry()
productLisBx = tk.Listbox()
amountLisBx = tk.Listbox()
lis = []
productLis = []

def addLis():
    amountLisBx.insert(tk.END, ent2.get())
    productLisBx.insert(tk.END, ent.get())

    lis.append(ent.get())
    ent.delete(0,tk.END)

    productLis.append(float(ent2.get()))
    ent2.delete(0,tk.END)

def showGraph():
    plt.plot(lis, productLis, color='red', marker='*')
    plt.bar(lis, productLis)
    plt.title(f"Sales for {datetime.now().strftime("%B %Y")}")
    plt.show()

btn = tk.Button(text="add", command=addLis)
btn2 = tk.Button(text="Show graph", command=showGraph)

lb = tk.Label(text="Enter a product")
lb2 = tk.Label(text="Enter amount")
lb3 = tk.Label(text="producs")
lb4 = tk.Label(text="amounts")
lb.place(x=20, y=0)
ent.place(x=0, y=50)
lb2.place(x=200, y=0)
ent2.place(x=200, y=50)
btn.place(x=100, y=200)
btn2.place(x=200, y=200)
lb3.place(x=400, y=0)
productLisBx.place(x=400, y=20)
lb4.place(x=505, y=0)
amountLisBx.place(x=505, y=20)
root.mainloop()