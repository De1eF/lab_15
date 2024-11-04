from tkinter import *
import tkinter

def GUI():
    m = tkinter.Tk()
    m.title("Letter counter")
    m.configure(width=450, height=280)
    
    wResult = Label(m, text="...", bg="gray")
    wResult.grid(row=5, column=2, padx=2, pady=2)
    
    def calculate():
        letterDict = dict()
        with open("task2/input.txt") as f:
            s = f.read()
            for chr in s:
                if not ord(chr) in range(ord("A"), ord("z")):
                    continue
                if (chr.lower() in letterDict.keys()):
                    letterDict[chr.lower()] += 1
                else:
                    letterDict[chr.lower()] = 1
        result = ""
        for i in sorted(letterDict.items()):
            result += "{} : {} \n".format(i[0], i[1])
        wResult.configure(text=result)
    
            
    
    wButton = Button(m, text="Search", width=25, command = lambda : calculate(), bg="gray")
    wButton.grid(row=4, column=2, padx=2, pady=2)
    
    m.mainloop()
GUI()