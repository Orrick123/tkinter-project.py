import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo
show = tkinter.Tk()

show.title("Project : Duel")
show.configure(bg="red")
show.geometry("500x500")
show.resizable(False,True)

frame = ttk.Frame(show)
frame.pack(padx=25, pady=25, fill="x", expand=True)

label_class = ttk.Label(frame, text= "Class : ")
label_class.pack(padx=15, pady=15, fill="x", expand=True)

varClass = tkinter.StringVar()

entry_class = ttk.Entry(frame, textvariable = varClass)
entry_class.pack(padx=15, pady=10, fill="x", expand=True)

varname = tkinter.StringVar()

label_name = ttk.Label(frame, text = "name : ")
label_name.pack( padx=15, pady=15, fill="x", expand=True)

entry_name = ttk.Entry(frame, textvariable = varname)
entry_name.pack(padx=15, pady=10, fill="x", expand=True)

vardate = tkinter.StringVar()

label_date = ttk.Label(frame,text= "date : ")
label_date.pack( padx=15, pady=10, fill="x", expand=True)

entry_date = ttk.Entry(frame, textvariable = vardate)
entry_date.pack(padx=15, pady=10, fill="x", expand=True)

def AksiKirim():
    output = f" Class yang telah dipilihkan adalah {varClass.get()}, name yang telah dipilihkan adalah {varname.get()}, dan Musuh yang akan dilawan adalah {varMusuh.get()}"
    showinfo(message= output)
    
submit = ttk.Button( frame, text="Kirim", command=AksiKirim )
submit.pack( padx=15, pady=10, fill="x", expand=True)
show.mainloop()