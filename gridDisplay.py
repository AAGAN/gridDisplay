from Tkinter import *

class bucket:

    rows = 0
    cols = 0
    values = "text"
    active = 0
    
    def __init__(self, master, row, col, value):
        self.rows = row
        self.cols = col
        self.values = value
        self.button = Button(master, text = value, fg="black",bg="white",command=self.activatee)
        self.button.grid(row = self.rows, column = self.cols)

    def activatee(self):
        self.button.configure(bg = "red")
        self.active = 1

    def deactivate(self):
        self.active = 0
        
root = Tk()
#root.title("gridDisplay")
#root.geometry("500x500")

buckets = [bucket(root, row = 0, col = count, value = str(count)) for count in xrange(10)]

root.mainloop()

