from naim.interface.menu import Affiche_Acceuil
from naim.interface.accueil import TableauDevis
from naim.ctrl.ctrl_inscrti import Ctrl_Inscri
from naim.dao.dao_connexion import Db_Connexion
from naim.exception.ex_connexion import Ex_conn

class Ctrl_menu:
    def __init__(self):
        self.vue = Affiche_Acceuil()
        self.vue.inscription.config(command=self.open_inscription)   # Quand on appuie sur le bouton d'inscription, on ouvre la page inscription
        self.vue.bouton_connexion.config(command=self.check_datas)
        self.change_page = False    # Attribut pour changer de page
        self.db = Db_Connexion()
        self.vue.mainloop()

    # Fonction qui renvoie True si le bouton d'inscription est sélectionné
    def open_inscription(self):
        self.change_page = True
        self.vue.destroy()
        self.change_page = False

    def check_datas(self):
        username = self.vue.entry_user.get()
        password = self.vue.entry_pass.get()

        if(self.db.check_connexion(username, password)):
            print("Connexion réussie.")
            TableauDevis()
        else:
            Ex_conn.display()
    