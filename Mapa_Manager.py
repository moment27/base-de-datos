import tkintermapview
import customtkinter as ctk
from Admin.Lugar_list_Ad_NavyDB import L_Lugar
from Admin.Distric_list_Ad_NavyDB import L_Distrito
import os
import tempfile
import webbrowser
from PIL import Image, ImageTk
import io

class MapaManager:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.l_lugar=L_Lugar()
        self.l_distrito=L_Distrito()
        self.mapa_widget = None
        self.marcadores = []
        self.centro_mapa = (-12.046374, -77.042793)  # Lima, Perú
        self.ruta_dibujada=None
        self.marcador_distancia=None
        self.texto_distancia=None
        
    def crear_mapa_widget(self):
        """Crea el widget del mapa en el frame padre"""
        if self.mapa_widget:
            self.mapa_widget.destroy()
        
        # Crear el widget del mapa
        self.mapa_widget = tkintermapview.TkinterMapView(
            self.parent_frame, 
            width=525, 
            height=324,
            corner_radius=10
        )
        self.mapa_widget.set_position(*self.centro_mapa)
        self.mapa_widget.set_zoom(12)
        self.mapa_widget.pack(fill="both", expand=True)
        
        return self.mapa_widget
    
    def limpiar_marcadores(self):
        for marker in self.marcadores:
            marker.delete()
        self.marcadores = []
    
    def mostrar_mapa_general(self):
      
        if not self.mapa_widget:
            self.crear_mapa_widget()
        self.limpiar_marcadores()

        distritos=self.l_distrito.Lista_Distrito()
        lugares=self.l_lugar.Lista_Lugar()
        for lugar in lugares:
            if lugar[3]:
                try:
                    lat,lon=map(float,lugar[3].split(','))
                    marker=self.mapa_widget.set_marker(lat,lon,text=lugar[1])
                    self.marcadores.append(marker)
                except Exception as e:
                    print(f"Coordenadas inválidas: {lugar[3]}")    


    def actualizar_mapa_widget(self, filtro=None, distrito=None, tiempo=None, provincia=None):
        
        if not self.mapa_widget:
            self.crear_mapa_widget()
        else:
            self.mostrar_mapa_general()
    
    def agregar_marcador(self,lat,lon,nombre,callback=None):
        if self.mapa_widget:
            marcador=self.mapa_widget.set_marker(lat,lon,text=nombre)
            self.marcadores.append(marcador)
            
            if callback:
                marcador.command=lambda m=marcador: callback(m.position[0],m.position[1],nombre)

    ruta_dibujada=None
    def trazar_ruta(self,origen,destino,distancia_Km=None):
        if self.mapa_widget:
            if self.ruta_dibujada:
                self.mapa_widget.delete_all_path(self.ruta_dibujada)
            self.ruta_dibujada=self.mapa_widget.set_path([origen,destino])  

            #if self.marcador_distancia:
                #self.marcador_distancia.delete()

            if hasattr(self, "texto_distancia") and self.texto_distancia:
                self.etiqueta_distancia.destroy()
                self.etiqueta_distancia=None    

            if distancia_Km is not None:
                texto=f"{distancia_Km:.2f} km"
                self.etiqueta_distancia=ctk.CTkLabel(self.parent_frame,text=texto,font=("Arial",11,"bold"),fg_color="black",corner_radius=5)
                
                self.etiqueta_distancia.place(relx=0.5,rely=0.42,anchor="center")

    def limpiar_mapa(self):
     
        if self.mapa_widget:
            self.mapa_widget.destroy()
            self.mapa_widget = None
            self.marcadores = []
    
    def cerrar(self):
        """Cierra las conexiones y limpia recursos"""
        pass