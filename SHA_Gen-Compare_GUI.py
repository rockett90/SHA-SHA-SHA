import tkinter
from tkinter import *
from tkinter import ttk
from pathlib import Path
from tkinter import filedialog
import hashlib

#######################################
#Variables, Functions etc
#######################################

buffer = 800000   #variable for the read buffer size in bits (100kB)
genMyFile = ""     #variable to store the file path
compMyFile = ""
hash_gen = ""
hash_comp = ""

def genBrowseForFiles():
    global genMyFile
    genMyFile = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    
def compBrowseForFiles():
    global compMyFile
    compMyFile = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    
def genHash():
    global hash_gen
    with open(genMyFile, 'rb') as f:   #read file as binary
        while True:
            data = f.read(buffer)
            if not data:
                break
            elif algorithm_gen_combobox.get() == "SHA-1":
                hash_gen.set(hashlib.sha1(data).hexdigest())
            elif algorithm_gen_combobox.get() == "SHA-256":
                hash_gen.set(hashlib.sha256(data).hexdigest())
            elif algorithm_gen_combobox.get() == "SHA-384":
                hash_gen.set(hashlib.sha384(data).hexdigest())
            elif algorithm_gen_combobox.get() == "SHA-512":
                hash_gen.set(hashlib.sha512(data).hexdigest())
            else:
                hash_gen.set("Please Choose an Algorithm from the Drop Down Menu...")
                
def compHash():
    global hash_comp
    with open(compMyFile, 'rb') as f:   #read file as binary
        while True:
            data = f.read(buffer)
            if not data:
                break
            elif algorithm_comp_combobox.get() == "SHA-1":
                hash_comp.set(hashlib.sha1(data).hexdigest())
            elif algorithm_comp_combobox.get() == "SHA-256":
                hash_comp.set(hashlib.sha256(data).hexdigest())
            elif algorithm_comp_combobox.get() == "SHA-384":
                hash_comp.set(hashlib.sha384(data).hexdigest())
            elif algorithm_comp_combobox.get() == "SHA-512":
                hash_comp.set(hashlib.sha512(data).hexdigest())
            else:
                hash_comp.set("Please Choose an Algorithm from the Drop Down Menu...")
            comparison()
     
def comparison():
    if comp_entry.get() == "":
        comp_result.set("Please Enter Hash for Comparison")
    elif hash_comp.get() == comp_entry.get():
        comp_result.set("These Match!")
    else:
        comp_result.set("These Don't Match :(")


#######################################
#Doing all the GUI bits and bobs
#######################################

#Creating the main window
window = tkinter.Tk()
window.resizable(width=False, height=False)   #unable to resize the window
window.geometry("652x347")    #sizing the window
window.title("SHA Generation / Comparison Tool")    #giving it a title
window_icon = tkinter.PhotoImage(file=(Path(__file__).parent / "icon.png"))
window.iconphoto(True, window_icon)

#Variables for the GUI
hash_gen = StringVar();
hash_gen.set("")
hash_comp = StringVar();
hash_comp.set("")
comp_result = StringVar();
comp_result.set("")
    
#Creating the inner frame
frame = tkinter.Frame(window)
frame.pack()

#Creating frame, row 1 of 2, the generation frame
sha_gen_frame = tkinter.LabelFrame(frame, text="SHA.Generator")
sha_gen_frame.grid(row= 0, column=0, padx=0, pady=10)

algorithm_gen_combobox = ttk.Combobox(sha_gen_frame, values=["Choose Algorithm...", "SHA-1", "SHA-256", "SHA-384", "SHA-512"])
algorithm_gen_combobox.current(0)   #puts the first entry as default (Choose)
algorithm_gen_combobox.grid(row = 0, column = 0, padx = 5)

gen_choose_file_button = ttk.Button(sha_gen_frame, width = 22,  text ="Browse for File...", command = genBrowseForFiles)
gen_choose_file_button.grid(row = 0, column = 1, padx = 5)

gen_generate_button = ttk.Button(sha_gen_frame, width = 22,  text ="Generate Hash", command = genHash)
gen_generate_button.grid(row = 0, column = 3, padx = 5)

gen_copy_gen_button = ttk.Button(sha_gen_frame, width = 22,  text ="Copy to Clipboard")
gen_copy_gen_button.grid(row = 0, column = 4, padx = 5)

gen_calculated_label = ttk.Label(sha_gen_frame, text = "Generated Hexadecimal Hash")
gen_calculated_label.grid(row = 2, columnspan = 2, padx = 5, pady = (10,0), sticky = "W")

gen_calculated_entry = tkinter.Entry(sha_gen_frame, width = 99, bg = "white", textvariable = hash_gen)
gen_calculated_entry.grid(row = 3, columnspan = 5, padx = 5, pady = (0,10))

#Creating frame, row 2 of 2, the comparison frame
sha_comp_frame = tkinter.LabelFrame(frame, text="SHA.Comparison")
sha_comp_frame.grid(row = 1, column=0, padx=0, pady=5)

algorithm_comp_combobox = ttk.Combobox(sha_comp_frame, values=["Choose Algorithm...", "SHA-1", "SHA-256", "SHA-384", "SHA-512"])
algorithm_comp_combobox.current(0)   #puts the first entry as default (Choose)
algorithm_comp_combobox.grid(row = 0, column = 0, padx = 5)

comp_choose_file_button = ttk.Button(sha_comp_frame, width = 22,  text ="Browse for File...", command = compBrowseForFiles)
comp_choose_file_button.grid(row = 0, column = 1, padx = 5)

comp_generate_button = ttk.Button(sha_comp_frame, width = 22,  text ="Compare Hashes", command = compHash)
comp_generate_button.grid(row = 0, column = 3, padx = 5)

comp_copy_gen_button = ttk.Button(sha_comp_frame, width = 22,  text ="Copy to Clipboard")
comp_copy_gen_button.grid(row = 0, column = 4, padx = 5)

comp_label = ttk.Label(sha_comp_frame, text = "Enter Hash for Comparison")
comp_label.grid(row = 2, columnspan = 2, padx = 5, pady = (10,0), sticky = "W")

comp_entry = tkinter.Entry(sha_comp_frame, width = 99, bg = "light yellow")
comp_entry.grid(row = 3, columnspan = 5, padx = 5, pady = (0,10))

comp_calculated_label = ttk.Label(sha_comp_frame, text = "Generated Hexadecimal Hash")
comp_calculated_label.grid(row = 4, columnspan = 2, padx = 5, pady = (0,0), sticky = "W")

comp_calculated_entry = tkinter.Entry(sha_comp_frame, width = 99, bg = "white", textvariable = hash_comp)
comp_calculated_entry.grid(row = 5, columnspan = 5, padx = 5, pady = (0,10))

comp_result_label = ttk.Label(sha_comp_frame, text = "Comparison Result")
comp_result_label.grid(row = 6, columnspan = 2, padx = 5, pady = (0,0), sticky = "W")

comp_result_entry = tkinter.Entry(sha_comp_frame, width = 35, bg = "white", textvariable = comp_result)
comp_result_entry.grid(row = 7, columnspan = 5, padx = 5, pady = (0,10), sticky = "W")

window.mainloop()
