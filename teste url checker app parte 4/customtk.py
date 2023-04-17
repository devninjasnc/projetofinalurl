import tkinter
import customtkinter
from PIL import ImageTk, Image
import tkinter.messagebox as MessageBox
import subprocess

customtkinter.set_appearance_mode("Dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green,white

app = customtkinter.CTk()  # creating custom tkinter window
app.geometry("600x440")
app.title('URL CHECKER')

resposta = tkinter.StringVar()
resposta2 = tkinter.StringVar()



def verificar_():
    nome = entry1.get()
    if nome == 'www.amazon.com.br':
        resposta.set('O SITE É SEGURO') 
    elif nome == 'www.americanas.com.br': 
        resposta.set('O SITE É SEGURO') 
    elif nome == 'www.magazineluiza.com.br':  
        resposta.set('O SITE É SEGURO')  
    else:
        resposta2.set('O SITE É FALSO')

def limpar():
    entry1.delete(0, tkinter.END)
    resposta.set('')
    resposta2.set('')
    
    


    
    

def tutorial():
    subprocess.run(['python', 'C:\\Users\\bebel\\Videos\\teste url checker app parte 4\\tutorial.py'])

img1 = ImageTk.PhotoImage(file='imagens\pattern.png')
l1 = customtkinter.CTkLabel(master=app, image=img1)
l1.pack()
# CRIANDO O FRAME
frame = customtkinter.CTkFrame(master=l1, width=320, height=370, corner_radius=15, fg_color='White')
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

img2 = ImageTk.PhotoImage(file='imagens\LogoUrl.png')
l2 = customtkinter.CTkLabel(master=frame, image=img2)
l2.place(x=110, y=10)
#img AMAZON


entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='INSIRA A URL')
entry1.place(x=50, y=140)

# CRIAÇÂO DO BOTAO
button1 = customtkinter.CTkButton(master=frame, width=220, text="VERIFICAR", command=verificar_, corner_radius=6)
button1.place(x=50, y=170)
button2 = customtkinter.CTkButton(master=frame, width=220, text="LIMPAR",command=limpar, corner_radius=6)
button2.place(x=50, y=200)
button3 = customtkinter.CTkButton(master=frame, width=220, text="TUTORIAL APP",command=tutorial, corner_radius=6)
button3.place(x=50, y=330)

# Adicionando Label para exibir a resposta
label_resposta = customtkinter.CTkLabel(master=frame, textvariable=resposta, text_color='green')
label_resposta2 = customtkinter.CTkLabel(master=frame, textvariable=resposta2, text_color='red')
label_resposta2.place(x=114, y=250)
label_resposta.place(x=114, y=250)


app.mainloop()
