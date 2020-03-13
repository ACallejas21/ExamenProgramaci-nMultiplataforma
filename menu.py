# -*- coding: utf8 -*-
# Programa: Examen II Parcial // clase Manu
# Autor: Akdiel Callejas Amador
# Fecha 13/03/20

from estacionamiento import Estacionamiento

class Menu:
    """ Representa el menu principal con que el interactua el usuario. """
    
    def __init__(self):
        """ iniciliza una clase de tipo estcionamiento. """
        self.estacionamiento = Estacionamiento()
        