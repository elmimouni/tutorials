from tkinter import *
# // from tkinter import * // doesn't import messagebox it has to be explicitly imported
from tkinter import messagebox
from math import *
from optparse import OptionParser

<<<<<<< HEAD
def about():
    messagebox.showinfo("Info", "Equations solver v1.3 is a program that solves 1st and 2nd degree equations.""\n""Created by Abderrahmane El Mimouni and supervised by El Hassan El Mimouni.")

def help():
    messagebox.showinfo("Info", "Coming soon...")
=======
def info():
    messagebox.showinfo("Information", "Equations resolver v1.3 is a program coded by Abderrahmane El Mimouni.""\n""And supervised by El Hassan El Mimouni.")

def aide():
    messagebox.showinfo("Information", "In developement.")
>>>>>>> 91ed11d588683628e4e4af697985b4dac9092424

def equation1():
    
    def back():
        
        destroyWidgets()
        
    def reset():
        entr1.delete(0, END)
        entr2.delete(0, END)
        entr3.delete(0, END)
        entr4.delete(0, END)
    
    def solve():

        try:
            a = int(entr1.get())
            b = int(entr2.get())
            c = int(entr3.get())
            x = (c-b)/a
            entr4.config(bg="white", fg="black")
            entr4.delete(0, END)
            entr4.insert(0, x)

        except ValueError:
            messagebox.showerror("Error", "Error of value.")
            
        except ZeroDivisionError:
            messagebox.showerror("Error", "Error of division by 0.")

    def createWidgets():
        global txt0, txt1, txt2, txt3, txt4, entr1, entr2, entr3, entr4, btn1, btn2, btn3

        txt0 = Label(window, text = 'Equation ax + b = c', fg='red', font=('Times', 16, 'bold', 'italic'))
        txt1 = Label(window, text = 'a :', font=('Times', 12))
        txt2 = Label(window, text = 'b :', font=('Times', 12))
        txt3 = Label(window, text = 'c :', font=('Times', 12))
        txt4 = Label(window, text = 'x :', font=('Times', 12))
        
        entr1 = Entry(window, font=('Times', 12))
        entr2 = Entry(window, font=('Times', 12))
        entr3 = Entry(window, font=('Times', 12))
        entr4 = Entry(window, font=('Times', 12))
        
        entr1.delete(0, END)
        entr1.insert(0, "")
        entr2.delete(0, END)
        entr2.insert(0, "")
        entr3.delete(0, END)
        entr3.insert(0, "")
        entr4.delete(0, END)
        entr4.insert(0, "")

<<<<<<< HEAD
        btn1 = Button(window, text='Solve', font=('Times', 12), command=solve)
        btn2 = Button(window, text='Reset', font=('Times', 12), command=reset)
        btn3 = Button(window, text="Back", font=('Times', 12), command=back)
=======
        btn1 = Button(fen, text='Solve', font=('Times', 12), command=Calculer)
        btn2 = Button(fen, text='Again', font=('Times', 12), command=refaire)
        btn3 = Button(fen, text="Remove", font=('Times', 12), command=tout_refaire)
>>>>>>> 91ed11d588683628e4e4af697985b4dac9092424

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

    def destroyWidgets():
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
        
    createWidgets()

def equation2():
    
    def back():
        
        destroyWidgets()
        
    
    def reset():
        global delete
        entr1.delete(0, END)
        entr2.delete(0, END)
        entr3.delete(0, END)
        entr4.destroy()
        entr5.destroy()
        txt4.destroy()
        txt5.destroy()

        
    def solve():

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
<<<<<<< HEAD
                messagebox.showinfo("Result", "This equation does not have a solution!")
=======
                messagebox.showinfo("End of the exercice", "This equation has no solution!")
>>>>>>> 91ed11d588683628e4e4af697985b4dac9092424
                    
            if (delta == 0):
                x0 = (-b/2*a)
                txt4.grid(row=4, column=0)
                entr4.grid(row=4, column=1)
                entr4.insert(0, x0)

        except ValueError:
<<<<<<< HEAD
            messagebox.showerror("Error", "Value Error!")
            
    def alert():
        messagebox.showinfo("Info", "Equations solver v1.3 is a program that solves 1st and 2nd degree equations.""\n""Created by Abderrahmane El Mimouni and supervised by El Hassan El Mimouni.")
        
    def createWidgets():
        global txt0, txt01, txt1, txt2, txt3, txt4, txt5, entr1, entr2, entr3, entr4, entr5, btn1, btn2, btn3
        txt0 = Label(window, text="équation", font=("Times", 16, "bold", "italic"), fg="red")
        txt01 = Label(window, text="ax² + bx + c = 0", font=("Times", 16, "bold", "italic"), fg="red")
        txt1 = Label(window, text="a:", font=("Times", 12))
        txt2 = Label(window, text="b:", font=("Times", 12))
        txt3 = Label(window, text="c:", font=("Times", 12))
        txt4 = Label(window, text="x1:", font=("Times", 12))
        txt5 = Label(window, text="x2:", font=("Times", 12))

        entr1 = Entry(window, font=("Times", 12))
        entr2 = Entry(window, font=("Times", 12))
        entr3 = Entry(window, font=("Times", 12))
        entr4 = Entry(window, font=("Times", 12))
        entr5 = Entry(window, font=("Times", 12))
=======
            messagebox.showerror("Error", "Error of value!")
            
    def widgets():
        global fen, txt0, txt01, txt1, txt2, txt3, txt4, txt5, entr1, entr2, entr3, entr4, entr5, btn1, btn2, btn3
        
        txt0 = Label(fen, text="Equation", font=("Times", 16, "bold", "italic"), fg="red")
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
>>>>>>> 91ed11d588683628e4e4af697985b4dac9092424

        txt0.grid(row=0, column=0)
        txt01.grid(row=0, column=1)
        txt1.grid(row=1, column=0)
        txt2.grid(row=2, column=0)
        txt3.grid(row=3, column=0)

        entr1.grid(row=1, column=1)
        entr2.grid(row=2, column=1)
        entr3.grid(row=3, column=1)

<<<<<<< HEAD
        btn1 = Button(window, text="Solve", font=("Times", 13), command=solve)
        btn1.grid(row=6, column=1)

        btn2= Button(window, text="Reset", font=("Times", 13), command=reset)
        btn2.grid(row=6, column=0)

        btn3= Button(window, text="Back", font=("Times", 13), command=back)
=======
        btn1 = Button(fen, text="Solve", font=("Times", 13), command=calculer)
        btn1.grid(row=6, column=1)

        btn2= Button(fen, text="Again", font=("Times", 13), command=supprimer)
        btn2.grid(row=6, column=0)

        btn3= Button(fen, text="Remove", font=("Times", 13), command=tout_supprimer)
>>>>>>> 91ed11d588683628e4e4af697985b4dac9092424
        btn3.grid(row=7, column=1)

    def destroyWidgets():

        for child in window.winfo_children():
            print(child.cget('class'))
            # child.destroy()

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

    createWidgets()

  


def main():
<<<<<<< HEAD
    global window, menubar
    parser = OptionParser()
    parser.add_option("-W", "--width", action="store", type="int", dest="windowWidth", help="Set width for your window")
    parser.add_option("-H", "--height", action="store", type="int", dest="windowHeight", help="Set height for your window")
    (options, args) = parser.parse_args()
	
    window = Tk()
    window.title("1st and 2nd degree equations resolver")
    windowSize = str(options.windowHeight)+'x'+str(options.windowWidth)
    window.geometry(windowSize)
    menubar = Menu(window)
    
    menu_equation= Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Equation", menu=menu_equation)
    menu_equation.add_command(label="1st degree", command=equation1)
    menu_equation.add_command(label="2nd degree", command=equation2)

    menu_help= Menu(menubar, tearoff=0)
    menubar.add_cascade(label="?", menu=menu_help)
    menu_help.add_command(label="Help", command=help)
    menu_help.add_command(label="About", command=about)
    
    window.config(menu=menubar)
    window.mainloop()
=======
    global fen
    
    fen = Tk()
    fen.title("Equations resolver v1.3")
    fen.geometry("290x200")
    
    menubar = Menu(fen)
    
    menu_equation= Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Equation", menu=menu_equation)
    menu_equation.add_command(label="First-degree equation", command=equation1)
    menu_equation.add_command(label="Second-degree equation", command=equation2)

    menu_help= Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=menu_help)
    menu_help.add_command(label="Help", command=aide)
    menu_help.add_command(label="About", command=info)
>>>>>>> 91ed11d588683628e4e4af697985b4dac9092424
    

main()
