# Importation classes pour les controleurs
from naim.ctrl.ctrl_inscrti import Ctrl_Inscri
from naim.ctrl.ctrl_menu import Ctrl_menu

# Importation classes pour la base de données
from naim.dao.db import Data_Base

#-----------------------------MAIN--------------------------------------------------------------------
db = Data_Base()
db.connect()

ctrl_inscri = Ctrl_Inscri()
ctrl_inscri.vider_factory()


