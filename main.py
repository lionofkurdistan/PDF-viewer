from tkinter import*
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf
import os 
root = Tk()
root.geometry('500x650+400+10')
root.title('PDF viewer By DEV lion of kurdistan')
root.resizable (False,False)
root.configure(background='white')

def bro ():
        filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                              title='select book [Lion Of Kurdistan]',
                                              filetype=(('PDF File','.pdf'),
                                                        ('PDF File','PDF'),
                                                        ('PDF','txt')
                                                       
                                                       )
                                             
                                             )
        v1 = pdf.ShowPdf()
        v2 = v1.pdf_view(root, pdf_location=open(filename, 'r'),width=77,height=100)
        v2.pack(pady=(0,0))
                                              




B = Button(root, text="open book",width=58,font='Tajawal 16',fg='white',bg='red',cursor='hand2',command=bro)
B.pack()

photo1 = PhotoImage(file='logo.png')
ph_1 = Label(root, image=photo1,width=500,height=530,bd=5,relief='groove')
ph_1.place(x=1,y=50)

L = Label(root, text='By Dev: Lion Of Kurdistan', font='Tajawal 14',fg='red', bg='white' )
L.place(x=170,y=600)


root.mainloop()
