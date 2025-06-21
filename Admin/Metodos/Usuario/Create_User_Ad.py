#Metodos y temas empleados en clases
import subprocess
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from User_List_Ad_NavyDB import *

def Limpiar_PSW():
    global password_text
    password_text.delete(0,"end")
def Limpiar_USER():
    global user_text
    user_text.delete(0,"end")

def Volver():
    ventana_crUser.destroy()
    subprocess.run(["python","Admin/Ventana_Admin.py"])

def Crear_Usuario_C():
    global user_text,password_text
    nombre_user = user_text.get()
    password = password_text.get()
    categoria= user_cat.get()
    if nombre_user == "" or password =="":
        print("El campo está vacío")
        return
    resultado = L_Usuario().Crear_Usuario(nombre_user,password,categoria)
    if resultado:
        print("Usuario creada exitosamente")
        Limpiar_USER()
        ventana_crUser.destroy()
        subprocess.Popen(["python","Admin/Ventana_Admin.py"])
    else:
        print("Error al crear el usuario") 

#Interfaz gráfica
import customtkinter as ctk
from PIL import Image
#Propiedades de la ventana
ventana_crUser=ctk.CTk()
ventana_crUser.geometry("620x620+740+90")
ventana_crUser.title("Login")
ventana_crUser.iconbitmap("Images/ico (1).ico")
ventana_crUser.resizable(False,False)


titulo=ctk.CTkLabel(ventana_crUser,text="Login",font=("Ubuntu",70))
titulo.pack()


img_logo=Image.open("Images/Login.png")
logo_ctk=ctk.CTkImage(dark_image=img_logo,size=(60,60))
logo=ctk.CTkLabel(ventana_crUser,image=logo_ctk,text="")
logo.place(x=400,y=15)



user=ctk.CTkLabel(ventana_crUser,text="Usuario:",font=("Ubuntu",37))
user.place(x=110,y=130)
user_text=ctk.CTkEntry(ventana_crUser,font=("Ubuntu",23),width=200)
user_text.place(x=260,y=137)



img_tash=Image.open("Images/tash.png")
tash_ctk=ctk.CTkImage(dark_image=img_tash,size=(30,30))
tash=ctk.CTkButton(ventana_crUser,image=tash_ctk,text="",width=40,fg_color="#242424",hover_color="#a5a4a4",command=Limpiar_USER)
tash.place(x=470,y=135)


password=ctk.CTkLabel(ventana_crUser,text="Contraseña:",font=("Ubuntu",37))
password.place(x=46,y=214)
password_text=ctk.CTkEntry(ventana_crUser,font=("Ubuntu",23),width=200)
password_text.place(x=259,y=221)

tash1=ctk.CTkButton(ventana_crUser,image=tash_ctk,text="",width=40,fg_color="#242424",hover_color="#a5a4a4",command=Limpiar_PSW)
tash1.place(x=470,y=221)



categoria_user=ctk.CTkLabel(ventana_crUser,text="Categoria:",font=("Ubuntu",37))
categoria_user.place(x=75,y=297)


cat_user=["Normal","Admin"]
user_cat=ctk.CTkComboBox(ventana_crUser,values=cat_user,font=("Arial",19),width=200,height=34,state="readonly")
user_cat.place(x=260,y=310)
user_cat.set("Categoria Usuario")

img_back=Image.open("Images/back.png")
back_ctk=ctk.CTkImage(dark_image=img_back,size=(30,30))
back=ctk.CTkButton(ventana_crUser,image=back_ctk,text="Volver",font=("Ubuntu",23),width=40,fg_color="#242424",hover_color="#a5a4a4",command=Volver)
back.place(x=160,y=408)

img_conf=Image.open("Images/icon_confirma.png")
conf_ctk=ctk.CTkImage(dark_image=img_conf,size=(30,30))
conf=ctk.CTkButton(ventana_crUser,image=conf_ctk,text="Confirmar",font=("Ubuntu",23),width=40,fg_color="#242424",hover_color="#a5a4a4",command=Crear_Usuario_C)
conf.place(x=300,y=408)

ventana_crUser.mainloop()