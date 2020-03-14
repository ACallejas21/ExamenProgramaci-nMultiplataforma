# -*- coding: utf8 -*-
# Programa: Examen II Parcial // clase Manu
# Autor: Akdiel Callejas Amador
# Fecha 13/03/20
# enlace repositorio: https://github.com/LMV-CORP-504/ExamenProgramaci-nMultiplataforma.git

import sys
from estacionamiento import Estacionamiento

class Menu:
    """ Representa el menu principal con que el interactua el usuario. """
    
    def __init__(self):
        """ iniciliza una clase de tipo estcionamiento y vrea el diccionario. """
        self.estacionamiento = Estacionamiento()
        self.opciones = {"1": self.agregar_vehivulo,
                         "2": self.salida_vehiculo,
                         "3": self.reporte,
                         "4": self.buscar,
                         "5": self.buscarTodos,
                         "6": self.cerrar
                        }

    
    def desplegar_menu(self):
        """ despliega el Menu principal """
        print("""
              ------- Menú ------
              1. ingreso de vehículo
              2. Salida de vehículo
              3. Reporte diario
              4. Buscar Cehículo
              5: Mostar todos Los vehiculos
              6. Salir
        """)
    
    def run(self):
        """ se encarga de mantener el programa corriendo hasta que se diga lo contrario. """
        while True:
            self.desplegar_menu()
            elecion = input("ingrese una opción: ")
            opcion = self.opciones.get(elecion)

            if opcion:
                opcion()
            else:
                print("La elección no es valída")


    def agregar_vehivulo(self):
        """ ingresa un vehículo. """
        self.estacionamiento.ingreso_vehiculo()
    
    def salida_vehiculo(self):
        """ se encarga de la salida del vehiculo y calcula el ticket. """
        self.estacionamiento.salida_vehiculo()
    
    def reporte(self):
        """ crea el reporte diario """
        pass

    def buscar(self):
        """ busca unn vehículo """
        placa = input("Ingrese la placa del vehiculo")
        vehiculo = self.estacionamiento.buscar_vehículo(placa)

        if vehiculo:
            print("Placa: {0}\nMarca:{1}Tipo:{2}\nModelo{3}\nHora ingreso: {4}"
                 .format(vehiculo.placa_vehiculo, vehiculo.marca_vehiculo, vehiculo.tipo_vehiculo, 
                         vehiculo.modelo_vehiculo, vehiculo.hora_ingreso_vehiculo))
        else:
            print("El vehículo no existe.")
    
    def buscarTodos(self):
        """ Muestra todos los vehiculos en el estacionamiento """
        for vehiculo in self.estacionamiento.lista_estacionamiento:
            print("Placa: {0}\nMarca:{1}Tipo:{2}\nModelo{3}\nHora ingreso:{4\nestado: {5}"
                  .format(vehiculo.placa_vehiculo, vehiculo.marca_vehiculo, vehiculo.tipo_vehiculo, 
                          vehiculo.modelo_vehiculo, vehiculo.hora_ingreso_vehiculo,vehiculo.estado_vehiculo))
        
    def cerrar(self):
        """ Cierra el programa """
        sys.exit(0)
    
    def reporte(self):
        """ Crea el reporte del sistema. """
        print("Ganacias totales: ")

if __name__ == "__main__":
    menu = Menu()
    menu.run()