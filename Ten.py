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
        text_file = filedialog.asksaveasfile(mode="w",defaultextension=".txt",filetypes=[("Txt Files","*.txt")])
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
        textBox.delete(tk.SEL_FIRST,tk.SEL_LAST)
def copy():
    if textBox.tag_ranges(tk.SEL):
        root.clipboard_clear()
        root.clipboard_append(textBox.get(tk.SEL_FIRST,tk.SEL_LAST))
def paste():
    textBox.insert(tk.INSERT,root.clipboard_get())
def exit():
    if(file_active):
        text_file.close()
    root.destroy()
root = tk.Tk()
root.geometry("793x581")
root.title("Ten")
icon = Image.open("Assets/Ten.ico")
photo = ImageTk.PhotoImage(icon)
root.wm_iconphoto(False,photo)
root.resizable(False,False)
root.configure(background="black")
textFont = tk.font.Font(size=14)
newButton = tk.Button(root,text="New",width=8,command=new)
openExistingButton = tk.Button(root,text="Open Existing",command=openExisting)
saveButton = tk.Button(root,text="Save",width=8,command=save)
restoreOriginalButton = tk.Button(root,text="Restore Original",command=revertOriginal)
selectAllButton = tk.Button(root,text="Select All",width=8,command=selectAll)
cutButton = tk.Button(root,text="Cut",width=8,command=cut)
copyButton = tk.Button(root,text="Copy",width=8,command=copy)
pasteButton = tk.Button(root,text="Paste",width=8,command=paste)
exitButton = tk.Button(root,text="Exit",width=8,command=exit)
textBox = tk.Text(root,height=24,width=70,font=textFont,wrap="none")
scrollbar_x = tk.Scrollbar(root,orient=tk.HORIZONTAL,command=textBox.xview)
scrollbar_y = tk.Scrollbar(root,orient=tk.VERTICAL,command=textBox.yview)
textBox.configure(xscrollcommand=scrollbar_x.set,yscrollcommand=scrollbar_y.set,tabs=textFont.measure(" " * 4),insertwidth=1)
newButton.place(x=2,y=5)
openExistingButton.place(x=67,y=5)
saveButton.place(x=150,y=5)
restoreOriginalButton.place(x=215,y=5)
selectAllButton.place(x=309,y=5)
cutButton.place(x=374,y=5)
copyButton.place(x=439,y=5)
pasteButton.place(x=504,y=5)
exitButton.place(x=569,y=5)
textBox.place(x=2,y=32)
scrollbar_x.place(x=2,y=564,width=796)
scrollbar_y.place(x=776,y=32,height=568)
root.mainloop()
