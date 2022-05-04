from tkinter import *
from tkinter import Text
from functions import *

global editor
global toCode
global output
global window


def menuBarCreator(window, editor, toCode, output):
    menuBar = Menu(window)
    window.config(menu=menuBar)

    fileMenu = Menu(menuBar, tearoff=0)
    runMenu = Menu(menuBar, tearoff=0)

    menuBar.add_cascade(label='File', menu=fileMenu)
    fileMenu.add_command(label='New File...', command=lambda: newFile(editor, toCode, output))
    fileMenu.add_command(label='Open File...', command=lambda: openFile(editor))
    fileMenu.add_separator()
    fileMenu.add_command(label='Save As...', command=lambda: saveAs(editor))
    fileMenu.add_command(label='Save...')
    fileMenu.add_separator()
    fileMenu.add_command(label='Exit', command=exit)

    menuBar.add_cascade(label='Run', menu=runMenu)
    runMenu.add_command(label='Run...', command=lambda: run(editor, toCode, output))
    runMenu.add_command(label='Clear Console', command=lambda: output.delete('1.0', END))


def inicializeWindow():
    window = Tk()

    window.title('BrainIDE')
    window.iconbitmap('.//resources//lovethefrogs.ico')

    window.config(background='#5e5e5e')

    editor = Text(background='#0d1117', foreground='white')
    editor.pack(expand=True, fill=BOTH, padx=2.5, pady=(2.5, 1.75))

    toCode = Text(background='#0d1117', foreground='white')
    toCode.pack(expand=True, fill=BOTH, side=LEFT, padx=(2.5, 1.75), pady=(1.75, 2.5))

    output = Text(background='#0d1117', foreground='white')
    output.bind("<Key>", lambda e: "break")
    output.pack(expand=True, fill=BOTH, side=RIGHT, padx=(1.75, 2.5), pady=(1.75, 2.5))

    # logo = PhotoImage(file='.//resources//lovethefrogs.png')
    # Label(image=logo, background='#5e5e5e', width=300, anchor='center').grid(column=1, row=3)

    menuBarCreator(window, editor, toCode, output)

    window.mainloop()
