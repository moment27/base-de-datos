#Metodos y temas empleados en clases
import subprocess
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Distric_list_Ad_NavyDB import *

def Limpiar_PSW():
    global password_text
    password_text.delete(0,"end")
def Limpiar_USER():
    global user_text
    user_text.delete(0,"end")

def Volver():
    ventana_crdistric.destroy()
    subprocess.Popen(["python","Admin/Ventana_Admin.py"])

def Crear_Distric_C():
    global user_text
    nombre_distric = user_text.get()
    if nombre_distric=="":
        print("El campo está vacío")
        return
    resultado = L_Distrito().Crear_Distric(nombre_distric)

    if resultado:
        print("Distrito creado exitosamente")
        Limpiar_USER()
        ventana_crdistric.destroy()
        subprocess.Popen(["python","Admin/Ventana_Admin.py"])
    else:
        print("Error al crear el distrito")


#Interfaz gráfica
import customtkinter as ctk
from PIL import Image
#Propiedades de la ventana
ventana_crdistric=ctk.CTk()
ventana_crdistric.geometry("620x620+740+90")
ventana_crdistric.title("Editar Distrito")
ventana_crdistric.iconbitmap("Images/ico (1).ico")
ventana_crdistric.resizable(False,False)


titulo=ctk.CTkLabel(ventana_crdistric,text="Editar Distrito",font=("Ubuntu",57))
titulo.place(x=83)


img_logo=Image.open("Images/Distrito.png")
logo_ctk=ctk.CTkImage(dark_image=img_logo,size=(65,65))
logo=ctk.CTkLabel(ventana_crdistric,image=logo_ctk,text="")
logo.place(x=459,y=5)



user=ctk.CTkLabel(ventana_crdistric,text="Nombre del Distrito:",font=("Ubuntu",37))
user.place(x=110,y=160)
user_text=ctk.CTkEntry(ventana_crdistric,font=("Ubuntu",23),width=270)
user_text.place(x=110,y=235)



img_tash=Image.open("Images/tash.png")
tash_ctk=ctk.CTkImage(dark_image=img_tash,size=(30,30))
tash=ctk.CTkButton(ventana_crdistric,image=tash_ctk,text="",width=40,fg_color="#242424",hover_color="#a5a4a4",command=Limpiar_USER)
tash.place(x=400,y=232)

img_back=Image.open("Images/back.png")
back_ctk=ctk.CTkImage(dark_image=img_back,size=(30,30))
back=ctk.CTkButton(ventana_crdistric,image=back_ctk,text="Volver",font=("Ubuntu",23),width=40,fg_color="#242424",hover_color="#a5a4a4",command=Volver)
back.place(x=150,y=332)

img_conf=Image.open("Images/icon_confirma.png")
conf_ctk=ctk.CTkImage(dark_image=img_conf,size=(30,30))
conf=ctk.CTkButton(ventana_crdistric,image=conf_ctk,text="Confirmar",font=("Ubuntu",23),width=40,fg_color="#242424",hover_color="#a5a4a4",command=Crear_Distric_C)
conf.place(x=299,y=332)


ventana_crdistric.mainloop()