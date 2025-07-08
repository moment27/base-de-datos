#Funciones y otros temas aportados al proyecto
def devolver():
    global ubcn_text
    coordenada_act="-12.045913375221852, -76.95443787206254"
    ubcn_text.configure(state="normal")
    ubcn_text.delete(0,"end")
    ubcn_text.insert(0,coordenada_act)
    ubcn_text.configure(state="readonly")

    try:
        lat,lon=map(float,coordenada_act.split(","))
        mapa_manager.agregar_marcador(lat,lon,"Ubicación Actual")
    except ValueError:
        print("Error: Coordenadas inválidas")    

def limpiar():
    global dist_text
    dist_text.delete(0,"end")
def limpiar1():
    global ubcn_text
    ubcn_text.configure(state="normal")
    ubcn_text.delete(0,"end")
    ubcn_text.configure(state="readonly")

def Limpiar_All():
    limpiar()
    limpiar1()
    global prov_cmb
    global time_cmb

    prov_cmb.set("Selec.Provincia")
    time_cmb.set("Select.Tiempo")

    mapa_manager.limpiar_marcadores()
    if mapa_manager.ruta_dibujada:
        mapa_manager.mapa_widget.delete_all_path()
        mapa_manager.ruta_dibujada=None
    if hasattr(mapa_manager,"etiqueta_distanciada") and mapa_manager.etiqueta_distancia:
        mapa_manager.etiqueta_distancia.destroy()
        mapa_manager.etiqueta_distancia=None    
    

def mostrar_mapa():
    global mapa_manager
    if mapa_manager:
        mapa_manager.mostrar_mapa_general()


#Interfaz gráfica
import customtkinter as ctk
import ctypes
import subprocess
from PIL import Image
from Mapa_Manager import MapaManager
from Admin.Distric_list_Ad_NavyDB import L_Distrito
from Admin.Categoria_list_Ad_NavyDB import L_Categoria
from Admin.Lugar_list_Ad_NavyDB import L_Lugar
from math import radians, sin,cos,sqrt,atan2

def Cerrar_Sesion():
    ventana.destroy()
    subprocess.Popen(["python","Login.py"])

def Validar_Distrito():
    global dist_text
    nom_distric=dist_text.get().strip()

    distric_model=L_Distrito()
    distrito=distric_model.SeleccionarUnDistrito(nom_distric)

    if distrito:
        print("Distrito encontrado")
    else:
        print("Distrito no encontrado")    

def Buscar():
    global dist_text
    nom_dist=dist_text.get().strip()

    if not nom_dist:
        print("Está vacío")
        return
    distric_model=L_Distrito()
    distrito=distric_model.SeleccionarUnDistrito(nom_dist)

    if distrito:
        print("Distrito encontrado",distrito[1])
        lugar_model=L_Lugar()
        lugares=lugar_model.Lugares_por_Distrito(nom_dist)

        if lugares:
            print("Lugares encontrados en el distrito")
            mapa_manager.mostrar_mapa_general()

            try:
                ubic_actual=ubcn_text.get().strip()
                lat_actual,lon_actual=map(float,ubic_actual.split(","))
                mapa_manager.agregar_marcador(lat_actual,lon_actual,"Ubicación Actual")
            except Exception:
                print("Ubicación actual inválida")

            for lugar in lugares:
                nombre_lugar=lugar[1]
                coordenadas=lugar[2]
                try:
                    lat,lon=map(float,coordenadas.split(","))
                    mapa_manager.agregar_marcador(lat, lon, nombre_lugar, lambda l=lat, lo=lon, n=nombre_lugar: marcador_clickeado(l, lo, n))
                except ValueError:
                    print(f"Coordenadas inválidas")    

        else:
            print("No hay")

    else:
        print("Distrito no encontrado")    


def calcular_distancia(lat1,lon1,lat2,lon2):
    r=6371.0
    lat1_rad=radians(lat1)
    lon1_rad=radians(lon1)
    lat2_rad=radians(lat2)
    lon2_rad=radians(lon2)

    dlat=lat2_rad - lat1_rad
    dlon=lon2_rad - lon1_rad

    a=sin(dlat/2)**2+cos(lat1_rad)*cos(lat2_rad)*sin(dlon/2)**2
    c=2*atan2(sqrt(a),sqrt(1-a))

    distancia=r*c
    return distancia

def marcador_clickeado(lat,lon,nombre):
    ubic_actual=ubcn_text.get().strip()
    try:
        lat_actual,lon_actual=map(float,ubic_actual.split(","))

        


        distancia=calcular_distancia(lat_actual,lon_actual,lat,lon)

        mapa_manager.trazar_ruta((lat_actual,lon_actual),(lat,lon),distancia_Km=distancia)

        print(f"Distancia a {nombre}: {distancia:.2f}km")

    except Exception as e:
        print(f"Error al calcular distancia o trazar la línea: {e}")    



categoria_model= L_Categoria()
categ_bd=categoria_model.Lista_Categoria()
lista_categoria=[fila[1] for fila in categ_bd] if categ_bd else[]


#Propiedades de ventana
ventana=ctk.CTk()
ventana.geometry("620x760+740+90")
ventana.title("NavyGo")
ventana.resizable(False,False)
ventana.iconbitmap("Images/ico (1).ico")
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("NaviGo.GRUPO.EDG")

#Labels y otros elementos de nuestro programa

img_crses=Image.open("Images/Cerrar_sesion.png")
crses_ctk=ctk.CTkImage(dark_image=img_crses,size=(40,40))
crses=ctk.CTkButton(ventana,text="Cerrar Sesión",image=crses_ctk,fg_color="#242424",font=("Ubuntu",19),command=Cerrar_Sesion)
crses.place(x=10,y=1)


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
prov_cmb.set("Selec.Provincia")



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


filtro=ctk.CTkComboBox(ventana,values=lista_categoria,font=("Arial",19),width=140,state="readonly")
filtro.place(x=332,y=342)
filtro.set("Filtro")



frame_mapa=ctk.CTkFrame(ventana,width=525,height=324,corner_radius=10)
frame_mapa.place(x=52,y=420)

mapa_manager=MapaManager(frame_mapa)
mapa_manager.crear_mapa_widget()
mapa_manager.mostrar_mapa_general()



img_btn=Image.open("Images/check.png")
btn_check_ctk=ctk.CTkImage(dark_image=img_btn,size=(27,27))
ventana.check=btn_check_ctk
gen_code=ctk.CTkButton(ventana,image=ventana.check,text="",width=22,fg_color="#242424",hover_color="#a5a4a4",command=devolver)
gen_code.place(x=497,y=249)

img_limp1=Image.open("Images/tash.png")
limp_ctk1=ctk.CTkImage(dark_image=img_limp1,size=(27,27))
limp1=ctk.CTkButton(ventana,text="",image=limp_ctk1,width=45,fg_color="#242424",hover_color="#a5a4a4",command=limpiar1)
limp1.place(x=540,y=248)


img_acpt=Image.open("Images/icon_confirma.png")
acpt_ctk=ctk.CTkImage(dark_image=img_acpt,size=(27,27))
acpt=ctk.CTkButton(ventana,text="Buscar",font=("Ubuntu",16),image=acpt_ctk,fg_color="#242424",hover_color="#a5a4a4",command=Buscar)
acpt.place(x=20,y=340)

img_apfl=Image.open("Images/Aplicar_filtro.png")
apfl_ctk=ctk.CTkImage(dark_image=img_apfl,size=(27,27))
apfl=ctk.CTkButton(ventana,text="Aplicar Filtro",font=("Ubuntu",16),image=apfl_ctk,fg_color="#242424",hover_color="#a5a4a4")
apfl.place(x=170,y=340)


img_limp_all=Image.open("Images/tash.png")
limp_all_ctk=ctk.CTkImage(dark_image=img_limp_all,size=(27,27))
limp_all=ctk.CTkButton(ventana,text="Limpiar",font=("Ubuntu",16),image=limp_all_ctk,fg_color="#242424",hover_color="#a5a4a4",command=Limpiar_All)
limp_all.place(x=480,y=340)



ventana.mainloop()
