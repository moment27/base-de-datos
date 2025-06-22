#Metodos y temas empleados en clases
import subprocess
from Admin.User_List_Ad_NavyDB import *
def Limpiar_PSW():
    global password_text
    password_text.delete(0,"end")
def Limpiar_USER():
    global user_text
    user_text.delete(0,"end")

def abrir_olvidar_contraseña():
    ventana_login.destroy()
    subprocess.Popen(["python","Olvidar_Contraseña.py"])

def abrir_nueva_cuenta():
    ventana_login.destroy()
    subprocess.Popen(["python","Crear_Cuenta.py"])



#Clase para Validad los datos
class FormularioIniSesion:
    
    def guarda_iniciado(self):
        global user_text,password_text

        try :

            if user_text is None or password_text is None:
                print("No hay nada escrito")
            user=user_text.get()
            paswd=password_text.get()

            if user.strip()=="" or paswd.strip()=="":
                print("Campos Vacíos") 
                return 
            
            categoria=L_Usuario().Obtener_Cat_Usuario(user,paswd)
            
            if categoria:

                Limpiar_PSW()
                Limpiar_USER()


                
                if categoria.lower()=="admin":
                    ventana_login.destroy()
                    subprocess.Popen(["python","Admin/Ventana_Admin.py"])
                else:
                    ventana_login.destroy()    
                    subprocess.Popen(["python","Principal.py"])
                
            else:
                print("Credenciales incorrectas")
            
        except ValueError as error:
            print(f"Error al iniciar sesión{error}")





#Interfaz gráfica
import customtkinter as ctk
from PIL import Image
from User_Login_NaviDB import *
from Conexion_MySQL import *
#Propiedades de la ventana
ventana_login=ctk.CTk()
ventana_login.geometry("620x620+740+90")
ventana_login.title("Login")
ventana_login.iconbitmap("Images/ico (1).ico")
ventana_login.resizable(False,False)


titulo=ctk.CTkLabel(ventana_login,text="Login",font=("Ubuntu",70))
titulo.pack()


img_logo=Image.open("Images/Login.png")
logo_ctk=ctk.CTkImage(dark_image=img_logo,size=(60,60))
logo=ctk.CTkLabel(ventana_login,image=logo_ctk,text="")
logo.place(x=400,y=15)



user=ctk.CTkLabel(ventana_login,text="Usuario:",font=("Ubuntu",37))
user.place(x=110,y=130)
user_text=ctk.CTkEntry(ventana_login,font=("Ubuntu",23),width=200)
user_text.place(x=260,y=137)



img_tash=Image.open("Images/tash.png")
tash_ctk=ctk.CTkImage(dark_image=img_tash,size=(30,30))
tash=ctk.CTkButton(ventana_login,image=tash_ctk,text="",width=40,fg_color="#242424",hover_color="#a5a4a4",command=Limpiar_USER)
tash.place(x=470,y=135)


password=ctk.CTkLabel(ventana_login,text="Contraseña:",font=("Ubuntu",37))
password.place(x=46,y=214)
password_text=ctk.CTkEntry(ventana_login,font=("Ubuntu",23),width=200)
password_text.place(x=259,y=221)

tash1=ctk.CTkButton(ventana_login,image=tash_ctk,text="",width=40,fg_color="#242424",hover_color="#a5a4a4",command=Limpiar_PSW)
tash1.place(x=470,y=221)


img_sesion=Image.open("Images/ini_sesion.png")
sesion_ctk=ctk.CTkImage(dark_image=img_sesion,size=(45,45))
sesion=ctk.CTkButton(ventana_login,image=sesion_ctk,text="Iniciar Sesión",fg_color="#242424",hover_color="#a5a4a4",font=("Ubuntu",19),command=FormularioIniSesion().guarda_iniciado)
sesion.place(x=240,y=305)


img_rest_psw=Image.open("Images/rest_psw.png")
rest_psw_ctk=ctk.CTkImage(dark_image=img_rest_psw,size=(40,40))
rest_psw=ctk.CTkButton(ventana_login,text="Olvidé la contraseña",image=rest_psw_ctk,fg_color="#242424",hover_color="#a5a4a4",font=("Ubuntu",19),command=abrir_olvidar_contraseña)
rest_psw.place(x=210,y=389)


img_logo_new_count=Image.open("Images/Login.png")
logo_ctk_nw=ctk.CTkImage(dark_image=img_logo_new_count,size=(40,40))
new_count=ctk.CTkButton(ventana_login,text="Crear Cuenta",fg_color="#242424",hover_color="#a5a4a4",font=("Ubuntu",19),image=logo_ctk_nw,command=abrir_nueva_cuenta)
new_count.place(x=250,y=470)


ventana_login.mainloop()