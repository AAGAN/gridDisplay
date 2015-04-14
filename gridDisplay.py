from Tkinter import *


class bucket:
    rows = 0
    cols = 0
    values = "text"
    def __init__(self, master, row, col, value):
        self.rows = row
        self.cols = col
        self.values = value
        self.button = Button(master, text = value, fg="black",bg="white",command=self.activatee)
        self.button.grid(row = self.rows, column = self.cols)

    def activatee(self):
        self.button.configure(bg = "red")
        
    

root = Tk()
#root.title("gridDisplay")
#root.geometry("500x500")

bucket1 = bucket(root, row = 0, col = 0, value = "0.010")
bucket2 = bucket(root, row = 0, col = 1, value = "0.015")


root.mainloop()

