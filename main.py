#Importation de toutes les classes du dossier entite
from naim.entite.user import User
from naim.entite.client import Client
from naim.entite.quote import Quote
from naim.entite.receipt import Receipt

#Importation de toutes les classes du dossier factories
from naim.factories.factory_user import Factory_user

#Importation de toutes les classes du dossier interface
from naim.interface.inscription import Affiche_Inscription

#Importation de toutes les classes du dossier controle
from naim.ctrl.ctrl_inscrti import Ctrl_Inscri

ctrl_inscri = Ctrl_Inscri()
ctrl_inscri.vider_factory()


