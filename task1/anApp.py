import tkinter
import json
from tkinter import *

fileDirectory = "task1/workerDb.json"

def listFromDb(fileDirectory):
    with open(fileDirectory) as f:
        return json.load(f)

def getAllWorkersOfCompany(company):
    workerDir = listFromDb(fileDirectory)
    companyWorkerList = []
    for w in workerDir.items():
        if (w[1] == company):
            companyWorkerList.append(w)
    return companyWorkerList

def GUI():
    m = tkinter.Tk()
    m.title("Worker manager")
    m.configure(width=450, height=280, bg="yellow")

    options = []
    for el in listFromDb(fileDirectory).items():
        if not el[1] in options:
            options.append(el[1])
    clicked = StringVar()
    clicked.set("Select Company") 
    wDesc = OptionMenu(m, clicked, *options)
    wDesc.configure(bg="gold")
    wDesc.grid(row=2, column=2, padx=2, pady=2)
    
    wButton = Button(m, text="Search", width=25, command = lambda : placeResult(getAllWorkersOfCompany(clicked.cget())), bg="gold")
    wButton.grid(row=4, column=2, padx=2, pady=2)

    def placeResult(workerList):
        s = ""
        for w in workerList:
            s += "Name: " + w[0] + "\n"
        wResult.configure(text=s)
    
    wResult = Label(m, text="...", bg="yellow")
    wResult.grid(row=5, column=2, padx=2, pady=2)


    m.mainloop()
GUI()
