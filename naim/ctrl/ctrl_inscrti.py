from naim.interface.inscription import Affiche_Inscription
from naim.factories.factory_user import Factory_user  # à adapter selon ton projet

class Ctrl_Inscri:
    def __init__(self):
        self.factory = Factory_user()
        self.vue = Affiche_Inscription()
        self.vue.bouton_valider.config(command=self.recuperer_donnees)
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

        # Création d'un utilisateur via Factory
        fac = Factory_user()
        fac.create_user(prenom, nom, nom_utilisateur,
                        telephone, email, adresse_postale, mot_de_passe)

        print("Utilisateur créé avec succès !")
        print(fac)

        self.vue.quit()
        return fac
    
    def vider_factory(self):
        self.factory.clear_all()
        print("Tous les utilisateurs ont été supprimés.")
 