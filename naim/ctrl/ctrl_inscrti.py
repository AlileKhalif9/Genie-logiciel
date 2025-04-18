from naim.interface.inscription import Affiche_Inscription
from naim.factories.factory_user import Factory_user 
from naim.exception.ex_inscri import Ex_inscri
from naim.dao.dao_inscri import Db_Inscri

class Ctrl_Inscri:
    def __init__(self):
        self.factory = Factory_user()
        self.vue = Affiche_Inscription()
        self.vue.bouton_valider.config(command=self.recuperer_donnees)
        self.db = Db_Inscri()
        self.db.init_db()
        self.vue.mainloop()

    def recuperer_donnees(self):
        # Récupérer les valeurs depuis les champs de saisie
        nom = self.vue.entry_nom.get()
        prenom = self.vue.entry_prenom.get()
        nom_utilisateur = self.vue.entry_nom_utilisateur.get()
        email = self.vue.entry_adresse_mail.get()
        adresse_postale = self.vue.entry_adresse_postale.get()
        mot_de_passe = self.vue.entry_mot_de_passe.get()
        telephone = "+33651554791"  # temporaire 

        if(nom == ""):
            Ex_inscri.check_surname()
            return

        if(prenom == ""):
            Ex_inscri.check_name()
            return
        
        if(email == ""):
            Ex_inscri.check_email()
            return
        
        if(adresse_postale == ""):
            Ex_inscri.check_adress()
            return

        if(nom_utilisateur == ""):
            Ex_inscri.check_username()
            return

        # On vérifie si le mot de passe et la confirmation de mot de passe sont les memes
        if(mot_de_passe != self.vue.entry_confirmer_mdp.get()):
            Ex_inscri.check_password()
            return

        # Création d'un utilisateur via Factory
        fac = Factory_user()
        fac.create_user(prenom, nom, nom_utilisateur,
                        telephone, email, adresse_postale, mot_de_passe)
        self.db.add_user(prenom, nom, nom_utilisateur, 
                         telephone, email, adresse_postale, mot_de_passe)

        print("Utilisateur créé avec succès !")
        print("Utilisateur ajouté à la base de données")
        print(fac)

        self.vue.quit()
        return True
    
    # Fonction pour supprimer l'utilisateur
    def vider_factory(self):
        self.factory.clear()
        self.db.clear_all_users()
        print("Tous les utilisateurs ont été supprimés.")

    # Surcharge du print
    def check_user(self, nom_utilisateur, password):
        for user in self.factory.liste_users:
            if user.nom_utilisateur == nom_utilisateur and user.get_password() == password:
                return True
        return False

        
 