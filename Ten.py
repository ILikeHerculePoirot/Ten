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
def selectAll():
    textBox.tag_add(tk.SEL,"1.0",tk.END)
    textBox.mark_set(tk.INSERT,"1.0")
    textBox.see(tk.INSERT)
def cut():
    if textBox.tag_ranges(tk.SEL):
        root.clipboard_clear()
        root.clipboard_append(textBox.get(tk.SEL_FIRST,tk.SEL_LAST))
        textBox.delete(tk.SEL_FIRST, tk.SEL_LAST)
def copy():
    if textBox.tag_ranges(tk.SEL):
        root.clipboard_clear()
        root.clipboard_append(textBox.get(tk.SEL_FIRST,tk.SEL_LAST))
def paste():
    textBox.insert(tk.INSERT,root.clipboard_get())
root = tk.Tk()
root.geometry("800x600")
root.title("Ten")
icon = Image.open("Assets/Ten.ico")
photo = ImageTk.PhotoImage(icon)
root.wm_iconphoto(False,photo)
root.resizable(False,False)
root.configure(background="black")
textFont = tk.font.Font(size=14)
newButton = tk.Button(root,text="     New     ",command=new)
openExistingButton = tk.Button(root,text="Open Existing",command=openExisting)
saveButton = tk.Button(root,text="     Save     ",command=save)
restoreOriginalButton = tk.Button(root,text="Restore Original",command=revertOriginal)
selectAllButton = tk.Button(root,text="  Select All  ",command=selectAll)
cutButton = tk.Button(root,text="     Cut     ",command=cut)
copyButton = tk.Button(root,text="     Copy     ",command=copy)
pasteButton = tk.Button(root,text="    Paste    ",command=paste)
textBox = tk.Text(root,height=26,width=72,font=textFont,wrap="none")
scrollbar_x = tk.Scrollbar(root,orient=tk.HORIZONTAL,command=textBox.xview)
scrollbar_y = tk.Scrollbar(root,orient=tk.VERTICAL,command=textBox.yview)
newButton.place(x=2,y=5)
openExistingButton.place(x=67,y=5)
saveButton.place(x=151,y=5)
restoreOriginalButton.place(x=216,y=5)
selectAllButton.place(x=311,y=5)
cutButton.place(x=382,y=5)
copyButton.place(x=442,y=5)
pasteButton.place(x=511,y=5)
textBox.place(x=2,y=32)
scrollbar_x.place(x=2,y=580,width=796)
scrollbar_y.place(x=780,y=32,height=568)
root.mainloop()
