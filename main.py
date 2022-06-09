import tkinter
# from list_family_fonts import ListFamilyFonts


def create_new_file():
    print("Create a new file.")
    text_area.delete(1.0, "end")


def save_file():
    print("Save current file.")
    text_container = text_area.get(1.0, "end")
    file = open("notepad.txt", "w")
    file.write(text_container)
    file.close()


def open_file():
    print("Open file.")
    file = open("notepad.txt", "r")
    text_container = file.read()
    text_area.insert(1.0, text_container)
    file.close()


def update_font():
    f_size = spin_font_size.get()
    f_type = spin_font_type.get()
    text_area.config(font="{} {}".format(f_type, f_size))


window = tkinter.Tk()
window.title("Notepad")
# window.minsize(width=720, height=360)
window.geometry("720x360")

frame = tkinter.Frame(window, height=30)
frame.pack(fill="x")

font_text = tkinter.Label(frame, text=" Font: ")
font_text.pack(side="left")

spin_font_type = tkinter.Spinbox(frame, values=("Arial", "Verdana", "Sans"))
spin_font_type.pack(side="left")

font_size = tkinter.Label(frame, text=" Size: ")
font_size.pack(side="left")

spin_font_size = tkinter.Spinbox(frame, from_=0, to=72)
spin_font_size.pack(side="left")

button_update_changes = tkinter.Button(frame, text="UPDATE", command=update_font)
button_update_changes.pack(side="left")

text_area = tkinter.Text(window, font="Arial 20 bold", width=700, height=350)
text_area.pack()

main_menu = tkinter.Menu(window)

file_menu = tkinter.Menu(main_menu, tearoff=0)
file_menu.add_command(label="New", command=create_new_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Exit", command=window.quit)

main_menu.add_cascade(label="File", menu=file_menu)
window.config(menu=main_menu)

window.mainloop()
# ListFamilyFonts()
