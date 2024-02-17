#!/usr/bin/python3.6
# @author::: anthony.kiggundu@

import ttk
import os
import PIL
from PIL import Image, ImageTk
from Tkinter import *
#import Image, ImageTk
import Tkinter
import tkFileDialog
import tkMessageBox
import ScrolledText

class nodeEdit(PanedWindow): # Frame
    
    def __init__(self, master=None):    
#     parameters that you want to send through the Frame class. 
        self.master = master
        self.master.title('node-e-dit')
        self.master.geometry('{}x{}'.format(1000, 650))
        self.master.config(background="lavender")
        self._filetypes = [('Text', '*.txt'),("HTML files", "*.html;*.htm"),('All files', '*')]
        #self.createPanel(master)
    
    def cancelForm(self):
        pass
    
    def save_file(self):
        
        try:       
            file_pointer = open(self.fname, 'w')
            if (self.fname == ''):
                file_pointer.write(self.textfield.get('1.0', 'end'))
                file_pointer.close()
                tkMessageBox.showinfo('Nod-e-dit', 'File saved successfully')

            else:            
                file_pointer.write(self.textfield.get('1.0', 'end')) # change every 'self' that refers to the Text, to self.text
                file_pointer.close()
                tkMessageBox.showinfo('Nod-e-dit', 'File saved successfully.')
        except IOError:
            print("Save File::", "Failed to save the file\n'%s'" % self.fname)
        return
    
    def save_file_as(self):
        
        try:
            self.fname = tkFileDialog.asksaveasfilename(defaultextension='.txt',
                                                             filetypes = self._filetypes)
            file_pointer = open(self.fname, 'w')
            if (self.fname == ''):
                file_pointer.write(self.textfield.get('1.0', 'end'))
                file_pointer.close()
                tkMessageBox.showinfo('Nod-e-dit', 'File saved successfully')

            else:            
                file_pointer.write(self.textfield.get('1.0', 'end')) # change every 'self' that refers to the Text, to self.text
                file_pointer.close()
                tkMessageBox.showinfo('Nod-e-dit', 'File saved successfully.')
        except IOError:
            print("Save File::", "Failed to save the file\n'%s'" % self.fname)
        return

    def donothing(self, master):    
        filewin = Toplevel(self.master)
        button = Button(filewin, text="Do nothing button")
        button.pack()
    
    def open_file(self):
        self.fname = tkFileDialog.askopenfilename(filetypes=self._filetypes) # (("Template files", "*.tplate"),("HTML files", "*.html;*.htm"),("All files", "*.*") ))
                                                                                                                                       
        if self.fname:
            try:                                    
                with open(self.fname,'r') as filename:
                    self.textfield.insert('1.0',filename.read()) #(Tkinter.END, filename.read()) #.pack() 
                filename.close()                                                                             
            except IOError:
                print("Open Source File", "Failed to read file\n'%s'" % self.fname)
            return

# ToDo :: this function needs to be adjusted to automatically render a corresponding sub-menu's icon
    def showImg(self):
        load = Image.open("./src/chat.png")
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
    
    def createPanel(self, master):
    
        #self.content = StringVar()
        self.textfield = ScrolledText.ScrolledText(self.master, wrap=Tkinter.WORD, height=190, width=190)
#        self.textfield = ScrolledText(self.master, state='disabled', height=12)
        self.textfield.grid(row=0, column=0, sticky=(N, S, W, E))
        self.textfield.configure(font='TkFixedFont')
        self.textfield.configure(state='normal')
        # Autoscroll to the bottom
        self.textfield.yview(Tkinter.END)  
        
### Would be cool to have icons besides submenus,, but this has not yet worked so far
#    new_icon = PIL.Image.open("/home/ubuntu/src/new.jpg")
#    n_icon = PIL.ImageTk.PhotoImage(new_icon)
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
# TODO:: --> accelerators are not working as expected.    
        filemenu.add_command(label="New", command=self.donothing, accelerator="Ctrl+N") #image=n_icon)
        filemenu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")

        filemenu.add_separator()    

        filemenu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+s" )
        filemenu.add_command(label="Save as...", command=self.save_file_as, accelerator="Ctrl+a")
        filemenu.add_command(label="Close", command=self.master.quit, accelerator="Ctrl+X")

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=self.donothing, accelerator="Ctrl+U")
        editmenu.add_command(label="Redo", command=self.donothing, accelerator="Ctrl+R")

        editmenu.add_separator()

        editmenu.add_command(label="Cut", command=self.donothing, accelerator="Ctrl+T")
        editmenu.add_command(label="Copy", command=self.donothing,accelerator="Ctrl+C")
        editmenu.add_command(label="Paste", command=self.donothing, accelerator="Ctrl+V")
        editmenu.add_command(label="Delete", command=self.donothing)
        editmenu.add_command(label="Select All", command=self.donothing, accelerator="Ctrl+A")

        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.donothing, accelerator="Ctrl+H")
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)              
        self.master.config(menu=menubar)

    def window_and_widgets_layout(self, master): #, nodePanel):         
        self.master.grid_rowconfigure(0,weight=1)
        self.master.grid_columnconfigure(0,weight=1)

        self.ops_label = Label(self.master, text= "Choose Operation")
        self.ops_entry = Entry(self.master)
        self.ops_label.pack({"side": "left"})
        self.ops_entry.pack({"side": "right"})
        
        self.ops_button_save = Button(self.master, text = "Save", fg = "grey", command = self.saveForm)
        self.ops_button_save.pack({"side": "left"})
#       self.ops_button.grid(row = 1, column = 0, sticky = W+E+N+S)

        self.ops_button_cancel = Button(self.master, text = "Cancel", command = self.cancelForm, fg = "grey")
        self.ops_button_cancel.pack({"side": "left"})
    
        # Left-most pane
        left_pane = PanedWindow(master,orient=VERTICAL) # self, master
        left_pane.pack(fill=BOTH, expand=1)
        #left = Label(m_pane, text="left pane")
        #left_pane.add(left)
        
        self.treeview = ttk.Treeview(master, columns=("Directory","File contents"))
        left_pane.add(self.treeview)
        # Column headers here 
        self.treeview.heading('#0', text='Directory')        
        self.treeview.heading('#1', text='File Content')
        self.treeview.column('#0', stretch=Tkinter.YES)
        self.treeview.column('#1', stretch=Tkinter.YES)        
        #self.treeview.grid(row=4, columnspan=4, sticky='nsew')
        
        # Right-most pane
        right_pane = PanedWindow(left_pane,orient=VERTICAL) # self, master      
        right = Label(right_pane, text="right pane")
        right_pane.add(right)
        #Frame.__init__(self, master)    
        #self.master=master
        # self.pack(expand=Y, fill=BOTH)
        #self.createPanel ()
def main():
    root = Tkinter.Tk() 
    node = nodeEdit(master=root)
    node.createPanel(master=root)
 #   for i in range(4):
 #       root.columnconfigure(0, weight=1)
 #   for i in range(1,3):
 #       root.rowconfigure(1, weight=1)
    root.mainloop()  #node.mainloop() 
#    root.destroy()
    
if __name__ == "__main__":
    main()
