import subprocess
from Admin.User_List_Ad_NavyDB import L_Usuario

def Limpiar_USER():
    global ingr_user_text
    ingr_user_text.delete(0,"end")

def Limpiar_NEW_PSW():
    global ingr_new_psw_text
    ingr_new_psw_text.delete(0,"end")
    
def Limpiar_RPT_NEW_PSW():
    global ingr_dnv_new_psw_text
    ingr_dnv_new_psw_text.delete(0,"end")    

def Regresar_Login():
    ventana_olv_psw.destroy()
    subprocess.Popen(["python","Login.py"])

def confirmar_cambio():
    global ingr_user_text,ingr_new_psw_text,ingr_dnv_new_psw_text

    usuario=ingr_user_text.get().strip()
    new_pswd=ingr_new_psw_text.get().strip()
    rpt_pswd=ingr_dnv_new_psw_text.get().strip()

    if usuario=="" or new_pswd=="" or rpt_pswd=="" :
        print("Campos Vacíos")
        return
    if new_pswd!=rpt_pswd:
        print("Error, las contraseñas no coinciden")
        return

    gestor=L_Usuario()
    resultado=gestor.Actualizar_Contraseña(usuario,rpt_pswd)

    if resultado:
        print("Cambio Exitoso")
        ventana_olv_psw.destroy()
        subprocess.Popen(["python","Login.py"])
    else:
        print("No se pudo actualizar")
         

import customtkinter as ctk
from PIL import Image


ventana_olv_psw=ctk.CTk()
ventana_olv_psw.title("Olvidar Contraseña")
ventana_olv_psw.geometry("620x620+740+90")
ventana_olv_psw.iconbitmap("Images/ico (1).ico")
ventana_olv_psw.resizable(False,False)


titulo=ctk.CTkLabel(ventana_olv_psw,text="Olvidar Contraseña",font=("Ubuntu",42))
titulo.place(x=87)

img_titulo=Image.open("Images/rest_psw.png")
titulo_ctk=ctk.CTkImage(dark_image=img_titulo,size=(75,75))
lg_titulo=ctk.CTkLabel(ventana_olv_psw,image=titulo_ctk,text="")
lg_titulo.place(x=454,y=-7)




ingr_user=ctk.CTkLabel(ventana_olv_psw,text="Ingresa usuario:",font=("Ubuntu",30))
ingr_user.place(x=64,y=120)
ingr_user_text=ctk.CTkEntry(ventana_olv_psw,font=("Ubuntu",23),width=200)
ingr_user_text.place(x=289,y=120)


img_tash=Image.open("Images/tash.png")
tash_ctk=ctk.CTkImage(dark_image=img_tash,size=(30,30))
tash=ctk.CTkButton(ventana_olv_psw,image=tash_ctk,text="",width=40,fg_color="#242424",hover_color="#a5a4a4",command=Limpiar_USER)
tash.place(x=497,y=118)

ingr_new_psw=ctk.CTkLabel(ventana_olv_psw,text="Contraseña nueva:",font=("Ubuntu",30))
ingr_new_psw.place(x=27,y=210)
ingr_new_psw_text=ctk.CTkEntry(ventana_olv_psw,font=("Ubuntu",23),width=200)
ingr_new_psw_text.place(x=289,y=210)


tash1=ctk.CTkButton(ventana_olv_psw,image=tash_ctk,text="",width=40,fg_color="#242424",hover_color="#a5a4a4",command=Limpiar_NEW_PSW)
tash1.place(x=497,y=210)




ingr_dnv_new_psw=ctk.CTkLabel(ventana_olv_psw,text="Repítalo (paso 2):",font=("Ubuntu",30))
ingr_dnv_new_psw.place(x=42,y=300)
ingr_dnv_new_psw_text=ctk.CTkEntry(ventana_olv_psw,font=("Ubuntu",23),width=200)
ingr_dnv_new_psw_text.place(x=289,y=300)

tash1=ctk.CTkButton(ventana_olv_psw,image=tash_ctk,text="",width=40,fg_color="#242424",hover_color="#a5a4a4",command=Limpiar_RPT_NEW_PSW)
tash1.place(x=497,y=300)



img_confirmar=Image.open("Images/icon_confirma.png")
confimar_ctk=ctk.CTkImage(dark_image=img_confirmar,size=(40,40))
confimar=ctk.CTkButton(ventana_olv_psw,text="Confirmar",font=("Ubuntu",19),image=confimar_ctk,fg_color="#242424",hover_color="#a5a4a4",command=confirmar_cambio)
confimar.place(x=223,y=385)

img_regresar=Image.open("Images/back.png")
regresar_ctk=ctk.CTkImage(dark_image=img_regresar,size=(40,40))
regresar=ctk.CTkButton(ventana_olv_psw,text="Regresar",image=regresar_ctk,font=("Ubuntu",19),fg_color="#242424",hover_color="#a5a4a4",command=Regresar_Login)
regresar.place(x=222,y=470)





ventana_olv_psw.mainloop()