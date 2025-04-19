from tkinter import *
#import pyautogui 
#for tkinter import filedialog 
#import timer 
import os

############# REF -> https://www.youtube.com/watch?v=eQRCYlJzO4c ##########################



class Affiche_creation_devis(Tk):
    def __init__(self):
        super().__init__()
        self.title("Création Devis")
        self.geometry("1280x800")
        self.resizable(False, False)
        self.config(background="#2A2F4F")
        self.utilisateur_connecte = None

        self.id_devis_actuel = self.get_next_id()  # Initialisation de l'ID
        self.afficher_interface()

    def afficher_interface(self):
        # Création du canvas
        self.canvas = Canvas(self, width=1280, height=800, bg="#7894a4", highlightthickness=0)
        self.canvas.pack(fill=BOTH, expand=True)

        # Scroll
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.canvas.bind_all("<Button-4>", self._on_mousewheel_linux)
        self.canvas.bind_all("<Button-5>", self._on_mousewheel_linux)

        # Titre
        self.canvas.create_text(640, 50, text="Création Devis", font=("Arial", 40, "bold"), fill="black", anchor="center")

        # Bouton de capture
        bouton_screen = Button(
            self,
            text="Enregistrer Devis",
            font=("Arial", 16, "bold"),
            bg="blue",
            fg="white",
            command=self.capture_fenetre
        )
        self.canvas.create_window(640, 120, window=bouton_screen)

    def get_next_id(self):
        # Recherche du prochain ID dispo dans le dossier
        dossier = r"C:\Users\S\Documents\Prog\L3\S2\Projet_Genie_Logiciel\res"
        id_max = 0
        for fichier in os.listdir(dossier):
            if fichier.startswith("Devis_") and fichier.endswith(".png"):
                try:
                    id_num = int(fichier.split("_")[1].split(".")[0])
                    id_max = max(id_max, id_num)
                except:
                    pass
        return id_max + 1

    def capture_fenetre(self):
        # Coordonnées de la fenêtre Tkinter
        x = self.winfo_rootx()
        y = self.winfo_rooty()
        w = self.winfo_width()
        h = self.winfo_height()

        # Définir chemin auto
        dossier = r"C:\Users\S\Documents\Prog\L3\S2\Projet_Genie_Logiciel\res"
        nom = f"Devis_{self.id_devis_actuel}.png"
        chemin = os.path.join(dossier, nom)

        # Capture partielle
        pyautogui.screenshot(chemin, region=(x, y, w, h))
        print(f"Devis enregistré : {chemin}")

        # Affichage dans une popup
        self.afficher_popup_image(chemin)

        # Incrémenter l'ID pour le prochain devis
        self.id_devis_actuel += 1

    def afficher_popup_image(self, chemin_image):
        popup = Toplevel(self)
        popup.title("Aperçu du devis")
        popup.geometry("600x450")
        popup.configure(bg="#2A2F4F")

        image = Image.open(chemin_image)
        image = image.resize((580, 400), Image.ANTIALIAS)
        self.popup_image = ImageTk.PhotoImage(image)

        Label(popup, image=self.popup_image, bg="#2A2F4F").pack(pady=20)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(event.delta / 120), "units")

    def _on_mousewheel_linux(self, event):
        if event.num == 4:
            self.canvas.yview_scroll(1, "units")
        elif event.num == 5:
            self.canvas.yview_scroll(-1, "units")


if __name__ == "__main__":
    app = Affiche_creation_devis()
    app.mainloop()
