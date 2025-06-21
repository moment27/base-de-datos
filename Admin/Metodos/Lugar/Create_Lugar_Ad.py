#Metodos y temas empleados en clases
import subprocess

def Limpiar_PSW():
    global password_text
    password_text.delete(0,"end")
def Limpiar_USER():
    global user_text
    user_text.delete(0,"end")


#Interfaz gráfica
import customtkinter as ctk
from PIL import Image
#Propiedades de la ventana
ventana_crlugar=ctk.CTk()
ventana_crlugar.geometry("620x620+740+90")
ventana_crlugar.title("Crear Lugar")
ventana_crlugar.iconbitmap("Images/ico (1).ico")
ventana_crlugar.resizable(False,False)


titulo=ctk.CTkLabel(ventana_crlugar,text="Login",font=("Ubuntu",70))
titulo.pack()


img_logo=Image.open("Images/Login.png")
logo_ctk=ctk.CTkImage(dark_image=img_logo,size=(60,60))
logo=ctk.CTkLabel(ventana_crlugar,image=logo_ctk,text="")
logo.place(x=400,y=15)



user=ctk.CTkLabel(ventana_crlugar,text="Usuario:",font=("Ubuntu",37))
user.place(x=110,y=130)
user_text=ctk.CTkEntry(ventana_crlugar,font=("Ubuntu",23),width=200)
user_text.place(x=260,y=137)



img_tash=Image.open("Images/tash.png")
tash_ctk=ctk.CTkImage(dark_image=img_tash,size=(30,30))
tash=ctk.CTkButton(ventana_crlugar,image=tash_ctk,text="",width=40,fg_color="#242424",hover_color="#a5a4a4",command=Limpiar_USER)
tash.place(x=470,y=135)


password=ctk.CTkLabel(ventana_crlugar,text="Contraseña:",font=("Ubuntu",37))
password.place(x=46,y=214)
password_text=ctk.CTkEntry(ventana_crlugar,font=("Ubuntu",23),width=200)
password_text.place(x=259,y=221)

tash1=ctk.CTkButton(ventana_crlugar,image=tash_ctk,text="",width=40,fg_color="#242424",hover_color="#a5a4a4",command=Limpiar_PSW)
tash1.place(x=470,y=221)



categoria_user=ctk.CTkLabel(ventana_crlugar,text="Categoria:",font=("Ubuntu",37))
categoria_user.place(x=75,y=297)


cat_user=["Normal","Admin"]
user_cat=ctk.CTkComboBox(ventana_crlugar,values=cat_user,font=("Arial",19),width=200,height=34,state="readonly")
user_cat.place(x=260,y=310)
user_cat.set("Categoria Usuario")





ventana_crlugar.mainloop()