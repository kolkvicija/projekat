from tkinter import *
from tkinter import messagebox

FONT = ("Courier New", 10)

win = Tk()
win.title("Banka")
win.config(pady=50, padx=50)


def pop():
    """Otvara novi prozor nakon odabira banke."""
    popup = Toplevel()
    popup.title("Forma")
    popup.config(pady=50, padx=50)

    name = Label(popup, text="Ime: ")
    name.grid(row=0, column=0)
    surname = Label(popup, text="Prezime: ")
    surname.grid(row=1, column=0)
    amount = Label(popup, text="Iznos: ")
    amount.grid(row=2, column =0)
    pin = Label(popup, text="Pin: ")
    pin.grid(row=3, column=0)

    def ok_cancel():
        """Zapisuje unesene podatke, a ukoliko su polja prazna, vaća grešku."""
        if name_entry.get() == "" or surname_entry.get() == "" or pin_entry.get() == "" or amount_entry.get() == "":
            messagebox.showwarning(title="Greška!", message="Polja ne smiju biti prazna.")
        elif name_entry and surname_entry and pin_entry and amount_entry:
            # with open("data.txt", "a") as data:
            #     data.write(f"\n{name_entry.get()} | {surname_entry.get()} | {pin_entry.get()}")
            popup.destroy()

    ok = Button(popup, text="Potvrdi", command=ok_cancel)
    ok.grid(row=4, column=1)
    cancel = Button(popup, text="Poništi", command=popup.destroy)
    cancel.grid(row=4, column=2)

    # Unos podataka
    name_entry = Entry(popup, width=30)
    name_entry.focus()
    name_entry.grid(row=0, column=1, columnspan=2, pady=5)
    surname_entry = Entry(popup, width=30)
    surname_entry.grid(row=1, column=1, columnspan=2, pady=5)
    amount_entry = Entry(popup, width=30)
    amount_entry.grid(row=2, column=1, columnspan=2, pady=5)
    pin_entry = Entry(popup, width=30, show='*')
    pin_entry.grid(row=3, column=1, columnspan=2, pady=5)
    popup.mainloop()


# Izbor banke
label = Label(text="Odaberite banku: ", pady=20, font=FONT)
label.grid(row=0, column=0)

one = Button(text="UniCredit Bank", command=pop, height=3, width=13, font=FONT, padx=10, pady=10)
one.grid(row=1, column=0)

two = Button(text="Nova Banka", command=pop, height=3, width=13, font=FONT, padx=10, pady=10)
two.grid(row=1, column=1)

three = Button(text="Addiko Bank", command=pop, height=3, width=13, font=FONT, padx=10, pady=10)
three.grid(row=2, column=0)

four = Button(text="Raiffeisen Bank", command=pop, height=3, width=13, font=FONT, padx=10, pady=10)
four.grid(row=2, column=1)

five = Button(text="MF Banka", command=pop, height=3, width=13, font=FONT, padx=10, pady=10)
five.grid(row=3, column=0)

six = Button(text="NLB Banka", command=pop, height=3, width=13, font=FONT, padx=10, pady=10)
six.grid(row=3, column=1)
win.mainloop()
