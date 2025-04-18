# Importation classes pour les controleurs
from naim.ctrl.ctrl_inscrti import Ctrl_Inscri
from naim.ctrl.ctrl_menu import Ctrl_menu

# Importation classes pour la base de données
from naim.dao.db import Data_Base

#-----------------------------------------MAIN----------------------------------------------------------#
"""
ctrl_inscri.clear_factory()
"""
db = Data_Base()
db.connect()
ctrl_menu = Ctrl_menu()
if(ctrl_menu.change_page):
    ctrl_inscri = Ctrl_Inscri()

