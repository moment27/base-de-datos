#Metodos y temas empleados en clases
import subprocess

def Limpiar_PSW():
    global password_text
    password_text.delete(0,"end")
def Limpiar_USER():
    global user_text
    user_text.delete(0,"end")

def Limipiar_Categoria():
    global categoria_text
    categoria_text.delete(0,"end")

def Limpiar_Distrito():
    global distrito_text
    distrito_text.delete(0,"end")

def Volver():
    ventana_crlugar.destroy()
    subprocess.Popen(["python", "Admin/Ventana_Admin.py"])



#Interfaz gráfica
import customtkinter as ctk
from PIL import Image
#Propiedades de la ventana
ventana_crlugar=ctk.CTk()
ventana_crlugar.geometry("620x620+740+90")
ventana_crlugar.title("Crear Lugar")
ventana_crlugar.iconbitmap("Images/ico (1).ico")
ventana_crlugar.resizable(False,False)


titulo=ctk.CTkLabel(ventana_crlugar,text="Crear Lugar",font=("Ubuntu",67))
titulo.place(x=93)


img_logo=Image.open("Images/Distrito.png")
logo_ctk=ctk.CTkImage(dark_image=img_logo,size=(60,60))
logo=ctk.CTkLabel(ventana_crlugar,image=logo_ctk,text="")
logo.place(x=455,y=15)



user=ctk.CTkLabel(ventana_crlugar,text="Nombre:",font=("Ubuntu",37))
user.place(x=100,y=130)
user_text=ctk.CTkEntry(ventana_crlugar,font=("Ubuntu",23),width=200)
user_text.place(x=260,y=137)



img_tash=Image.open("Images/tash.png")
tash_ctk=ctk.CTkImage(dark_image=img_tash,size=(30,30))
tash=ctk.CTkButton(ventana_crlugar,image=tash_ctk,text="",width=40,fg_color="#242424",hover_color="#a5a4a4",command=Limpiar_USER)
tash.place(x=470,y=135)


password=ctk.CTkLabel(ventana_crlugar,text="Coordenadas:",font=("Ubuntu",37))
password.place(x=17,y=214)
password_text=ctk.CTkEntry(ventana_crlugar,font=("Ubuntu",23),width=200)
password_text.place(x=259,y=221)

tash1=ctk.CTkButton(ventana_crlugar,image=tash_ctk,text="",width=40,fg_color="#242424",hover_color="#a5a4a4",command=Limpiar_PSW)
tash1.place(x=470,y=221)



categoria=ctk.CTkLabel(ventana_crlugar,text="Categoria:",font=("Ubuntu",37))
categoria.place(x=75,y=297)
categoria_text=ctk.CTkEntry(ventana_crlugar,font=("Ubuntu",23),width=200)
categoria_text.place(x=259,y=304)

tash2=ctk.CTkButton(ventana_crlugar,image=tash_ctk,text="",width=40,fg_color="#242424",hover_color="#a5a4a4",command=Limipiar_Categoria)
tash2.place(x=470,y=304)


distrito=ctk.CTkLabel(ventana_crlugar,text="Distrito:",font=("Ubuntu",37))
distrito.place(x=110,y=380)
distrito_text=ctk.CTkEntry(ventana_crlugar,font=("Ubuntu",23),width=200)
distrito_text.place(x=259,y=387)

tash3=ctk.CTkButton(ventana_crlugar,image=tash_ctk,text="",width=40,fg_color="#242424",hover_color="#a5a4a4",command=Limpiar_Distrito)
tash3.place(x=470,y=387)


img_back=Image.open("Images/back.png")
back_ctk=ctk.CTkImage(dark_image=img_back,size=(45,45))
back=ctk.CTkButton(ventana_crlugar,text="Volver",image=back_ctk,fg_color="#242424",font=("Ubuntu",21),command=Volver)
back.place(x=130,y=500)


img_conf=Image.open("Images/icon_confirma.png")
conf_ctk=ctk.CTkImage(dark_image=img_conf,size=(45,45))
conf=ctk.CTkButton(ventana_crlugar,text="Confirmar",image=conf_ctk,fg_color="#242424",font=("Ubuntu",21))
conf.place(x=320,y=500)









ventana_crlugar.mainloop()