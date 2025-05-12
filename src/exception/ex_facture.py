from tkinter import messagebox
from src.interface.i18n import tr

# Classe qui affiche des messages concernant des factures
class Ex_facture:
    """
    Méthode de classe qui permet d'afficher un message pour informer que l'on a supprimer une facture
    quand on clique sur le bouton Supprimer dans l'onglet Facture.
    """
    @staticmethod
    def remove_receipt(id_facture):
        messagebox.showinfo(tr("Titre_suppression_facture"), tr("Msg_suppression_facture").format(id=id_facture))


    """
    Méthode de classe pour afficher un message quand une facture a été crée
    quand l'utilisateur clique sur le bouton Valider d'un devis
    """
    @staticmethod
    def validate_receipt():
        messagebox.showinfo(tr("Titre_creation_facture"), tr("Msg_creation_facture"))

    
    """
    Méthode de classe pour afficher un message quand la recherche de facture donne rien
    """
    @staticmethod
    def search_error():
        messagebox.showerror(tr("Titre_recherche_facture"), tr("Msg_recherche_facture"))

