# -*- coding: utf8 -*-
# Programa: Examen II Parcial
# Autor: Akdiel Callejas Amador
# Fecha 13/03/20

import datetime
ultimo_id = 0

class Vehiculo:
    """ se encarga de la cración de un objeto tipo Vehículo """

    def __init__(self, numero_placa, marca="", model="",tipo_vehiculo="" ):
        """ crea un objeto tipo vehiculo en base a los parametros datos. """
        global ultimo_id
        ultimo_id += 1
        self.id_vehiculo = ultimo_id
        self.placa_vehiculo = numero_placa
        self.marca_vehiculo = marca
        self.modelo_vehiculo = model
        if tipo_vehiculo == "automovil" or tipo_vehiculo == "automóvil" or tipo_vehiculo== "motocicleta":
            self.tipo_vehiculo = tipo_vehiculo
        else:
            print("el tipo de vehívulo no es es aceptado o es incorrecto.")
        self.hora_ingreso_vehiculo = datetime.datetime.now()
        self.estado_vehiculo = True