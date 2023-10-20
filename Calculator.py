from tkinter import *
"""
basic calculator script
if i ever come back to improve this, i'll completely redo the button placement, making it more dynamic, resize with window, etc.
I think Tkinter.frame() would work for this but i dont really know

would also add a catch for diving by 0, which i forgot to do in my first go
"""

class CalcWindow:
    def __init__(self, win):

        #button sizing options
        self.buttonSize = 2
        self.startX = 100
        self.startY = 100
        self.paddingAmount = 25
        


        self.currentValue = 0
        self.displayStr = str(self.currentValue)
        self.displayText = StringVar()
        self.displayText.set(self.displayStr)

        self.lbl=Label(win, textvariable=self.displayText).place(x=self.startX,y=25)

        self.btnClear=Button(win, text="C", width=self.buttonSize, command=self.btnClear).place(x=self.startX+self.paddingAmount*2,y=self.startY-self.paddingAmount)
        self.btnBackspace=Button(win, text="⌫", width=self.buttonSize, command=self.btnBackspacePress).place(x=self.startX+self.paddingAmount*3,y=self.startY-self.paddingAmount)

        
        self.btn1=Button(win, text="1", width=self.buttonSize, command=self.btn1Press).place(x=self.startX,y=self.startY)
        self.btn2=Button(win, text="2", width=self.buttonSize, command=self.btn2Press).place(x=self.startX+self.paddingAmount,y=self.startY)
        self.btn3=Button(win, text="3", width=self.buttonSize, command=self.btn3Press).place(x=self.startX+self.paddingAmount*2,y=self.startY)
        self.btn4=Button(win, text="4", width=self.buttonSize, command=self.btn4Press).place(x=self.startX,y=self.startY+self.paddingAmount)
        self.btn5=Button(win, text="5", width=self.buttonSize, command=self.btn5Press).place(x=self.startX+self.paddingAmount,y=self.startY+self.paddingAmount)
        self.btn6=Button(win, text="6", width=self.buttonSize, command=self.btn6Press).place(x=self.startX+self.paddingAmount*2,y=self.startY+self.paddingAmount)
        self.btn7=Button(win, text="7", width=self.buttonSize, command=self.btn7Press).place(x=self.startX,y=self.startY+self.paddingAmount*2)
        self.btn8=Button(win, text="8", width=self.buttonSize, command=self.btn8Press).place(x=self.startX+self.paddingAmount,y=self.startY+self.paddingAmount*2)
        self.btn9=Button(win, text="9", width=self.buttonSize, command=self.btn9Press).place(x=self.startX+self.paddingAmount*2,y=self.startY+self.paddingAmount*2)
        self.btn0=Button(win, text="0", width=self.buttonSize, command=self.btn0Press).place(x=self.startX,y=self.startY+self.paddingAmount*3)


        self.btnDiv=Button(win, text="÷", width=self.buttonSize, command=self.btnDivPress).place(x=self.startX+self.paddingAmount*3,y=self.startY)
        self.btnMult=Button(win, text="x", width=self.buttonSize, command=self.btnMultPress).place(x=self.startX+self.paddingAmount*3,y=self.startY+self.paddingAmount)
        self.btnSub=Button(win, text="-", width=self.buttonSize, command=self.btnSubPress).place(x=self.startX+self.paddingAmount*3,y=self.startY+self.paddingAmount*2)
        self.btnAdd=Button(win, text="+", width=self.buttonSize, command=self.btnAddPress).place(x=self.startX+self.paddingAmount*3,y=self.startY+self.paddingAmount*3)
        self.btnEquals=Button(win, text="=", width=self.buttonSize, command=self.btnEqualsPress).place(x=self.startX+self.paddingAmount*2,y=self.startY+self.paddingAmount*3)


    def btnClear(self):
        self.currentValue = 0
        self.displayStr = str(self.currentValue)
        self.displayText.set(self.displayStr)
    
    def addToLabel(self, value):
        self.displayStr = (self.displayStr+str(value)).lstrip("0")
        self.displayText.set(str(self.displayStr))
        #print("DEBUG: label added to, value: "+str(value))

    
    def btnBackspacePress(self):
        self.displayStr = self.displayStr[:-1]
        self.displayText.set(str(self.displayStr))
    
    
    def btn1Press(self): self.addToLabel(1)
    def btn2Press(self): self.addToLabel(2)
    def btn3Press(self): self.addToLabel(3)
    def btn4Press(self): self.addToLabel(4)
    def btn5Press(self): self.addToLabel(5)
    def btn6Press(self): self.addToLabel(6)
    def btn7Press(self): self.addToLabel(7)
    def btn8Press(self): self.addToLabel(8)
    def btn9Press(self): self.addToLabel(9)
    def btn0Press(self): self.addToLabel(0)

    def btnDivPress(self): self.addToLabel("÷")
    def btnMultPress(self): self.addToLabel("x")
    def btnSubPress(self): self.addToLabel("0")
    def btnAddPress(self): self.addToLabel("+")
        
        
    
    def btnEqualsPress(self):
        self.evalStr = self.displayStr.lstrip("0").replace("x", "*").replace("÷", "/")
        self.currentValue = eval(self.evalStr)
        self.displayStr = str(self.currentValue)
        self.displayText.set(self.displayStr)


def main():
    window=Tk()
    CalcWin=CalcWindow(window)
    window.title('Calculator')
    window.geometry("300x300+10+10")
    window.mainloop()

if __name__ == "__main__":
    main()