#this program coded in Python can solve equations in second degree.

from tkinter import *
from math import sqrt

def supprimer():
    global fen, entr1, entr2, entr3, entr4, entr5, txt4, txt5, delete
    entr1.delete(0, END)    
    entr2.delete(0, END)
    entr3.delete(0, END)
    entr4.destroy()
    entr5.destroy()
    txt4.destroy()
    txt5.destroy()

    
def calculer():
    global fen, entr1, entr2, entr3, entr4, entr5, txt4, txt5

    try:
        a = int(entr1.get())
        b = int(entr2.get())
        c = int(entr3.get())
        
        delta = (b**2-4*a*c)
        if (delta > 0):
            x1 = (-b+sqrt(delta)/2*a)
            x2 = (-b-sqrt(delta)/2*a)
            txt4.grid(row=4, column=0)
            txt5.grid(row=5, column=0)

            entr4.grid(row=4, column=1)
            entr5.grid(row=5, column=1)
            entr4.insert(0, x1)
            entr5.insert(0, x2)
            
        if (delta < 0):
            messagebox.showinfo("Fin de l'exercice", "L'équation n'admet aucune solution!")
                
        if (delta == 0):
            x0 = (-b/2*a)
            txt4.grid(row=4, column=0)
            entr4.grid(row=4, column=1)
            entr4.insert(0, x0)

    except ValueError:
        messagebox.showerror("Erreur", "Erreur de valeur!")
        
def alert():
    messagebox.showinfo("Info", "Programme créé par Abderrahmane El Mimouni.""\n""Et encadré par El Hassan El Mimouni.")
    
def widgets():
    global fen, entr1, entr2, entr3, entr4, entr5, txt4, txt5

    fen = Tk()
    fen.title("Equations resolver")
    fen.geometry("260x189")

    menubar = Menu(fen)

    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label="A propos", command=alert)
    menubar.add_cascade(label="Aide", menu=menu1)

    fen.config(menu=menubar)
    
    txt0 = Label(fen, text="équation", font=("Times", 16, "bold", "italic"), fg="red")
    txt01 = Label(fen, text="ax² + bx + c = 0", font=("Times", 16, "bold", "italic"), fg="red")
    txt1 = Label(fen, text="a:", font=("Times", 12))
    txt2 = Label(fen, text="b:", font=("Times", 12))
    txt3 = Label(fen, text="c:", font=("Times", 12))
    txt4 = Label(fen, text="x1:", font=("Times", 12))
    txt5 = Label(fen, text="x2:", font=("Times", 12))

    entr1 = Entry(fen, font=("Times", 12))
    entr2 = Entry(fen, font=("Times", 12))
    entr3 = Entry(fen, font=("Times", 12))
    entr4 = Entry(fen, font=("Times", 12))
    entr5 = Entry(fen, font=("Times", 12))

    txt0.grid(row=0, column=0)
    txt01.grid(row=0, column=1)
    txt1.grid(row=1, column=0)
    txt2.grid(row=2, column=0)
    txt3.grid(row=3, column=0)

    entr1.grid(row=1, column=1)
    entr2.grid(row=2, column=1)
    entr3.grid(row=3, column=1)

    btn1 = Button(fen, text="Résoudre", font=("Times", 13), command=calculer)
    btn1.grid(row=6, column=1)

    btn2= Button(fen, text="Refaire", font=("Times", 13), command=supprimer)
    btn2.grid(row=6, column=0)
    
    fen.mainloop()

widgets()
