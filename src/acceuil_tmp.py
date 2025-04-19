from tkinter import *
from datetime import datetime

class TableauDevis(Frame):
    def __init__(self, parent):
        super().__init__()
        self.title("Projet Génie Logiciel")
        self.geometry("1280x800")
        self.resizable(False, False)
        self.config(background="#2A2F4F")
        self.utilisateur_connecte = None

        
        self.devis_donnees = [
        ]

        # Canvas pour scroll
        self.canvas = Canvas(self, bg="#dddddd", highlightthickness=0)
        self.scroll_y = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scroll_y.set)

        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        # Frame qui contient les lignes de données
        self.table_frame = Frame(self.canvas, bg="#dddddd")
        self.canvas.create_window((0, 0), window=self.table_frame, anchor='nw')
        self.table_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Boutons haut
        self.boutons_frame = Frame(self, bg="#dddddd")
        self.boutons_frame.pack(side=TOP, fill=X)
        Button(self.boutons_frame, text="Filtrer", command=self.filtrer).pack(side=LEFT, padx=5, pady=5)
        Button(self.boutons_frame, text="Chercher", command=self.chercher).pack(side=LEFT, padx=5, pady=5)
        Button(self.boutons_frame, text="Nouveau", command=self.ajouter_devis).pack(side=LEFT, padx=5, pady=5)

        self.mettre_a_jour_tableau()

    def mettre_a_jour_tableau(self):
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        headers = ["ID", "Client", "Total", "Date", "Validé ?", "Actions"]
        for col, text in enumerate(headers):
            Label(self.table_frame, text=text, font=("Arial", 10, "bold"), bg="#cccccc").grid(row=0, column=col, padx=5, pady=5, sticky="w")

        for i, devis in enumerate(self.devis_donnees, start=1):
            id_dev, nom_client, total, date, valide = devis
            Label(self.table_frame, text=id_dev, bg="white").grid(row=i, column=0, padx=5, pady=2, sticky="w")
            Label(self.table_frame, text=nom_client, bg="white").grid(row=i, column=1, padx=5, pady=2, sticky="w")
            Label(self.table_frame, text=total, bg="white").grid(row=i, column=2, padx=5, pady=2, sticky="w")
            Label(self.table_frame, text=date, bg="white").grid(row=i, column=3, padx=5, pady=2, sticky="w")
            Label(self.table_frame, text="✔" if valide else "✘", fg="green" if valide else "red", bg="white").grid(row=i, column=4, padx=5, pady=2, sticky="w")
            Button(self.table_frame, text="Supprimer", command=lambda idx=i-1: self.supprimer_devis(idx)).grid(row=i, column=5, padx=5, pady=2)

    def ajouter_devis(self):
        nouvel_id = self.devis_donnees[-1][0] + 1 if self.devis_donnees else 1
        date = datetime.now().strftime("%d/%m/%Y")
        self.devis_donnees.append([nouvel_id, f"Client {nouvel_id}", "0 €", date, False])
        self.mettre_a_jour_tableau()

    def supprimer_devis(self, index):
        if 0 <= index < len(self.devis_donnees):
            self.devis_donnees.pop(index)
            self.mettre_a_jour_tableau()

    def filtrer(self):
        print("Filtrage non implémenté")

    def chercher(self):
        print("Recherche non implémentée")


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x600")
    root.title("Gestion des devis")
    TableauDevis(root).pack(fill=BOTH, expand=True)
    root.mainloop()



"""
import tkinter as tk

# Données simulées de devis (liste de listes : [ID, Nom client, Total, Date, Valide?])
# Ici, Valide? est un booléen (True pour validé, False pour non validé).
devis_donnees = [
    [123, "Client A", "90 €", "07/03/2025", True],
    [124, "Client B", "150 €", "08/03/2025", False],
    [125, "Client C", "130 €", "09/03/2025", True],
]

# Fonction pour (re)dessiner le tableau de devis dans l'interface
def mettre_a_jour_tableau():
    # On supprime toutes les lignes existantes dans la frame des données (y compris l'entête)
    for widget in data_frame.winfo_children():
        widget.destroy()
    # Création de l'entête du tableau
    lbl = tk.Label(data_frame, text="ID Devis", width=10, bg="#dddddd", font=('TkDefaultFont', 10, 'bold'))
    lbl.grid(row=0, column=0, padx=5, pady=2, sticky="w")
    lbl = tk.Label(data_frame, text="Nom client", width=15, bg="#dddddd", font=('TkDefaultFont', 10, 'bold'))
    lbl.grid(row=0, column=1, padx=5, pady=2, sticky="w")
    lbl = tk.Label(data_frame, text="Total", width=8, bg="#dddddd", font=('TkDefaultFont', 10, 'bold'))
    lbl.grid(row=0, column=2, padx=5, pady=2, sticky="w")
    lbl = tk.Label(data_frame, text="Date", width=12, bg="#dddddd", font=('TkDefaultFont', 10, 'bold'))
    lbl.grid(row=0, column=3, padx=5, pady=2, sticky="w")
    lbl = tk.Label(data_frame, text="Validé ?", width=8, bg="#dddddd", font=('TkDefaultFont', 10, 'bold'))
    lbl.grid(row=0, column=4, padx=5, pady=2, sticky="w")
    # On ajoute une colonne supplémentaire pour l'espace des boutons d'action (supprimer)
    # (pas de texte pour l'en-tête de cette colonne)
    tk.Label(data_frame, text="", bg="#dddddd").grid(row=0, column=5, padx=5)
    
    # Remplissage des lignes de données
    for i, devis in enumerate(devis_donnees, start=1):
        id_dev, nom_client, total, date, valide = devis
        # Frame pour la ligne (pour appliquer un style de fond spécifique)
        ligne_frame = tk.Frame(data_frame, bg="white", highlightbackground="green", highlightthickness=1)
        ligne_frame.grid(row=i, column=0, columnspan=6, padx=2, pady=2, sticky="nsew")
        # Création des labels pour chaque colonne de la ligne, ajoutés dans ligne_frame
        tk.Label(ligne_frame, text=str(id_dev), bg="white").pack(side="left", padx=5, pady=2)
        tk.Label(ligne_frame, text=str(nom_client), bg="white").pack(side="left", padx=5, pady=2)
        tk.Label(ligne_frame, text=str(total), bg="white").pack(side="left", padx=5, pady=2)
        tk.Label(ligne_frame, text=str(date), bg="white").pack(side="left", padx=5, pady=2)
        # Affichage de l'état "Validé ?" avec une coche verte ou une croix rouge
        if valide:
            etat_txt = "\u2713"  # symbole check mark
            couleur = "green"
        else:
            etat_txt = "\u2717"  # symbole X
            couleur = "red"
        tk.Label(ligne_frame, text=etat_txt, fg=couleur, bg="white", font=('TkDefaultFont', 10, 'bold')).pack(side="left", padx=5, pady=2)
        # Bouton Supprimer à la fin de la ligne
        btn_supprimer = tk.Button(ligne_frame, text="Supprimer", bg="#f0f0f0", command=lambda index=i-1: supprimer_devis(index))
        btn_supprimer.pack(side="right", padx=5, pady=2)
        # (Optionnel) On pourrait ajouter un bouton "Modifier" ici de manière similaire

    # Ajuster la zone de scroll après mise à jour
    data_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

# Fonction appelée par le bouton "Nouveau" pour ajouter un devis factice
def ajouter_devis():
    # Ajout d'une ligne factice :
    # On crée un nouvel ID en ajoutant 1 au dernier ID existant (ou 1 si la liste est vide)
    nouvel_id = devis_donnees[-1][0] + 1 if devis_donnees else 1
    # Données fictives pour le nouveau devis
    nom = f"Client {nouvel_id}"
    total = "0 €"  # total par défaut
    # Date du jour au format jj/mm/aaaa
    from datetime import datetime
    date = datetime.now().strftime("%d/%m/%Y")
    valide = False  # par défaut non validé
    # Ajout dans la liste de données
    devis_donnees.append([nouvel_id, nom, total, date, valide])
    # Rafraîchir l'affichage du tableau
    mettre_a_jour_tableau()

# Fonction appelée par les boutons "Supprimer" sur chaque ligne
def supprimer_devis(index):
    # Retirer le devis de la liste de données
    if 0 <= index < len(devis_donnees):
        devis_donnees.pop(index)
        # Rafraîchir l'affichage du tableau
        mettre_a_jour_tableau()

# Création de la fenêtre principale
root = tk.Tk()
root.title("Gestion des devis")
root.geometry("600x400")

# Frame du haut contenant les boutons Filtrer, Chercher, Nouveau
top_frame = tk.Frame(root)
top_frame.pack(fill="x", padx=5, pady=5)
tk.Button(top_frame, text="Filtrer").pack(side="left", padx=5)
tk.Button(top_frame, text="Chercher").pack(side="left", padx=5)
tk.Button(top_frame, text="Nouveau", command=ajouter_devis).pack(side="left", padx=5)

# Canvas et Scrollbar pour la zone de tableau des devis
canvas = tk.Canvas(root, bg="#dddddd")
canvas.pack(side="left", fill="both", expand=True, padx=5, pady=5)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

# Frame qui contiendra les données du tableau, placée à l'intérieur du Canvas
data_frame = tk.Frame(canvas, bg="#dddddd")
canvas.create_window((0, 0), window=data_frame, anchor="nw")

# Mise à jour de la région de scroll quand la taille du contenu change
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
data_frame.bind("<Configure>", on_frame_configure)

# Initialiser l'affichage du tableau avec les données existantes
mettre_a_jour_tableau()

# Lancement de la boucle principale Tkinter
root.mainloop()
"""