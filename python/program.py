from tkinter import *
# // from tkinter import * // doesn't import messagebox it has to be explicitly imported
from tkinter import messagebox
from math import *

def info():
    messagebox.showinfo("Info", "Equations resolver v1.3 est un programme créé par Abderrahmane El Mimouni.""\n""Et encadré par El Hassan El Mimouni.")

def aide():
    messagebox.showinfo("Info", "En cours de développement.")

def equation1():
    global fen

    def tout_refaire():
        global txt0, txt1, txt2, txt3, txt4, entr1, entr2, entr3, entr4, btn1, btn2, btn3
        
        txt0.destroy()
        txt1.destroy()
        txt2.destroy()
        txt3.destroy()
        txt4.destroy()
        entr1.destroy()
        entr2.destroy()
        entr3.destroy()
        entr4.destroy()
        btn1.destroy()
        btn2.destroy()
        btn3.destroy()
        
    def refaire():
        global entr1, entr2, entr3, entr4
        entr1.delete(0, END)
        entr2.delete(0, END)
        entr3.delete(0, END)
        entr4.delete(0, END)
    
    def Calculer():
        global fen, entr1, entr2, entr3, entr4, btn1

        try:
            a = int(entr1.get())
            b = int(entr2.get())
            c = int(entr3.get())
            x = (c-b)/a
            entr4.config(bg="white", fg="black")
            entr4.delete(0, END)
            entr4.insert(0, x)

        except ValueError:
            messagebox.showerror("Erreur", "Erreur de valeur")
            
        except ZeroDivisionError:
            messagebox.showerror("Erreur", "Erreur de division par 0")

    def CreateWidgets():
        global fen, txt0, txt1, txt2, txt3, txt4, entr1, entr2, entr3, entr4, btn1, btn2, btn3

        txt0 = Label(fen, text = 'Equation ax + b = c', fg='red', font=('Times', 16, 'bold', 'italic'))
        txt1 = Label(fen, text = 'a :', font=('Times', 12))
        txt2 = Label(fen, text = 'b :', font=('Times', 12))
        txt3 = Label(fen, text = 'c :', font=('Times', 12))
        txt4 = Label(fen, text = 'x :', font=('Times', 12))
        
        entr1 = Entry(fen, font=('Times', 12))
        entr2 = Entry(fen, font=('Times', 12))
        entr3 = Entry(fen, font=('Times', 12))
        entr4 = Entry(fen, font=('Times', 12))
        
        entr1.delete(0, END)
        entr1.insert(0, "")
        entr2.delete(0, END)
        entr2.insert(0, "")
        entr3.delete(0, END)
        entr3.insert(0, "")
        entr4.delete(0, END)
        entr4.insert(0, "")

        btn1 = Button(fen, text='Résoudre', font=('Times', 12), command=Calculer)
        btn2 = Button(fen, text='Refaire', font=('Times', 12), command=refaire)
        btn3 = Button(fen, text="Tout refaire", font=('Times', 12), command=tout_refaire)

        txt0.grid(row =0, column =1)
        txt1.grid(row =1, column =0)
        txt2.grid(row =2, column =0)
        txt3.grid(row =3, column =0)
        txt4.grid(row =4, column =0)
        
        entr1.grid(row =1, column =1)
        entr2.grid(row =2, column =1)
        entr3.grid(row =3, column =1)
        entr4.grid(row =4, column =1)

        btn1.grid(row =5, column =1)
        btn2.grid(row =5, column =0)
        btn3.grid(row =6, column =1)

    def main():
        global fen, entr1, entr2, entr3, entr4, btn1
        
        CreateWidgets()

    main()

def equation2():
    global fen
    
    def tout_supprimer():
        
        global txt0, txt01, txt1, txt2, txt3, txt4, txt5, entr1, entr2, entr3, entr4, entr5, btn1, btn2, btn3
        
        txt0.destroy()
        txt01.destroy()
        txt1.destroy()
        txt2.destroy()
        txt3.destroy()
        txt4.destroy()
        txt5.destroy()
        entr1.destroy()
        entr2.destroy()
        entr3.destroy()
        entr4.destroy()
        entr5.destroy()
        btn1.destroy()
        btn2.destroy()
        btn3.destroy()
    
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
        global fen, txt0, txt01, txt1, txt2, txt3, txt4, txt5, entr1, entr2, entr3, entr4, entr5, btn1, btn2, btn3
        
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

        btn3= Button(fen, text="Tout Refaire", font=("Times", 13), command=tout_supprimer)
        btn3.grid(row=7, column=1)

    widgets()

def main():
    global fen
    
    fen = Tk()
    fen.title("Equations resolver v1.3")
    fen.geometry("260x200")
    
    menubar = Menu(fen)
    
    menu_equation= Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Équations", menu=menu_equation)
    menu_equation.add_command(label="Équation du premier degré", command=equation1)
    menu_equation.add_command(label="Équation du second degré", command=equation2)

    menu_help= Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=menu_help)
    menu_help.add_command(label="Aide", command=aide)
    menu_help.add_command(label="About E.R.", command=info)
    
    fen.config(menu=menubar)
    fen.mainloop()

main()
