from naim.interface.menu import Affiche_Acceuil
from naim.ctrl.ctrl_inscrti import Ctrl_Inscri


class Ctrl_menu:
    def __init__(self):
        self.vue = Affiche_Acceuil()
        self.vue