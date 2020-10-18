# Yael Vaisman
# Baking pan converter app
from tkinter import *
import math


class panShape(object):
    def __init__(self, shape, rowIndex):
        self.shape = shape
        self.pan = self.setShape(rowIndex)

    def setShape(self, rowIndex):
        if self.shape == "Round":
            return RoundPan(rowIndex)
        if self.shape == "Square":
            return SquarePan(rowIndex)
        if self.shape == "Rectangle":
            return RectanglePan(rowIndex)

    def getArea(self):
        return self.pan.calculateArea()


def on_entry_click(entry):
    # if entry.get() == "diameter":
    entry.delete(0, "end")  # delete all the text in the entry
    entry.insert(0, '')  # Insert blank for user input


class RoundPan(panShape):
    def __init__(self, rowIndex):
        self.height = Entry(root, width=20)
        self.height.insert(0, "height (can ignore)")
        self.height.grid(row=rowIndex, column=0, padx=10, pady=10)
        self.diameter = Entry(root, width=20)
        self.diameter.insert(0, "diameter")
        self.diameter.grid(row=rowIndex, column=1)
        self.diameter.bind(
            "<FocusIn>", lambda _: on_entry_click(self.diameter))
        self.units = Entry(root, width=20)
        self.units.insert(0, "number of units")
        self.units.grid(row=rowIndex, column=2, padx=10, pady=10)
        self.units.bind(
            "<FocusIn>", lambda _: on_entry_click(self.units))

    def calculateArea(self):
        rad = (int(self.diameter.get()))/2
        return((rad**2)*math.pi*(int(self.units.get())))


class SquarePan(panShape):
    def __init__(self, rowIndex):
        self.height = Entry(root, width=20)
        self.height.insert(0, "height (can ignore)")
        self.height.grid(row=rowIndex, column=0)
        self.length = Entry(root, width=20)
        self.length.insert(0, "length")
        self.length.grid(row=rowIndex, column=1)
        self.length.bind(
            "<FocusIn>", lambda _: on_entry_click(self.length))
        self.units = Entry(root, width=20)
        self.units.insert(0, "number of units")
        self.units.grid(row=rowIndex, column=2)
        self.units.bind(
            "<FocusIn>", lambda _: on_entry_click(self.units))
        # area = ((length.get())**2)*(units.get())

    def calculateArea(self):
        area = int(self.length.get())**2
        return (area*int(self.units.get()))


class RectanglePan(panShape):
    def __init__(self, rowIndex):
        self.length = Entry(root, width=20)
        self.length.insert(0, "length")
        self.length.grid(row=rowIndex, column=0)
        self.length.bind(
            "<FocusIn>", lambda _: on_entry_click(self.length))
        self.width = Entry(root, width=20)
        self.width.insert(0, "width")
        self.width.grid(row=rowIndex, column=1)
        self.width.bind(
            "<FocusIn>", lambda _: on_entry_click(self.width))
        self.units = Entry(root, width=20)
        self.units.insert(0, "number of units")
        self.units.grid(row=rowIndex, column=2)
        self.units.bind(
            "<FocusIn>", lambda _: on_entry_click(self.units))
        # area = length.get()*width.get()*units.get()
        # self.setShapeArea(area)

    def calculateArea(self):
        return(int(self.length.get())*int(self.width.get())*int(self.units.get()))

    ########################################################################
    # creating the root widget
root = Tk()
root.title("Baking Pan Converter")
root.geometry("540x430")
root.grid_rowconfigure(0, minsize=80)
originPanLabel = Label(root, text="Choose original pan:")
originPanLabel.grid(row=0, column=1)
pans = ["Round", "Square", "Rectangle"]
originalpanChoice = StringVar()
originalpanChoice.set("Round")

originPan = panShape("Round", 2)
originalArea = 0
targetArea = 0


def originalShapeSelected():
    global originPan
    originPan = panShape(originalpanChoice.get(), 2)


def convertion():
    global originPan
    global originalArea
    global targetArea
    global targetPan
    originalArea = originPan.getArea()
    targetArea = targetPan.getArea()
    multBy = targetArea/originalArea
    resultLabel = Label(root, text="Multiply the recipe by {:.2f}".format(multBy)
                        + "\n Have fun baking!")
    resultLabel.grid(row=7, column=1)


i = 0
for shape in pans:
    Radiobutton(root, text=shape, variable=originalpanChoice,
                value=shape, command=originalShapeSelected).grid(row=1, column=i)
    i += 1

root.grid_rowconfigure(3, minsize=80)
targetPanLabel = Label(root, text="Choose target pan:")
targetPanLabel.grid(row=3, column=1)
targetpanChoice = StringVar()
targetpanChoice.set("Round")
targetPan = panShape("Round", 5)


def targetShapeSelected():
    global targetPan
    targetPan = panShape(targetpanChoice.get(), 5)


i = 0
for shape in pans:
    Radiobutton(root, text=shape, variable=targetpanChoice,
                value=shape, command=targetShapeSelected).grid(row=4, column=i)
    i += 1
convert = Button(root, text="Convert!", padx=20,
                 pady=20, command=convertion)
convert.grid(row=6, column=1)

root.mainloop()
