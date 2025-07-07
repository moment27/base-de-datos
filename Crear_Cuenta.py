#Metodos para los botones
from Admin.User_List_Ad_NavyDB import L_Usuario
def Limpiar_PSW():
    global password_text
    password_text.delete(0,"end")
def Limpiar_USER():
    global user_text
    user_text.delete(0,"end")

#def Regresar_Login():
    #ventana_login.destroy()
    #subprocess.Popen(["python","Olvidar_Contraseña.py"])

class FormularioCrearCuenta():
    global user_text
    user_text = None

    global password_text
    password_text = None


    def guardar_usuario():
        global user_text,password_text

        try:
            if user_text is None or password_text is None:
                print("No hay nada escrito")
                return 
            user=user_text.get().strip()
            paswd=password_text.get().strip()

            if user.strip()=="" or paswd.strip()=="":
                print("Campos vacíos")
                return 

            usuario_model=L_Usuario()
            categoria="normal"

            cuenta=usuario_model.Crear_Usuario(user,paswd,categoria)
            if cuenta:
                print("Usuario Creado Correctamente")
                Limpiar_PSW()
                Limpiar_USER()
                ventana_new_count.destroy()
                subprocess.Popen(["python","Login.py"])
            else:
                print("Error al crear el usuario")
        except Exception as error:
            print(f"Error al ingresar los datos: {error}")

        




import customtkinter as ctk
from PIL import Image
import subprocess
from User_New_NaviDB import *
from Conexion_MySQL import *
#Propiedades de la ventana
ventana_new_count=ctk.CTk()
ventana_new_count.geometry("620x620+740+90")
ventana_new_count.title("Crear Cuenta")
ventana_new_count.iconbitmap("Images/ico (1).ico")
ventana_new_count.resizable(False,False)


titulo=ctk.CTkLabel(ventana_new_count,text="Crear Cuenta",font=("Ubuntu",52))
titulo.pack()


img_logo=Image.open("Images/Login.png")
logo_ctk=ctk.CTkImage(dark_image=img_logo,size=(50,50))
logo=ctk.CTkLabel(ventana_new_count,image=logo_ctk,text="")
logo.place(x=468,y=15)



user=ctk.CTkLabel(ventana_new_count,text="Usuario:",font=("Ubuntu",37))
user.place(x=110,y=130)
user_text=ctk.CTkEntry(ventana_new_count,font=("Ubuntu",23),width=200)
user_text.place(x=260,y=137)



img_tash=Image.open("Images/tash.png")
tash_ctk=ctk.CTkImage(dark_image=img_tash,size=(30,30))
tash=ctk.CTkButton(ventana_new_count,image=tash_ctk,text="",width=40,fg_color="#242424",hover_color="#a5a4a4",command=Limpiar_USER)
tash.place(x=470,y=135)


password=ctk.CTkLabel(ventana_new_count,text="Contraseña:",font=("Ubuntu",37))
password.place(x=46,y=214)
password_text=ctk.CTkEntry(ventana_new_count,font=("Ubuntu",23),width=200)
password_text.place(x=259,y=221)

tash1=ctk.CTkButton(ventana_new_count,image=tash_ctk,text="",width=40,fg_color="#242424",hover_color="#a5a4a4",command=Limpiar_PSW)
tash1.place(x=470,y=221)


img_logo_new_count=Image.open("Images/Login.png")
logo_ctk_nw=ctk.CTkImage(dark_image=img_logo_new_count,size=(40,40))
new_count=ctk.CTkButton(ventana_new_count,text="Crear Cuenta",fg_color="#242424",hover_color="#a5a4a4",font=("Ubuntu",19),image=logo_ctk_nw,command=FormularioCrearCuenta.guardar_usuario)
new_count.place(x=254,y=305)


ventana_new_count.mainloop()