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
        self.nom_utilisateur = " "

        self.devis_donnees = [

        ]

        self.afficher_inscription()

    def afficher_inscription(self):
        self.canvas = Canvas(self, width=1280, height=800, bg="#7894a4", highlightthickness=0)
        self.scroll_y = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scroll_y.set)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        self.frame_contenu = Frame(self.canvas, bg="#7894a4")
        self.canvas.create_window((0, 0), window=self.frame_contenu, anchor="nw")
        self.frame_contenu.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        Label(self.frame_contenu, text=f"Bienvenue {self.nom_utilisateur}",
              font=("Arial", 14), bg="#7894a4", fg="white").pack(pady=10, anchor="w", padx=20)

        self.boutons_frame = Frame(self.frame_contenu, bg="#7894a4")
        self.boutons_frame.pack(pady=10, anchor="w", padx=20)
        Button(self.boutons_frame, text="Filtrer", command=self.filtrer).pack(side=LEFT, padx=5)
        Button(self.boutons_frame, text="Chercher", command=self.chercher).pack(side=LEFT, padx=5)
        Button(self.boutons_frame, text="Nouveau", command=self.ajouter_devis).pack(side=LEFT, padx=5)

        self.table_frame = Frame(self.frame_contenu, bg="#dddddd")
        self.table_frame.pack(padx=20, pady=20, fill=X)

        self.mettre_a_jour_tableau()

        # Molette
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.canvas.bind_all("<Button-4>", self._on_mousewheel_linux)
        self.canvas.bind_all("<Button-5>", self._on_mousewheel_linux)

    def mettre_a_jour_tableau(self):
        pass

    def ajouter_devis(self):
        nouvel_id = self.devis_donnees[-1][0] + 1 if self.devis_donnees else 1
        nom = f"Client {nouvel_id}"
        total = "0 €"
        date = " "
        valide = False
        self.devis_donnees.append([nouvel_id, nom, total, date, valide])
        self.mettre_a_jour_tableau()

    def supprimer_devis(self, index):
        if 0 <= index < len(self.devis_donnees):
            self.devis_donnees.pop(index)
            self.mettre_a_jour_tableau()

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

