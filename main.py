# Importation classes pour les controleurs
from src.ctrl.ctrl_inscri import Ctrl_Inscri
from src.ctrl.ctrl_menu import Ctrl_menu
from src.ctrl.ctrl_accueil import Ctrl_accueil

# Importation classes pour la base de données
from src.dao.db import Data_Base
from src.dao.dao_inscri import Db_Inscri
from src.dao.dao_devis import Db_Devis
from src.dao.dao_client import Db_Client
from src.dao.dao_facture import Db_Facture
from src.interface.i18n import tr, get_langue

#-----------------------------------------MAIN----------------------------------------------------------#


def main():
    db = Data_Base()
    db.connect()


    while True:
        ctrl_menu = Ctrl_menu()
        
        if ctrl_menu.change_page:
            ctrl_inscri = Ctrl_Inscri()
        elif get_langue() != "FR":  # Si la langue a changé, relancer le menu
            continue
        else:
            ctrl_accueil = Ctrl_accueil(ctrl_menu.username)
            break





if __name__ == "__main__":
    main()

