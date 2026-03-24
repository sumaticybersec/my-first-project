import tkinter as tk
import datetime

root = tk.Tk()
root.title("Coffee Shop Billing System")
root.geometry("520x550")
root.configure(bg="lightyellow")

prices = {
    "Coffee":50,
    "Cappuccino":70,
    "Latte":80,
    "Sandwich":60,
    "Cake":90
}

coffee = tk.IntVar()
cappuccino = tk.IntVar()
latte = tk.IntVar()
sandwich = tk.IntVar()
cake = tk.IntVar()

def calculate_bill():

    receipt.delete("1.0",tk.END)

    total = 0
    now = datetime.datetime.now()

    receipt.insert(tk.END,"☕ Coffee Shop Receipt ☕\n")
    receipt.insert(tk.END,"Date: "+str(now)+"\n")
    receipt.insert(tk.END,"-----------------------------\n")

    if coffee.get()>0:
        price = coffee.get()*prices["Coffee"]
        receipt.insert(tk.END,f"Coffee x{coffee.get()} = ₹{price}\n")
        total += price

    if cappuccino.get()>0:
        price = cappuccino.get()*prices["Cappuccino"]
        receipt.insert(tk.END,f"Cappuccino x{cappuccino.get()} = ₹{price}\n")
        total += price

    if latte.get()>0:
        price = latte.get()*prices["Latte"]
        receipt.insert(tk.END,f"Latte x{latte.get()} = ₹{price}\n")
        total += price

    if sandwich.get()>0:
        price = sandwich.get()*prices["Sandwich"]
        receipt.insert(tk.END,f"Sandwich x{sandwich.get()} = ₹{price}\n")
        total += price

    if cake.get()>0:
        price = cake.get()*prices["Cake"]
        receipt.insert(tk.END,f"Cake x{cake.get()} = ₹{price}\n")
        total += price

    receipt.insert(tk.END,"-----------------------------\n")
    receipt.insert(tk.END,"Total Bill = ₹"+str(total))


def reset():
    coffee.set(0)
    cappuccino.set(0)
    latte.set(0)
    sandwich.set(0)
    cake.set(0)
    receipt.delete("1.0",tk.END)


def save_bill():
    bill_data = receipt.get("1.0",tk.END)

    file = open("bill.txt","a")
    file.write(bill_data)
    file.write("\n\n")
    file.close()


tk.Label(root,text="☕ Coffee Shop Billing System ☕",
font=("Arial",20,"bold"),bg="lightyellow").pack(pady=10)

frame = tk.Frame(root,bg="lightyellow")
frame.pack()

tk.Label(frame,text="Coffee ₹50",bg="lightyellow").grid(row=0,column=0,padx=10,pady=5)
tk.Entry(frame,textvariable=coffee,width=5).grid(row=0,column=1)

tk.Label(frame,text="Cappuccino ₹70",bg="lightyellow").grid(row=1,column=0,padx=10,pady=5)
tk.Entry(frame,textvariable=cappuccino,width=5).grid(row=1,column=1)

tk.Label(frame,text="Latte ₹80",bg="lightyellow").grid(row=2,column=0,padx=10,pady=5)
tk.Entry(frame,textvariable=latte,width=5).grid(row=2,column=1)

tk.Label(frame,text="Sandwich ₹60",bg="lightyellow").grid(row=3,column=0,padx=10,pady=5)
tk.Entry(frame,textvariable=sandwich,width=5).grid(row=3,column=1)

tk.Label(frame,text="Cake ₹90",bg="lightyellow").grid(row=4,column=0,padx=10,pady=5)
tk.Entry(frame,textvariable=cake,width=5).grid(row=4,column=1)

tk.Button(root,text="Generate Bill",
command=calculate_bill,
bg="green",fg="white",
font=("Arial",12)).pack(pady=10)

tk.Button(root,text="Save Bill",
command=save_bill,
bg="blue",fg="white",
font=("Arial",12)).pack(pady=5)

tk.Button(root,text="Reset",
command=reset,
bg="red",fg="white",
font=("Arial",12)).pack(pady=5)

receipt = tk.Text(root,height=12,width=42)
receipt.pack(pady=10)

root.mainloop()