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
        """Muestra el mapa general con todos los distritos y lugares"""
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
        """Actualiza el widget del mapa con nuevos datos"""
        if not self.mapa_widget:
            self.crear_mapa_widget()
        else:
            self.mostrar_mapa_general()
    
    def limpiar_mapa(self):
        """Limpia el mapa actual"""
        if self.mapa_widget:
            self.mapa_widget.destroy()
            self.mapa_widget = None
            self.marcadores = []
    
    def cerrar(self):
        """Cierra las conexiones y limpia recursos"""
        pass