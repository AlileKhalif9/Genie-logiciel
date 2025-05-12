from tkinter import messagebox
from src.interface.i18n import tr, get_langue

# Classe qui affiche des messages concernant les clients
class Ex_client:
    """
    Méthode de classe qui affiche un message si un des champs ou on entre les infos. personnels 
    d'un client ne sont pas remplis pendant la création d'un devis
    """
    @staticmethod
    def check_surname():
        messagebox.showerror(tr("Titre_champ_manquant"), tr("Msg_nom_client_vide"))

    @staticmethod
    def check_name():
        messagebox.showerror(tr("Titre_champ_manquant"), tr("Msg_prenom_client_vide"))

    @staticmethod
    def check_phone():
        messagebox.showerror(tr("Titre_champ_manquant"), tr("Msg_telephone_client_vide"))

    @staticmethod
    def check_email():
        messagebox.showerror(tr("Titre_champ_manquant"), tr("Msg_email_client_vide"))

    @staticmethod
    def check_address():
        messagebox.showerror(tr("Titre_champ_manquant"), tr("Msg_adresse_client_vide"))

    """
    Méthode de classe qui affiche un message pour indiquer que le format des champs
    pour entrer les informations personnelles du clients sont incorrect
    """
    @staticmethod
    def format_name():
        messagebox.showerror(tr("Titre_format_prenom"), tr("Msg_format_prenom"))
    @staticmethod
    def format_surname():
        messagebox.showerror(tr("Titre_format_nom"), tr("Msg_format_nom"))    
    @staticmethod
    def format_phone():
        messagebox.showerror(tr("Titre_format_tel"), tr("Msg_format_tel"))
    @staticmethod
    def format_email():
        messagebox.showerror(tr("Titre_format_email"), tr("Msg_format_email"))
    """
    Méthode de classe qui affiche un message si le numéro de téléphone ou bien l'@ mail
    a déjà été utilisé pour un client."""
    @staticmethod
    def already_phone():
        messagebox.showerror(tr("Titre_erreur"), tr("Msg_telephone_existant"))

    @staticmethod
    def already_email():
        messagebox.showerror(tr("Titre_erreur"), tr("Msg_email_existant"))
    """
    Méthode de classe qui affiche un message d'erreur si la recherche de client de donne rien
    """
    @staticmethod
    def search_error():
        messagebox.showerror(tr("Titre_recherche_client"), tr("Msg_recherche_client"))
    """
    Méthode de classe qui affiche un message quand on supprime un client
    de l'onglet Client
    """
    @staticmethod
    def remove_client(id_client):
        messagebox.showinfo(tr("Titre_suppression_client"), tr("Msg_suppression_client").format(id=id_client))
    
    