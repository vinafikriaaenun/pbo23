import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W
from fungsi import luas_prisma_segitiga,volume_prisma_segitiga

def hitung_luas():
    alas_segitiga = float(txtalas_segitiga.get())
    tinggi_segitiga = float(txttinggi_segitiga.get())
    tinggi_prisma = float(txttinggi_prisma.get())

    L = luas_prisma_segitiga(alas_segitiga,tinggi_segitiga,tinggi_prisma)

    txtLuas.delete(0, END)
    txtLuas.insert(END,L)

def hitung_volume():
    alas_segitiga = float(txtalas_segitiga.get())
    tinggi_segitiga = float(txttinggi_segitiga.get())
    tinggi_prisma = float(txttinggi_prisma.get())

    v = volume_prisma_segitiga(alas_segitiga,tinggi_segitiga,tinggi_prisma)
    
    txtVolume.delete(0,END)
    txtVolume.insert(END,v)

def hitung():
    hitung_luas()
    hitung_volume()

# Create tkinter object app = tk.Tk()
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Luas Permukaan dan Volume prisma segitiga")

# Windows
frame = Frame(app) 
frame.pack(padx=20, pady=20)

# Label Nama
nama = Label(frame, text="Nama : Vina Pikria Aenun") 
nama.grid(row=0, column=0, columnspan=2, sticky=W, padx=5, pady=5,)

# Label Alas Segitiga
alas_segitiga_label = Label(frame, text="alas_segitiga :") 
alas_segitiga_label.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi Segitiga
tinggi_segitiga = Label(frame, text="tinggi_segitiga :") 
tinggi_segitiga.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Label tinggi prisma
tinggi_prisma = Label(frame, text="tinggi_prisma :") 
tinggi_prisma.grid(row=4, column=0, sticky=W, padx=5, pady=5)

#Textbox
txtalas_segitiga= Entry(frame)
txtalas_segitiga.grid(row=2, column=1, sticky=W, padx=5, pady=5)

#Textbox
txttinggi_segitiga= Entry(frame)
txttinggi_segitiga.grid(row=3, column=1, sticky=W, padx=5, pady=5)

#Textbox
txttinggi_prisma= Entry(frame)
txttinggi_prisma.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas : ")
luas.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output label Volume
Volume = Label(frame, text="Volume : ")
Volume.grid(row=7, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=6, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume = Entry(frame)
txtVolume.grid(row=7, column=1, sticky=W, padx=5, pady=5)

app.mainloop()