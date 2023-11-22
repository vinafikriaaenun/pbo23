from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W

class FrmBalok:
    def __init__(self, parent, title):
        self.parent = parent       
        #self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # pasang Label
        Label(mainFrame, text='Panjang:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Lebar:").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi").grid(row=2, column=0, 
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Volume:").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtPanjang = Entry(mainFrame) 
        self.txtPanjang.grid(row=0, column=1, padx=5, pady=5)  
        self.txtLebar = Entry(mainFrame) 
        self.txtLebar.grid(row=1, column=1, padx=5, pady=5) 
        self.txtTinggi = Entry(mainFrame) 
        self.txtTinggi.grid(row=2, column=1, sticky=W, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame) 
        self.txtLuas.grid(row=4, column=1, padx=5, pady=5) 
        self.txtVolume = Entry(mainFrame) 
        self.txtVolume.grid(row=5, column=1, padx=5, pady=5) 
        
        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=3, column=1, padx=5, pady=5)
        
           
    # fungsi "onHitung" berfungsi untuk menghitung luas dan volume Balok  
    def onHitung(self, event=None):
        p = int(self.txtPanjang.get())
        l = int(self.txtLebar.get())
        t = int(self.txtTinggi.get())
        l = (2*p*l) + (2*p*t) + (2*l*t)
        V = p*l*t
        self.txtLuas.delete(0,END)
        self.txtLuas.insert(END,str(l))
        self.txtVolume.delete(0,END)
        self.txtVolume.insert(END,str(l))
               
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmBalok(root, "Program Luas Balok")
    root.mainloop() 