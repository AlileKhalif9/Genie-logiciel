from tkinter import messagebox
from src.interface.i18n import tr

class Ex_inscri:

    @staticmethod
    def check_surname():
        messagebox.showerror(tr("Titre_erreur"), tr("Msg_nom_vide"))

    @staticmethod
    def check_name():
        messagebox.showerror(tr("Titre_erreur"), tr("Msg_prenom_vide"))

    @staticmethod
    def check_email():
        messagebox.showerror(tr("Titre_erreur"), tr("Msg_email_vide"))

    @staticmethod
    def check_adress():
        messagebox.showerror(tr("Titre_erreur"), tr("Msg_adresse_vide"))

    @staticmethod
    def check_company():
        messagebox.showerror(tr("Titre_erreur"), tr("Msg_entreprise_vide"))

    @staticmethod
    def check_phone():
        messagebox.showerror(tr("Titre_erreur"), tr("Msg_telephone_vide"))

    @staticmethod
    def check_username():
        messagebox.showerror(tr("Titre_erreur"), tr("Msg_username_vide"))

    @staticmethod
    def check_password():
        messagebox.showerror(tr("Titre_erreur"), tr("Msg_mdp_vide"))

    @staticmethod
    def confirm_password():
        messagebox.showerror(tr("Titre_erreur"), tr("Msg_mdp_non_confirme"))

    @staticmethod
    def format_surname():
        messagebox.showerror(tr("Titre_format_nom"), tr("Msg_format_nom"))

    @staticmethod
    def format_name():
        messagebox.showerror(tr("Titre_format_prenom"), tr("Msg_format_prenom"))

    @staticmethod
    def format_phone():
        messagebox.showerror(tr("Titre_format_tel"), tr("Msg_format_tel"))

    @staticmethod
    def format_email():
        messagebox.showerror(tr("Titre_format_email"), tr("Msg_format_email"))

    @staticmethod
    def format_password():
        messagebox.showerror(tr("Titre_format_mdp"), tr("Msg_format_mdp"))

    @staticmethod
    def already_username():
        messagebox.showerror(tr("Titre_erreur"), tr("Msg_username_pris"))

    @staticmethod
    def already_email():
        messagebox.showerror(tr("Titre_erreur"), tr("Msg_email_pris"))

    @staticmethod
    def already_password():
        messagebox.showerror(tr("Titre_erreur"), tr("Msg_mdp_pris"))

    @staticmethod
    def msg_valid():
        messagebox.showinfo(tr("Titre_succes"), tr("Msg_compte_cree"))
