from tkinter import messagebox
from src.interface.i18n import tr

class Ex_devis:

    @staticmethod
    def check_date():
        messagebox.showerror(tr("Titre_champ_manquant"), tr("Msg_date_vide"))

    @staticmethod
    def date_limite():
        messagebox.showerror(tr("Titre_erreur_date"), tr("Msg_date_limite"))

    @staticmethod
    def check_order():
        messagebox.showerror(tr("Titre_champ_manquant"), tr("Msg_article_vide"))

    @staticmethod
    def check_order_quantities():
        messagebox.showerror(tr("Titre_champ_manquant"), tr("Msg_qte_vide"))

    @staticmethod
    def check_price():
        messagebox.showerror(tr("Titre_champ_manquant"), tr("Msg_prix_vide"))

    @staticmethod
    def check_all():
        messagebox.showerror(tr("Titre_erreur"), tr("Msg_articles_incomplets"))

    @staticmethod
    def format_date():
        messagebox.showerror(tr("Titre_format_date"), tr("Msg_format_date"))

    @staticmethod
    def format_quantities():
        messagebox.showerror(tr("Titre_quantite_invalide"), tr("Msg_qte_invalide"))

    @staticmethod
    def format_price():
        messagebox.showerror(tr("Titre_prix_invalide"), tr("Msg_prix_invalide"))

    @staticmethod
    def remove_quote(id_devis):
        messagebox.showinfo(tr("Titre_suppression_devis"), tr("Msg_suppression_devis").format(id=id_devis))

    @staticmethod
    def search_error():
        messagebox.showerror(tr("Titre_recherche_devis"), tr("Msg_recherche_devis"))

    @staticmethod
    def quote_succes():
        messagebox.showinfo(tr("Titre_reussite"), tr("Msg_creation_devis"))
