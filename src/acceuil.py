from tkinter import *
from datetime import datetime

class TableauDevis(Tk):
    def __init__(self):
        super().__init__()
        self.title("Accueil post connexion")
        self.geometry("1280x800")
        self.resizable(False, False)
        self.config(background="#2A2F4F")
        self.utilisateur_connecte = None
        self.nom_utilisateur = "User"
        self.page_actuelle = "devis"
        self.devis_donnees = [
    [1, "Entreprise Dupont", "4500 €", "12/04/2025", True],
    [2, "Société Martin", "3200 €", "08/04/2025", False],
    [3, "Client Test", "1250 €", "10/04/2025", True],
]

        self.afficher_acceuil()

    page_actuelle = "devis"

    def afficher_acceuil(self):
        self.canvas = Canvas(self, width=1280, height=800, bg="#7894a4")
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        self.frame_contenu = Frame(self.canvas, bg="#7894a4", width=1280, height=800) #On tous tes widgets dans frame_contenu et c’est le Canvas qui nous permet de scroller
        self.canvas.create_window((0, 0), window=self.frame_contenu, anchor="nw")
        self.frame_contenu.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        ########### Bienvenue ###########
        self.cadre_bienvenue = Frame(self.frame_contenu, bg="#dddddd", bd=2, relief=RIDGE, width=300, height=50) 
        self.cadre_bienvenue.place(x=50, y=30)
        self.cadre_bienvenue.pack_propagate(False)

        Label(self.cadre_bienvenue, text=f"Bienvenue {self.nom_utilisateur}",
              font=("Arial", 16, "bold"), bg="#dddddd", fg="#2A2F4F").pack(pady=10, padx=20, anchor="w")

        ########### ONGLETS ###########
        self.onglets_frame = Frame(self.frame_contenu, bg="#dddddd", bd=2, relief=RIDGE, width=500, height=40) #config frame 
        self.onglets_frame.place(x=140, y=165) #positionnement frame
        self.onglets_frame.pack_propagate(False)


        Button(self.onglets_frame, text="Mes Devis", command=self.devis).pack(side=LEFT, padx=10)
        Button(self.onglets_frame, text="Mes Factures", command=self.factures).pack(side=LEFT, padx=10)
        Button(self.onglets_frame, text="Mes clients", command=self.client).pack(side=LEFT, padx=10)
        Button(self.onglets_frame, text="Mes infos", command=self.infos).pack(side=LEFT, padx=10)


        ########### Filtres ###########
        self.filtres_frame = Frame(self.frame_contenu, bg="#dddddd", bd=2, relief=RIDGE, width=1000, height=80)
        self.filtres_frame.place(x=140, y=200)
        self.filtres_frame.pack_propagate(False)


        Button(self.filtres_frame, text="Filtrer", command=self.filtrer).pack(side=LEFT, padx=10)
        Button(self.filtres_frame, text="Chercher", command=self.chercher).pack(side=LEFT, padx=10)
        Button(self.filtres_frame, text="Nouveau", command=self.ajouter_devis).pack(side=LEFT, padx=10)


        ########### TABLEAU  ###########
        self.table_frame = Frame(self.frame_contenu, bg="#eeeeee", bd=1, relief=SOLID)
        self.table_frame.place(x=140, y=270, width=1000, height=500)

        #Exemple pour voir si ça marche (https://stacklima.com/creer-une-table-a-laide-de-tkinter/) pour le moment j'ai juste repris ce code 

        devis_donnees = [
            ["ID", "Client", "Total", "Date", "Validé ?"],  
            [" ", " ", " ", " ", " "],

            [1, "Client n°1 ", "3.5 €", "10/04/2025", "✅"],
            [2, "sinj", "2200 €", "11/04/2025", "❌"]
            ] #Le mieux serait de gerer ça avec un fichier json pour que ça reste en mémoire
        
        for i in range(len(devis_donnees)):
            for j in range(len(devis_donnees[0])):
                cell = Entry(self.table_frame, width=18, fg='black', font=('Arial', 12))
                cell.grid(row=i, column=j)
                cell.insert(END, devis_donnees[i][j])


        self.mettre_a_jour_tableau()

        # Molette
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.canvas.bind_all("<Button-4>", self._on_mousewheel_linux)
        self.canvas.bind_all("<Button-5>", self._on_mousewheel_linux)

    def mettre_a_jour_tableau(self):
        pass 

    def ajouter_devis(self):
        pass #append devis 
        
    def supprimer_devis(self, index):
        if 0 <= index < len(self.devis_donnees):
            self.devis_donnees.pop(index)
            self.mettre_a_jour_tableau()


    def devis(self):
        if self.page_actuelle != "devis":
            #changement de page 
            print("change page")
            self.page_actuelle = "devis"
            print(f"On est dans {self.page_actuelle}")
        else :
            #ne fais rien 
            print("change rien")

    def factures(self):
        if self.page_actuelle != "factures":
            #changement de page 
            print("change page")
            self.page_actuelle = "factures"
            print(f"On est dans {self.page_actuelle}")
        else :
            #ne fais rien 
            print("change rien")

    def clients(self):
        if self.page_actuelle != "clients":
            #changement de page 
            print("change page")
            self.page_actuelle = "clients"
            print(f"On est dans {self.page_actuelle}")
        else :
            #ne fais rien 
            print("change rien")

    def infos(self):
        if self.page_actuelle != "infos":
            #changement de page 
            print("change page")
            self.page_actuelle = "infos"
            print(f"On est dans {self.page_actuelle}")
        else :
            #ne fais rien 
            print("change rien")

    def filtrer(self):
        pass

    def chercher(self):
        pass

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(event.delta / 120), "units")

    def _on_mousewheel_linux(self, event):
        if event.num == 4:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            self.canvas.yview_scroll(1, "units")

if __name__ == "__main__":
    app = TableauDevis()
    app.mainloop()
