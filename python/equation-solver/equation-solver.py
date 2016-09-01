from tkinter import *
from tkinter import messagebox
from math import *
from optparse import OptionParser

def about():
    messagebox.showinfo("Info", "Equations solver v1.3 is a program that solves 1st and 2nd degree equations.""\n""Created by Abderrahmane El Mimouni and supervised by El Hassan El Mimouni.")

def help():
    messagebox.showinfo("Info", "Coming soon...")

def firstDegree():
    equationFrame['text']="1st Degree Equation Solver"
    destroyWidgets()
    def back():
        equationFrame.pack_forget()
        destroyWidgets()
    
    def reset():
        aEntry1.delete(0, END)
        bEntry1.delete(0, END)
        cEntry1.delete(0, END)
    
    def solve():
        try:
            a = int(aEntry1.get())
            b = int(bEntry1.get())
            c = int(cEntry1.get())
            x = (c-b)/a
            reset()
            if (a == 1):
                message = "The solution of  x + "+str(b)+" = "+str(c)+" is: \n"+ str(x)
            else:
                message = "The solution of  "+str(a)+"x + "+str(b)+" = "+str(c)+" is: \n"+ str(x)   
            messagebox.showinfo("Result", message)
        except ValueError:
            messagebox.showerror("Error", "Value error!")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Error: you cannot divide by 0!")

    def createWidgets():
        global aEntry1, bEntry1, cEntry1
        equationFrame.pack(fill="both", expand="yes")
        aLabel1 = Label(equationFrame, text="a = ").grid(row=0,column=0)
        aEntry1 = Entry(equationFrame, bd =1, width=10)
        aEntry1.grid(row=0,column=1)
        bLabel1 = Label(equationFrame, text="b = ").grid(row=1,column=0)
        bEntry1 = Entry(equationFrame, bd =1, width=10)
        bEntry1.grid(row=1,column=1)
        cLabel1 = Label(equationFrame, text="c = ", width=10).grid(row=2,column=0)
        cEntry1 = Entry(equationFrame, bd =1, width=10)
        cEntry1.grid(row=2,column=1)
        solveButton = Button(equationFrame, text="Solve", width=10, command=solve).grid(row=3,column=0)
        resetButton = Button(equationFrame, text="Reset", width=10, command=reset).grid(row=3,column=1)
        backButton = Button(equationFrame, text="Back", width=10, command=back).grid(row=3,column=2)

    createWidgets()

def secondDegree():
    equationFrame['text']="2nd Degree Equation Solver"
    destroyWidgets()
    def back():
        equationFrame.pack_forget()
        destroyWidgets()
    
    def reset():
        aEntry2.delete(0, END)
        bEntry2.delete(0, END)
        cEntry2.delete(0, END)
    
    def solve():
        try:
            a = int(aEntry2.get())
            b = int(bEntry2.get())
            c = int(cEntry2.get())
            delta = (b**2-4*a*c)
            if (delta > 0):
                x1 = (-b+sqrt(delta)/2*a)
                x2 = (-b-sqrt(delta)/2*a)
                if (a==1 & b==1):
                    message = "The solutions of x^2 + x +"+str(c)+" = 0 are: \n"+ str(x1)+ " and "+ str(x2)
                else:
                    if(a==1):
                        message = "The solutions of x^2 + "+str(b)+ "x + " +str(c)+" = 0 are: \n"+ str(x1)+ " and "+ str(x2)
                    else:
                        message = "The solutions of "+str(a)+"x^2 + x + " +str(c)+" = 0 are: \n"+ str(x1)+ " and "+ str(x2)
            if (delta < 0):
                message = "This equation does not have a solution!"
            if (delta == 0):
                x0 = (-b/2*a)
                if (a==1 & b==1):
                    message = "The unique solution of x^2 + x +"+str(c)+" = 0 is: \n"+ str(x0)
                else:
                    if(a==1):
                        message = "The unique solution of x^2 + "+str(b)+ "x + " +str(c)+" = 0 is: \n"+ str(x0)
                    else:
                        message = "The unique solution of "+str(a)+"x^2 + x + " +str(c)+" = 0 is: \n"+ str(x0)
            messagebox.showinfo("Result", message)
        except ValueError:
            messagebox.showerror("Error", "Value Error!")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Error: you cannot divide by 0!")

    def createWidgets():
        global aEntry2, bEntry2, cEntry2
        equationFrame.pack(fill="both", expand="yes")
        aLabel2 = Label(equationFrame, text="a = ").grid(row=0,column=0)
        aEntry2 = Entry(equationFrame, bd =1, width=10)
        aEntry2.grid(row=0,column=1)
        bLabel2 = Label(equationFrame, text="b = ").grid(row=1,column=0)
        bEntry2 = Entry(equationFrame, bd =1, width=10)
        bEntry2.grid(row=1,column=1)
        cLabel2 = Label(equationFrame, text="c = ", width=10).grid(row=2,column=0)
        cEntry2 = Entry(equationFrame, bd =1, width=10)
        cEntry2.grid(row=2,column=1)
        solveButton = Button(equationFrame, text="Solve", width=10, command=solve).grid(row=3,column=0)
        resetButton = Button(equationFrame, text="Reset", width=10, command=reset).grid(row=3,column=1)
        backButton = Button(equationFrame, text="Back", width=10, command=back).grid(row=3,column=2)

    createWidgets()
def destroyWidgets():
    for child in equationFrame.winfo_children():
        child.destroy()

def initWindow():

    window.title("1st and 2nd degree equations resolver")
    windowSize = str(options.windowWidth)+'x'+str(options.windowHeight)
    window.geometry(windowSize)
    menubar = Menu(window)
    menu_equation= Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Equation", menu=menu_equation)
    menu_equation.add_command(label="1st degree", command=firstDegree)
    menu_equation.add_command(label="2nd degree", command=secondDegree)
    menu_help= Menu(menubar, tearoff=0)
    menubar.add_cascade(label="?", menu=menu_help)
    menu_help.add_command(label="Help", command=help)
    menu_help.add_command(label="About", command=about)
    window.config(menu=menubar)


def main():
    global window, options, equationFrame
    parser = OptionParser()
    parser.add_option("-W", "--width", action="store", type="int", dest="windowWidth", help="Set width for your window")
    parser.add_option("-H", "--height", action="store", type="int", dest="windowHeight", help="Set height for your window")
    (options, args) = parser.parse_args()
    
    window = Tk()
    initWindow()
    equationFrame = LabelFrame(window)
    window.mainloop()

main()