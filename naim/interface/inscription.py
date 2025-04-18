from tkinter import *
import os
from . import accueil
from . import inscription

class Affiche_Inscription(Tk):
    def __init__(self):
        super().__init__()
        self.title("Inscription")
        self.geometry("800x600")
        self.resizable(False, False)
        self.config(background="#2A2F4F")
        self.utilisateur_connecte = None

        self.inscri_folder = "C:\\Users\\matig\\Desktop\\L3\\genie logiciel\\programmes\\Genie-logiciel\\naim\\png\\inscri"
        self.button_folder = "C:\\Users\\matig\\Desktop\\L3\\genie logiciel\\programmes\\Genie-logiciel\\naim\\png\\bouton"

        self.images = {
            "i_admail": PhotoImage(file=os.path.join(self.inscri_folder, "adresse_mail.png")),
            "i_adpost": PhotoImage(file=os.path.join(self.inscri_folder, "adresse_postale.png")),
            "i_cmdp": PhotoImage(file=os.path.join(self.inscri_folder, "confirme_mdp.png")),
            "i_entreprise": PhotoImage(file=os.path.join(self.inscri_folder, "entreprise.png")),
            "i_mdp": PhotoImage(file=os.path.join(self.inscri_folder, "mdp.png")),
            "i_nom": PhotoImage(file=os.path.join(self.inscri_folder, "nom.png")),
            "i_uti": PhotoImage(file=os.path.join(self.inscri_folder, "nom_uti.png")),
            "i_piece": PhotoImage(file=os.path.join(self.inscri_folder, "piece_identite.png")),
            "i_prenom": PhotoImage(file=os.path.join(self.inscri_folder, "prenom.png")),
            "i_societe": PhotoImage(file=os.path.join(self.inscri_folder, "societe.png")),
            "i_ok": PhotoImage(file=os.path.join(self.inscri_folder, "ok.png")),
            "fermer": PhotoImage(file=os.path.join(self.button_folder, "close.png")),


        }

        self.afficher_inscription()

    def afficher_inscription(self):
        # Création du canvas
        self.canvas = Canvas(self, width=1280, height=800, bg="#7894a4", highlightthickness=0)
        self.scroll_y = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scroll_y.set)

        self.canvas.pack(fill=BOTH, expand=True)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        # Activation de la molette (scroll)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)  # Windows / Mac
        self.canvas.bind_all("<Button-4>", self._on_mousewheel_linux)  # Linux scroll up
        self.canvas.bind_all("<Button-5>", self._on_mousewheel_linux)  # Linux scroll down

        # Texte
        self.canvas.create_text(640, 50, text="Projet IHM", font=("Arial", 40, "bold"), fill="white", anchor="center")

    # Champs de saisie pour les champs demandés

    
        self.entry_nom = Entry(self, font=("Arial", 14), width=25)
        self.canvas.create_window(320, 115, window=self.entry_nom)

        self.entry_prenom = Entry(self, font=("Arial", 14), width=25)
        self.canvas.create_window(320, 230, window=self.entry_prenom)

        self.entry_adresse_mail = Entry(self, font=("Arial", 14), width=25)
        self.canvas.create_window(320, 345, window=self.entry_adresse_mail)

        self.entry_adresse_postale = Entry(self, font=("Arial", 14), width=25)
        self.canvas.create_window(320, 460, window=self.entry_adresse_postale)

        entry_raison_sociale = Entry(self, font=("Arial", 14), width=25)
        self.canvas.create_window(320, 575, window=entry_raison_sociale)

        entry_scan_piece = Entry(self, font=("Arial", 14), width=25)
        self.canvas.create_window(320, 700, window=entry_scan_piece)

        entry_entreprise = Entry(self, font=("Arial", 14), width=25)
        self.canvas.create_window(320, 815, window=entry_entreprise)

        self.entry_nom_utilisateur = Entry(self, font=("Arial", 14), width=25)
        self.canvas.create_window(320, 930, window=self.entry_nom_utilisateur)

        self.entry_mot_de_passe = Entry(self, font=("Arial", 14), width=25, show="*")
        self.canvas.create_window(320, 1060, window=self.entry_mot_de_passe)

        self.entry_confirmer_mdp = Entry(self, font=("Arial", 14), width=25, show="*")
        self.canvas.create_window(320, 1175, window=self.entry_confirmer_mdp)


####################""""
        self.canvas.create_image(100, 115, image=self.images["i_nom"], anchor="center")
        self.canvas.create_image(100, 230, image=self.images["i_prenom"], anchor="center")
        self.canvas.create_image(100, 345, image=self.images["i_admail"], anchor="center")
        self.canvas.create_image(100, 460, image=self.images["i_adpost"], anchor="center")
        self.canvas.create_image(100, 575, image=self.images["i_societe"], anchor="center")
        self.canvas.create_image(100, 700, image=self.images["i_piece"], anchor="center")
        self.canvas.create_image(100, 815, image=self.images["i_entreprise"], anchor="center")
        self.canvas.create_image(100, 930, image=self.images["i_uti"], anchor="center")
        self.canvas.create_image(100, 1060, image=self.images["i_mdp"], anchor="center")
        self.canvas.create_image(100, 1175, image=self.images["i_cmdp"], anchor="center")

        # Boutons pour les champs demandés
        bouton_nom_ok = Button(
            self,
            image=self.images["i_ok"],
            compound="center",
            borderwidth=0,
            command=lambda: print("Nom sélectionné")
        )
        self.canvas.create_window(500, 115, window=bouton_nom_ok)

        bouton_prenom_ok = Button(
            self,
            image=self.images["i_ok"],
            compound="center",
            borderwidth=0,
            command=lambda: print("Prénom sélectionné")
        )
        self.canvas.create_window(500, 230, window=bouton_prenom_ok)

        bouton_adresse_mail_ok = Button(
            self,
            image=self.images["i_ok"],
            compound="center",
            borderwidth=0,
            command=lambda: print("Adresse Mail sélectionnée")
        )
        self.canvas.create_window(500, 345, window=bouton_adresse_mail_ok)

        bouton_adresse_postale_ok = Button(
            self,
            image=self.images["i_ok"],
            compound="center",
            borderwidth=0,
            command=lambda: print("Adresse Postale sélectionnée")
        )
        self.canvas.create_window(500, 460, window=bouton_adresse_postale_ok)

        bouton_raison_sociale_ok = Button(
            self,
            image=self.images["i_ok"],
            compound="center",
            borderwidth=0,
            command=lambda: print("Raison Sociale sélectionnée")
        )
        self.canvas.create_window(500, 575, window=bouton_raison_sociale_ok)

        bouton_scan_piece_ok = Button(
            self,
            image=self.images["i_ok"],
            compound="center",
            borderwidth=0,
            command=lambda: print("Scan Pièce sélectionné")
        )
        self.canvas.create_window(500, 700, window=bouton_scan_piece_ok)

        bouton_entreprise_ok = Button(
            self,
            image=self.images["i_ok"],
            compound="center",
            borderwidth=0,
            command=lambda: print("Entreprise sélectionnée")
        )
        self.canvas.create_window(500, 815, window=bouton_entreprise_ok)

        bouton_nom_utilisateur_ok = Button(
            self,
            image=self.images["i_ok"],
            compound="center",
            borderwidth=0,
            command=lambda: print("Nom Utilisateur sélectionné")
        )
        self.canvas.create_window(500, 930, window=bouton_nom_utilisateur_ok)

        bouton_mot_de_passe_ok = Button(
            self,
            image=self.images["i_ok"],
            compound="center",
            borderwidth=0,
            command=lambda: print("Mot de Passe sélectionné")
        )
        self.canvas.create_window(500, 1060, window=bouton_mot_de_passe_ok)

        bouton_confirmer_mdp_ok = Button(
            self,
            image=self.images["i_ok"],
            compound="center",
            borderwidth=0,
            command=lambda: print("Confirmer le mot de passe")
        )
        self.canvas.create_window(500, 1175, window=bouton_confirmer_mdp_ok)

        self.bouton_valider = Button(
            self,
            image=self.images["i_ok"],
            compound="center",
            borderwidth=0,
        )
        self.canvas.create_window(500, 1290, window=self.bouton_valider)


        bouton_fermer = Button(
            self,
            image=self.images["fermer"],
            compound="center",
            bg="#7894a4",
            borderwidth=0,
            command=self.quit)
        self.canvas.create_window(1250, 30, window=bouton_fermer)


        # Optionnel : définir une région scrollable
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    # Molette Windows / Mac
    def _on_mousewheel(self, event):
        # Inverse the scrolling direction
        self.canvas.yview_scroll(int(event.delta / 120), "units")

    # Molette Linux
    def _on_mousewheel_linux(self, event):
        if event.num == 4:
            # Inverse the scrolling direction
            self.canvas.yview_scroll(1, "units")
        elif event.num == 5:
            # Inverse the scrolling direction
            self.canvas.yview_scroll(-1, "units")

    def acces_autorise(self):
        self.destroy()
        if __name__ == "__main__":
            accueil.main()

    def acces_inscription(self):
        self.destroy()
        if __name__ == "__main__":
            inscription.main()


if __name__ == "__main__":
    app = Affiche_Inscription()
    app.mainloop()