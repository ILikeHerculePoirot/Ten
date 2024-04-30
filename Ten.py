import tkinter as tk
from tkinter import filedialog,font
from PIL import Image,ImageTk
file_active = False
def new():
    global file_active,text_file
    text_file = filedialog.asksaveasfile(mode='w',defaultextension=".txt",filetypes=[("Txt Files","*.txt")])
    if(text_file):
        global original_text
        original_text = ""
        file_active = True
def openExisting():
    global file_active,text_file,original_text
    text_file_path = filedialog.askopenfilename(filetypes=[("Txt Files","*.txt")])
    if(text_file_path):
        text_file = open(text_file_path,"r+")
        original_text = text_file.readlines()
        textBox.delete(1.0,tk.END)
        for line in original_text:
            textBox.insert(tk.END,line)
        file_active=True
def save():
    global file_active,text_file
    text = textBox.get("1.0",tk.END)
    if(file_active):
        text_file.truncate(0)
        text_file.seek(0,2)
        text_file.write(text)
    else:
        text_file = filedialog.asksaveasfile(mode='w',defaultextension=".txt",filetypes=[("Txt Files","*.txt")])
        if(text_file):
            global original_text
            original_text = ""
            file_active = True
def revertOriginal():
    if(file_active):
        text_file.truncate(0)
        text_file.seek(0,2)
        textBox.delete(1.0,tk.END)
        for line in original_text:
            textBox.insert(tk.END,line)
            text_file.write(line)
root = tk.Tk()
root.geometry("800x600")
root.title("Ten")
icon = Image.open("Assets/Ten.ico")
photo = ImageTk.PhotoImage(icon)
root.wm_iconphoto(False,photo)
root.resizable(False,False)
root.configure(background="black")
textFont=tk.font.Font(size=14)
newButton = tk.Button(root,text="     New     ",command = lambda:new())
openExistingButton = tk.Button(root,text="Open Existing",command = lambda:openExisting())
saveButton = tk.Button(root,text="     Save     ",command = lambda:save())
restoreOriginalButton = tk.Button(root,text="Restore Original",command = lambda:revertOriginal())
textBox = tk.Text(root,height=26,width=72,font=textFont)
newButton.place(x=2,y=5)
openExistingButton.place(x=72,y=5)
saveButton.place(x=162,y=5)
restoreOriginalButton.place(x=233,y=5)
textBox.place(x=2,y=32)
root.mainloop()