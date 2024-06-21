import tkinter as tk
from tkinter import filedialog,font
from PIL import Image,ImageTk
file_active = False
def new():
    global file_active,text_file
    text_file = filedialog.asksaveasfile(mode="w",defaultextension=".txt",filetypes=[("Txt Files","*.txt")])
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
        file_active = True
def save():
    global file_active,text_file
    text = textBox.get("1.0",tk.END)
    if(file_active):
        text_file.truncate(0)
        text_file.seek(0,2)
        text_file.write(text)
    else:
        saveAs()
def saveAs():
    global file_active,text_file
    text = textBox.get("1.0",tk.END)
    text_file = filedialog.asksaveasfile(mode="w",defaultextension=".txt",filetypes=[("Txt Files","*.txt")])
    if(text_file):
        global original_text
        original_text = ""
        file_active = True
        text_file.truncate(0)
        text_file.seek(0,2)
        text_file.write(text)
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
        textBox.delete(tk.SEL_FIRST,tk.SEL_LAST)
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
root.configure(background="SystemButtonFace")
textFont = tk.font.Font(family="Times new roman",size=16)
newButton = tk.Button(root,text="New",width=8,bd=0,command=new)
openExistingButton = tk.Button(root,text="Open Existing",bd=0,command=openExisting)
saveButton = tk.Button(root,text="Save",width=8,bd=0,command=save)
saveAsButton = tk.Button(root,text="Save As",width=8,bd=0,command=save)
restoreOriginalButton = tk.Button(root,text="Restore",width=8,bd=0,command=revertOriginal)
selectAllButton = tk.Button(root,text="Select All",width=8,bd=0,command=selectAll)
cutButton = tk.Button(root,text="Cut",width=8,bd=0,command=cut)
copyButton = tk.Button(root,text="Copy",width=8,bd=0,command=copy)
pasteButton = tk.Button(root,text="Paste",width=8,bd=0,command=paste)
textBox = tk.Text(root,height=25,width=71,font=textFont,wrap="none")
scrollbar_y = tk.Scrollbar(root,orient=tk.VERTICAL,command=textBox.yview)
textBox.configure(yscrollcommand=scrollbar_y.set,tabs=textFont.measure(" " * 4),insertwidth=1,bd=0)
newButton.place(x=0,y=3)
openExistingButton.place(x=65,y=3)
saveButton.place(x=148,y=3)
saveAsButton.place(x=213,y=3)
restoreOriginalButton.place(x=278,y=3)
selectAllButton.place(x=343,y=3)
cutButton.place(x=408,y=3)
copyButton.place(x=473,y=3)
pasteButton.place(x=538,y=3)
textBox.place(x=0,y=26)
scrollbar_y.place(x=780,y=26,height=572)
root.mainloop()
