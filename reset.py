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

    inscri = Db_Inscri()
    inscri.clear()
    devis = Db_Devis()
    devis.clear()
    client = Db_Client()
    client.clear()
    facture = Db_Facture()
    facture.clear()




if __name__ == "__main__":
    main()