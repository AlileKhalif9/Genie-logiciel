from tkinter import *
import subprocess

#Classe de controlleur qui va recuperer les données 
#Et une classe qui gere l'IHM 
#Donc une classe qui affiche et une qui recupere les données 


# Chemin du dossier contenant les images
button_folder = r"res/button"


def menu():
    global window 
    # Création de la fenêtre
    window = Tk()
    window.title("Projet Genie Logiciel")
    window.geometry("1280x800")
    window.resizable(False, False)
    window.config(background="#767171")

    # Canvas
    canvas = Canvas(window, width=1080, height=720, bg="#2A2F4F", highlightthickness=0)
    canvas.pack(fill=BOTH, expand=True)

    # Images pour faire les boutons
    button_image1 = PhotoImage(file="../res/button/button_1_cyan.png")
    button_image2 = PhotoImage(file="../res/button/button_1_mallow_grand.png")
    button_image3 = PhotoImage(file="../res/button/close.png")
    button_image4 = PhotoImage(file="../res/button/log_button_2.png")
    button_image5 = PhotoImage(file="../res/button/password_button.png")

    # Ajouter un titre
    canvas.create_text(
        540, 50, text="Projet IHM ", font=("Arial", 40, "bold"), fill="white", anchor="center"
    )

    # Bouton connexion
    button1 = Button(
        window,
        text="Connexion",
        font=("Arial", 20),
        image=button_image1,
        compound="center",  
        bg="#2A2F4F",
        fg="black",
        borderwidth=0,
        command=lambda: save_text()  # ← action de sauvegarde ici
    )
    button1.place(x=850, y=370)


    button2 = Button(
        window,
        text="Inscription",
        font=("Arial", 20),
        image=button_image2,
        compound="center",
        bg="#2A2F4F",
        fg="black",
        borderwidth=0,
        command=lambda: print("Bouton 2 cliqué")
    )
    button2.place(x=1050, y=370)



    button3 = Button( #Bouton exit
        window,
        text=" ",
        font=("Arial", 20),
        image=button_image3,
        compound="center",
        bg="#2A2F4F",
        fg="black",
        borderwidth=0,
        command=window.quit
    )
    button3.place(x=1200, y=30)
    

    # Champs de connexion

    entry_user = Entry(window, font=("Arial", 14), width=25)
    entry_user.place(x=520, y=250)


    entry_pass = Entry(window, font=("Arial", 14), width=25, show="*")
    entry_pass.place(x=520, y=300)

#pas sur 
    def save_text():
        identifiant = entry_user.get()
        mot_de_passe = entry_pass.get()
        print(f"Identifiant : {identifiant}")
        print(f"Mot de passe : {mot_de_passe}")

    canvas.create_image(640, 400, image=button_image4, anchor="center")
    canvas.create_window(640, 380, window=entry_user)
    canvas.create_window(640, 420, window=entry_pass)

    window.mainloop()

if __name__ == "__main__":
    global window 
    menu()



