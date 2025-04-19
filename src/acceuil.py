from tkinter import *
from datetime import datetime
from PIL import Image, ImageTk
import os

class Tableau_Acceuil(Tk):
    def __init__(self):
        super().__init__()
        self.title("Accueil post connexion")
        self.geometry("1280x800")
        self.resizable(False, False)
        self.config(background="#2A2F4F")

        self.nom_utilisateur = "User"
        self.page_actuelle = None

        self.devis_donnees = [
            ["ID", "Client", "Total", "Date", "Validé ?"],
            [" ", " ", " ", " ", " "],
            [1, "Client n°1 ", "3.5 €", "10/04/2025", "✅"],
            [2, "sinj", "2200 €", "11/04/2025", "❌"]
        ]

        # Page d'acceuil -> canvas + frame scrollable
        self.canvas = Canvas(self, width=1280, height=800, bg="#7894a4")
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.frame_contenu = Frame(self.canvas, bg="#7894a4", width=1280, height=800)
        self.canvas.create_window((0, 0), window=self.frame_contenu, anchor="nw")
        self.frame_contenu.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Molette
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.canvas.bind_all("<Button-4>", self._on_mousewheel_linux)
        self.canvas.bind_all("<Button-5>", self._on_mousewheel_linux)
        
        
        self.devis()

#Le problème avec les switch c'est que je risque de superposer plusieurs frame par dessus donc là je supprime et en affiche une etc.. 
#https://stackoverflow.com/questions/15781802/python-tkinter-clearing-a-frame
    def clear_contenu(self):
        for widget in self.frame_contenu.winfo_children():
            widget.destroy()

    def afficher_menu_onglets(self):
        onglets_y = 165

        couleur_active = "#158aff"
        couleur_inactive = "#dddddd"
        texte_blanc = "white"
        texte_noir = "black"

        onglets = [
            ("Mes Devis", self.devis, "devis", 140),
            ("Mes Factures", self.factures, "factures", 320),
            ("Mes Clients", self.clients, "clients", 500),
            ("Mes Infos", self.infos, "infos", 680)
        ]

        for texte, fonction, page, x in onglets:
            actif = (self.page_actuelle == page)
            bouton = Button(
                self.frame_contenu,
                text=texte,
                command=fonction,
                bg=couleur_active if actif else couleur_inactive,
                fg=texte_blanc if actif else texte_noir,
                font=("Arial", 12, "bold"),
                width=15,
                relief=FLAT
            )
            bouton.place(x=x, y=onglets_y)

        Label(self.frame_contenu, text=f"Bienvenue {self.nom_utilisateur}",
              font=("Arial", 16, "bold"), bg="#dddddd", fg="#2A2F4F").place(x=50, y=30)

    def afficher_page_devis(self):
        self.clear_contenu()
        self.page_actuelle = "devis"
        self.afficher_menu_onglets()

        filtres = Frame(self.frame_contenu, bg="#dddddd", bd=2, relief=RIDGE, width=1000, height=80)
        filtres.place(x=140, y=200)
        filtres.pack_propagate(False)

        Button(filtres, text="Filtrer", command=self.filtrer).pack(side=LEFT, padx=10)
        Button(filtres, text="Chercher", command=self.chercher).pack(side=LEFT, padx=10)
        Button(filtres, text="Nouveau", command=self.ajouter_devis).pack(side=LEFT, padx=10)

        table = Frame(self.frame_contenu, bg="#eeeeee", bd=1, relief=SOLID)
        table.place(x=140, y=270, width=1000, height=500)

        #Exemple pour voir si ça marche (https://stacklima.com/creer-une-table-a-laide-de-tkinter/) pour le moment j'ai juste repris ce code 
        #Pour faire un switch de frames, code basé sur -> https://www.youtube.com/watch?v=95tJO7XJlko 

        #for i in range(len(self.devis_donnees)):
        #    for j in range(len(self.devis_donnees[0])):
        #        cell = Entry(table, width=18, fg='black', font=('Arial', 12))
        #       cell.grid(row=i, column=j)
        #        cell.insert(END, self.devis_donnees[i][j])

        for i in range(len(self.devis_donnees)):
            for j in range(len(self.devis_donnees[0])):
                cell = Entry(table, width=18, fg='black', font=('Arial', 12))
                cell.grid(row=i, column=j)
                cell.insert(END, self.devis_donnees[i][j])

            if i > 1:
                id_devis = self.devis_donnees[i][0]
                bouton = Button(table, text="Afficher", command=lambda id=id_devis: self.afficher_image_devis(id))
                bouton.grid(row=i, column=len(self.devis_donnees[0])) 

    def afficher_page_factures(self):
        self.clear_contenu()
        self.page_actuelle = "factures"
        self.afficher_menu_onglets()

    def afficher_page_clients(self):
        self.clear_contenu()
        self.page_actuelle = "clients"
        self.afficher_menu_onglets()

    def afficher_page_infos(self):
        self.clear_contenu()
        self.page_actuelle = "infos"
        self.afficher_menu_onglets()

    def devis(self):
        if self.page_actuelle != "devis":
            self.afficher_page_devis()

    def factures(self):
        if self.page_actuelle != "factures":
            self.afficher_page_factures()

    def clients(self):
        if self.page_actuelle != "clients":
            self.afficher_page_clients()

    def infos(self):
        if self.page_actuelle != "infos":
            self.afficher_page_infos()

    def mettre_a_jour_tableau(self):
        pass

    def ajouter_devis(self):
        pass

    def supprimer_devis(self, index):
        if 0 <= index < len(self.devis_donnees):
            self.devis_donnees.pop(index)
            self.mettre_a_jour_tableau()

    def filtrer(self):
        pass

    def chercher(self):
        pass

    def afficher_image_devis(self, id_devis):
        chemin = f"C:/Users/S/Documents/Prog/L3/S2/Projet_Genie_Logiciel/res/Devis_{id_devis}.png"

        if not os.path.exists(chemin):
            print(f"Devis {id_devis} introuvable")
            return

        popup = Toplevel(self)
        popup.title(f" Devis {id_devis}")
        popup.geometry("600x450")
        popup.configure(bg="#2A2F4F")

        image = Image.open(chemin)
        image = image.resize((580, 400), Image.ANTIALIAS)
        self.image_tk = ImageTk.PhotoImage(image)  

        Label(popup, image=self.image_tk, bg="#2A2F4F").pack(pady=20)


    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(event.delta / 120), "units")

    def _on_mousewheel_linux(self, event):
        if event.num == 4:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            self.canvas.yview_scroll(1, "units")

if __name__ == "__main__":
    app = Tableau_Acceuil()
    app.mainloop()