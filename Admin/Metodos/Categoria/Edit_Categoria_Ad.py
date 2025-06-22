#Metodos y temas empleados en clases
import subprocess
import sys
import os
#Para que me reconozca los otros directorios
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Categoria_list_Ad_NavyDB import *

def Limpiar_PSW():
    global password_text
    password_text.delete(0,"end")
def Limpiar_USER():
    global user_text
    user_text.delete(0,"end")

def Volver():
    ventana_crCat.destroy()
    subprocess.Popen(["python","Admin/Ventana_Admin.py"])

def Crear_Categoria_C():
    global user_text
    nombre_categoria = user_text.get()
    if nombre_categoria=="":
        print("El campo está vacío")
        return
    resultado = L_Categoria().Crear_Categoria(nombre_categoria)
    if resultado:
        print("Categoría creada exitosamente")
        Limpiar_USER()
        ventana_crCat.destroy()
        subprocess.Popen(["python","Admin/Ventana_Admin.py"])
    else:
        print("Error al crear la categoría")   



#Interfaz gráfica
import customtkinter as ctk
from PIL import Image
#Propiedades de la ventana
ventana_crCat=ctk.CTk()
ventana_crCat.geometry("620x620+740+90")
ventana_crCat.title("Editar Categoría")
ventana_crCat.iconbitmap("Images/ico (1).ico")
ventana_crCat.resizable(False,False)


titulo=ctk.CTkLabel(ventana_crCat,text="Editar Categoria",font=("Ubuntu",54))
titulo.place(x=65)


img_logo=Image.open("Images/Categoria.png")
logo_ctk=ctk.CTkImage(dark_image=img_logo,size=(65,65))
logo=ctk.CTkLabel(ventana_crCat,image=logo_ctk,text="")
logo.place(x=468,y=5)



user=ctk.CTkLabel(ventana_crCat,text="Nombre de la Categoria:",font=("Ubuntu",37))
user.place(x=80,y=160)
user_text=ctk.CTkEntry(ventana_crCat,font=("Ubuntu",23),width=300)
user_text.place(x=89,y=235)



img_tash=Image.open("Images/tash.png")
tash_ctk=ctk.CTkImage(dark_image=img_tash,size=(30,30))
tash=ctk.CTkButton(ventana_crCat,image=tash_ctk,text="",width=40,fg_color="#242424",hover_color="#a5a4a4",command=Limpiar_USER)
tash.place(x=400,y=232)

img_tash=Image.open("Images/back.png")
tash_ctk=ctk.CTkImage(dark_image=img_tash,size=(30,30))
tash=ctk.CTkButton(ventana_crCat,image=tash_ctk,text="Volver",font=("Ubuntu",23),width=40,fg_color="#242424",hover_color="#a5a4a4",command=Volver)
tash.place(x=150,y=332)

img_tash=Image.open("Images/icon_confirma.png")
tash_ctk=ctk.CTkImage(dark_image=img_tash,size=(30,30))
tash=ctk.CTkButton(ventana_crCat,image=tash_ctk,text="Confirmar",font=("Ubuntu",23),width=40,fg_color="#242424",hover_color="#a5a4a4",command=Crear_Categoria_C)
tash.place(x=299,y=332)


ventana_crCat.mainloop()