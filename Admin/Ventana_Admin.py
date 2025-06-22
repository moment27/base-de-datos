#Metodos y temas empleados en clases
from User_List_Ad_NavyDB import *
from Categoria_list_Ad_NavyDB import *
from Time_List_Ad_NavyDB import *
from Distric_list_Ad_NavyDB import *
from Lugar_list_Ad_NavyDB import *
from Conexion_MySQL import *
import subprocess
import sys
import os 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

def Limpiar_PSW():
    global password_text
    password_text.delete(0,"end")
def Limpiar_USER():
    global user_text
    user_text.delete(0,"end")

def Cargar_Usuario():
    l_user=L_Usuario().Lista_Usuario()
    for lista in l_user:
        tree.insert("","end",values=lista)

def siguiente_pagina(): 
    #global pagina_actual
    #pagina_actual+=1
    #Filtro_TB()
    
    global pagina_actual
    filtro=table_cmb.get() 

    #Se evalua la cantidad de páginas máximas a mostrar
    if filtro=="Lugares":
        total=L_Lugar().Cantidad_Lugar()

    elif filtro=="Distritos":
        total=L_Distrito().Cantidad_Distric()

    elif filtro=="Categoria":
        total=L_Categoria().Cantidad_Categoria()    
    else:
        total=0

    max_page=(total-1)//height            
    if pagina_actual < max_page: 
        pagina_actual+=1
        Filtro_TB()


def anterior_pagina():
    global pagina_actual
    if pagina_actual > 0:
        pagina_actual-=1
    Filtro_TB()  


pagina_actual=0
height=5

def Filtro_TB(value=None):
    global tree,pagina_actual,height

    filtro=table_cmb.get()
    offset=pagina_actual*height

    tree.pack_forget()
    tree.destroy()

    columns=("Id","Nombre")
    widths={}

    if filtro=="Usuarios":
        columns=("Id","Nombre","Password","Categoria")
        height=7

    elif filtro=="Tiempo":
        columns=("Id","Nombre")
        height=3
        widths={"Id":1,"Nombre":1}

    elif filtro=="Categoria":
        columns=("Id","Nombre")
        height=12

    elif filtro=="Lugares":
        columns=("Id","Nombre","Coordenadas","Categoria_id","Distrito_id")
        height=12
        widths={"Id":1,"Nombre":140,"Coordenadas":200,"Categoria_id":1,"Distrito_id":1}


    elif filtro=="Distritos":
        columns=("Id","Nombre") 
        height=9

    tree=ttk.Treeview(ventana_admin,columns=columns,show='headings',height=height)
    tree.pack(padx=20,pady=90,fill="both",expand=False)

    for col in columns:
        ancho=widths.get(col, 100)
        tree.column(col,anchor="center",width=ancho)
        tree.heading(col,text=col)


    #Cargando Datos  
    if filtro=="Usuarios":
        datos=L_Usuario().Lista_Usuario()

    elif filtro=="Categoria":
        datos=L_Categoria().Lista_Categoria_Personalizada(offset,height)

    elif filtro=="Tiempo":
        datos=L_Tiempo().Lista_Tiempo()

    elif filtro=="Distritos":
        datos=L_Distrito().Lista_Distrito_Personalizada(offset,height)

    elif filtro=="Lugares":
        datos=L_Lugar().Lista_Lugar_Personalizada(offset,height)    
    else:
        datos=[] #esto es por si no hay datos

    #Recorre los datos y los inserta en la tabla :D 
    for fila in datos:
        tree.insert("","end",values=fila)                                   
    

def Redigir_Crear():
    global table_cmb
    filtro=table_cmb.get()
    base_dir = os.path.dirname(os.path.abspath(__file__))

    if filtro=="Usuarios":
        ruta=os.path.join(base_dir,"Metodos","Usuario","Create_User_Ad.py")
        ventana_admin.destroy()
        subprocess.Popen(["python",ruta])


    elif filtro=="Categoria":
        ruta=os.path.join(base_dir,"Metodos","Categoria","Create_Categoria_Ad.py")
        ventana_admin.destroy()
        subprocess.Popen(["python",ruta])

    elif filtro=="Distritos":
        ruta=os.path.join(base_dir,"Metodos","Distrito","Create_Distric_Ad.py")
        ventana_admin.destroy()
        subprocess.Popen(["python",ruta])

    else:
        print("No hay tabla seleccionada")


def Redirigir_Editar():
    global table_cmb
    filtro=table_cmb.get()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    if filtro=="Usuarios":
        ruta=os.path.join(base_dir,"Metodos","Usuario","Edit_User_Ad.py")
        ventana_admin.destroy()
        subprocess.Popen(["python",ruta])
    elif filtro=="Categoria":
        ruta=os.path.join(base_dir,"Metodos","Categoria","Edit_Categoria_Ad.py")
        ventana_admin.destroy()
        subprocess.Popen(["python",ruta])
    elif filtro=="Distritos":
        ruta=os.path.join(base_dir,"Metodos","Distrito","Edit_Distric_Ad.py")
        ventana_admin.destroy()
        subprocess.Popen(["python",ruta])        



def Eliminar_Selec():
    sel=tree.selection()
    if not sel:
        print("No hay fila seleccionada")
        return
    item=tree.item(sel)
    id_sel= item['values'][0]
    filtro=table_cmb.get()

    if filtro=="Usuarios":
        L_Usuario().Eliminar_Usuario(id_sel)
    elif filtro=="Categoria":
        L_Categoria().Eliminar_Categoria(id_sel)
    elif filtro=="Distritos":
        L_Distrito().Eliminar_Distric(id_sel)
    else:
        print("No se puede eliminar")          


#Interfaz gráfica
import customtkinter as ctk
from tkinter import ttk
from PIL import Image
#Propiedades de la ventana
ventana_admin=ctk.CTk()
ventana_admin.geometry("920x620+740+90")
ventana_admin.title("Admin🎩")
ventana_admin.iconbitmap("Images/ico (1).ico")
ventana_admin.resizable(False,False)

titulo=ctk.CTkLabel(ventana_admin,text="Admin CRUD",font=("Ubuntu",70))
titulo.pack()

img_logo=Image.open("Images/Login.png")
logo_ctk=ctk.CTkImage(dark_image=img_logo,size=(60,60))
logo=ctk.CTkLabel(ventana_admin,image=logo_ctk,text="")
logo.place(x=670,y=15)


img_edit=Image.open("Images/crear.png")
edit_ctk=ctk.CTkImage(dark_image=img_edit,size=(25,25))
edit=ctk.CTkButton(ventana_admin,text="Crear",image=edit_ctk,fg_color="#242424",font=("Ubuntu",19),command=Redigir_Crear)
edit.place(x=30,y=105)


img_edit=Image.open("Images/edit.png")
edit_ctk=ctk.CTkImage(dark_image=img_edit,size=(25,25))
edit=ctk.CTkButton(ventana_admin,text="Editar",image=edit_ctk,fg_color="#242424",font=("Ubuntu",19),command=Redirigir_Editar)
edit.place(x=170,y=105)

img_edit=Image.open("Images/tash.png")
edit_ctk=ctk.CTkImage(dark_image=img_edit,size=(25,25))
edit=ctk.CTkButton(ventana_admin,text="Eliminar",image=edit_ctk,fg_color="#242424",font=("Ubuntu",19),command=Eliminar_Selec)
edit.place(x=300,y=105)


tablas=["Usuarios","Distritos","Lugares","Tiempo","Categoria"]

table_cmb=ctk.CTkComboBox(ventana_admin,values=tablas,font=("Arial",19),width=219,state="readonly")
table_cmb.place(x=670,y=105)
table_cmb.set("Selecciona la tabla")
table_cmb.configure(command=Filtro_TB)

img_left_next=Image.open("Images/left_next.png")
left_next_ctk=ctk.CTkImage(dark_image=img_left_next,size=(40,40))
left_next=ctk.CTkButton(ventana_admin,text="",image=left_next_ctk,fg_color="#242424",command=anterior_pagina)
left_next.place(x=20,y=550)

img_rigth_next=Image.open("Images/rigth_next.png")
rigth_next_ctk=ctk.CTkImage(dark_image=img_rigth_next,size=(40,40))
rigth_next=ctk.CTkButton(ventana_admin,text="",image=rigth_next_ctk,fg_color="#242424",command=siguiente_pagina)
rigth_next.place(x=140,y=550)


style=ttk.Style()
style.theme_use("clam")

#Estilo para los datos de la tabla
style.configure("Treeview",background="#2b2b2b",foreground="white",rowheight=25,fieldbackground="#2b2b2b")

#Estilo para el encabezados
style.configure("Treeview.Heading",background="#2b2b2b",foreground="white",font=("Arial",12,"bold"))


#Inserto el encabezado/columna
tree=ttk.Treeview(ventana_admin,columns=("Id","Nombre","Password","Categoria"),show='headings',height=5)
tree.pack(padx=20,pady=90,fill="both",expand=False)
tree.column("Id",anchor="center",width=50)
tree.column("Nombre",anchor="center",width=50)
tree.column("Password",anchor="center",width=50)
tree.column("Categoria",anchor="center",width=50)


tree.heading("Id",text="ID")
tree.heading("Nombre",text="Nombre")
tree.heading("Password",text="Password")
tree.heading("Categoria",text="Categoria")

#Por defecto se carga usuarios
Cargar_Usuario()



ventana_admin.mainloop()