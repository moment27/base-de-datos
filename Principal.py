#Funciones y otros temas aportados al proyecto
def devolver():
    global ubcn_text
    ubcn_text.configure(state="normal")
    ubcn_text.delete(0,"end")
    ubcn_text.insert(0,"-12.045913375221852, -76.95443787206254")
    ubcn_text.configure(state="readonly")

def limpiar():
    global dist_text
    dist_text.delete(0,"end")
def limpiar1():
    global ubcn_text
    ubcn_text.configure(state="normal")
    ubcn_text.delete(0,"end")
    ubcn_text.configure(state="readonly")



#Interfaz gráfica
import customtkinter as ctk
import ctypes
from PIL import Image

#Propiedades de ventana
ventana=ctk.CTk()
ventana.geometry("620x760+740+90")
ventana.title("NavyGo")
ventana.resizable(False,False)
ventana.iconbitmap("Images/ico (1).ico")
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("NaviGo.GRUPO.EDG")

#Labels y otros elementos de nuestro programa
titulo=ctk.CTkLabel(ventana,text="NavyGo",font=("Ubuntu",45))
titulo.pack()


img_logo=Image.open("Images/ico.png")
logo_ctk=ctk.CTkImage(dark_image=img_logo,size=(45,45))
ventana.logo=logo_ctk
logo=ctk.CTkLabel(ventana,image=ventana.logo,text="")
logo.place(x=389,y=4)






dist=ctk.CTkLabel(ventana,text="Búsqueda (distrito):",font=("Ubuntu",21))
dist.place(x=60,y=81)
dist_text=ctk.CTkEntry(ventana,font=("Arial",20),width=230)
dist_text.place(x=259,y=81)


img_login=Image.open("Images/Login.png")
login_ctk=ctk.CTkImage(dark_image=img_login,size=(40,40))
login=ctk.CTkButton(ventana,text="",image=login_ctk,fg_color="#242424",hover_color="#a5a4a4",width=45)
login.place(x=555,y=22)




img_limp=Image.open("Images/tash.png")
limp_ctk=ctk.CTkImage(dark_image=img_limp,size=(28,28))
limp=ctk.CTkButton(ventana,text="",image=limp_ctk,width=45,fg_color="#242424",hover_color="#a5a4a4",command=limpiar)
limp.place(x=500,y=80)




prov=ctk.CTkLabel(ventana,text="Provincia:",font=("Ubuntu",21))
prov.place(x=153,y=137)
priv=["Lima"]
prov_cmb=ctk.CTkComboBox(ventana,values=priv,font=("Arial",19),width=219,state="readonly")
prov_cmb.place(x=260,y=137)
prov_cmb.set("Selecciona provincia")



time=ctk.CTkLabel(ventana,text="Tiempo:",font=("Ubuntu",21))
time.place(x=170,y=193)

timp=["Mañana","Tarde","Noche"]
time_cmb=ctk.CTkComboBox(ventana,values=timp,font=("Arial",19),width=210,state="readonly")
time_cmb.place(x=260,y=193)
time_cmb.set("Selec.Tiempo")


ubcn=ctk.CTkLabel(ventana,text="Ubicación:",font=("Ubuntu",21))
ubcn.place(x=148,y=249)
ubcn_text=ctk.CTkEntry(ventana,font=("Ubuntu",21),state="readonly",width=230)
ubcn_text.place(x=260,y=249)

filt=["Mall","Restaurante","Parques","Universidades"]
filtro=ctk.CTkComboBox(ventana,values=filt,font=("Arial",19),width=171,state="readonly")
filtro.place(x=407,y=360)
filtro.set("Filtro")



vist_prev=ctk.CTkEntry(ventana,state="readonly",width=525,height=324)
vist_prev.place(x=52,y=420)


img_btn=Image.open("Images/check.png")
btn_check_ctk=ctk.CTkImage(dark_image=img_btn,size=(27,27))
ventana.check=btn_check_ctk
gen_code=ctk.CTkButton(ventana,image=ventana.check,text="",width=22,fg_color="#242424",hover_color="#a5a4a4",command=devolver)
gen_code.place(x=497,y=249)

img_limp1=Image.open("Images/tash.png")
limp_ctk1=ctk.CTkImage(dark_image=img_limp1,size=(27,27))
limp1=ctk.CTkButton(ventana,text="",image=limp_ctk1,width=45,fg_color="#242424",hover_color="#a5a4a4",command=limpiar1)
limp1.place(x=540,y=248)


ventana.mainloop()
