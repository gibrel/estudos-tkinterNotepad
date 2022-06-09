from tkinter import *
from tkinter import font


class ListFamilyFonts:

    def __init__(self):
        self.root = Tk()
        self.root.title('Font Families')
        self.fonts=list(font.families())
        self.fonts.sort()

        self.canvas = Canvas(self.root, borderwidth=0)
        self.frame = Frame(self.canvas)
        self.vsb = Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw")

        self.frame.bind("<Configure>", lambda event, canvas=self.canvas: self.on_frame_configure(self.canvas))

        self.populate(self.frame)

        self.root.mainloop()

    def populate(self, frame):
        """Put in the fonts"""
        list_number = 1
        for item in self.fonts:
            label = "listlabel" + str(list_number)
            label = Label(frame, text=item, font=(item, 16))
            label.pack()
            list_number += 1

    def on_frame_configure(self, canvas):
        """Reset the scroll region to encompass the inner frame"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


# ListFamilyFonts()
