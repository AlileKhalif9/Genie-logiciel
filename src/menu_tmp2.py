from tkinter import *
import os
import acceuil
import inscription

class Affiche_Acceuil(Tk):
    def __init__(self):
        super().__init__()
        self.title("Projet Génie Logiciel")
        self.geometry("1280x800")
        self.resizable(False, False)
        self.config(background="#2A2F4F")
        self.utilisateur_connecte = None

        self.button_folder = "../res/button"
        self.images_folder = "../res/images"

        # Chargement des images
        self.images = {
            "connexion": PhotoImage(file=os.path.join(self.button_folder, "button_1_cyan.png")),
            "mdp": PhotoImage(file=os.path.join(self.button_folder, "button_1_mallow_grand.png")),
            "fermer": PhotoImage(file=os.path.join(self.button_folder, "close.png")),
            "connect": PhotoImage(file=os.path.join(self.button_folder, "connexion_resize.png")),
            "lock": PhotoImage(file=os.path.join(self.button_folder, "cadenas_resize.png")),
            "explain": PhotoImage(file=os.path.join(self.images_folder, "explain_screen_v3.png")),
            "condi": PhotoImage(file=os.path.join(self.button_folder, "conditions_button_v2.png")),
            "language": PhotoImage(file=os.path.join(self.button_folder, "language_button_v2.png")),
            "help_button": PhotoImage(file=os.path.join(self.button_folder, "help.png")),
            "register_button":PhotoImage(file=os.path.join(self.button_folder, "register.png"))
        }

        self.afficher_connexion()

    def afficher_connexion(self):
        # Création du canvas
        self.canvas = Canvas(self, width=1280, height=800, bg="#2A2F4F", highlightthickness=0)
        self.canvas.pack(fill=BOTH, expand=True)
        

        # Activation de la molette (scroll)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)  # Windows / Mac
        self.canvas.bind_all("<Button-4>", self._on_mousewheel_linux)  # Linux scroll up
        self.canvas.bind_all("<Button-5>", self._on_mousewheel_linux)  # Linux scroll down

        # Texte
        self.canvas.create_text(640, 50, text="Projet IHM", font=("Arial", 40, "bold"), fill="white", anchor="center")

        # Images décoratives
        self.canvas.create_image(90, 380, image=self.images["connect"], anchor="center")
        self.canvas.create_image(630, 380, image=self.images["lock"], anchor="center")
        self.canvas.create_image(350, 600, image=self.images["explain"], anchor="center")

        # Champs utilisateur / mot de passe
        entry_user = Entry(self, font=("Arial", 14), width=25)
        entry_pass = Entry(self, font=("Arial", 14), width=25, show="*")
        self.canvas.create_window(250, 380, window=entry_user)
        self.canvas.create_window(800, 380, window=entry_pass)

        # Boutons
        bouton_connexion = Button(
            self,
            image=self.images["connexion"],
            text="Connexion",
            compound="center",
            font=("Arial", 20),
            bg="#2A2F4F",
            fg="black",
            borderwidth=0,
            command=lambda: print("Connexion"))
        self.canvas.create_window(485, 380, window=bouton_connexion)

        bouton_inscription = Button(
            self,
            image=self.images["mdp"],
            text="Mot de passe",
            compound="center",
            font=("Arial", 17),
            bg="#2A2F4F",
            fg="black",
            borderwidth=0,
            command=lambda: print("Mot de passe"))
        self.canvas.create_window(1040, 380, window=bouton_inscription)

        bouton_fermer = Button(
            self,
            image=self.images["fermer"],
            text=" ",
            compound="center",
            font=("Arial", 20),
            bg="#2A2F4F",
            fg="black",
            borderwidth=0,
            command=self.quit)
        self.canvas.create_window(1250, 30, window=bouton_fermer)

        language = Button(
            self,
            image=self.images["language"],
            compound="center",
            bg="#2A2F4F",
            fg="black",
            borderwidth=0,
            command=lambda: print("Langue"))
        self.canvas.create_window(1100, 550, window=language)

        conditions = Button(
            self,
            image=self.images["condi"],
            compound="center",
            bg="#2A2F4F",
            fg="black",
            borderwidth=0,
            command=lambda: print("Conditions"))
        self.canvas.create_window(1100, 660, window=conditions)

        help = Button(
            self,
            image=self.images["help_button"],
            text=" ",
            compound="center",
            font=("Arial", 20),
            bg="#2A2F4F",
            fg="black",
            borderwidth=0,
            command=lambda: print("Aide"))
        self.canvas.create_window(1250, 715, window=help)
    
        register = Button(
            self,
            image=self.images["register_button"],
            text=" ",
            compound="center",
            font=("Arial", 20),
            bg="#2A2F4F",
            fg="black",
            borderwidth=0,
            command=lambda: print("Aide"))
        self.canvas.create_window(200, 200, window=register)

        # Optionnel : définir une région scrollable
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    # Molette Windows / Mac
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    # Molette Linux
    def _on_mousewheel_linux(self, event):
        if event.num == 4:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            self.canvas.yview_scroll(1, "units")

    def acces_autorise(self):
        self.destroy()
        if __name__ == "__main__":
            acceuil.main()

    def acces_inscription(self):
        self.destroy()
        if __name__ == "__main__":
            inscription.main()


class Utilisateur:
    def __init__(self, identifiant, nom, email):
        self.identifiant = identifiant
        self.nom = nom
        self.email = email


if __name__ == "__main__":
    app = Affiche_Acceuil()
    app.mainloop()
