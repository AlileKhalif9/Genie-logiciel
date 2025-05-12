from tkinter import *
import tkintermapview

# Création de la fenêtre principale
root = Tk()
root.title("Test carte minimal")
root.geometry("800x600")

# Widget carte
map_widget = tkintermapview.TkinterMapView(root, width=800, height=600)
map_widget.pack(fill="both", expand=True)

# Centrage sur Paris avec zoom
map_widget.set_position(48.8566, 2.3522)
map_widget.set_zoom(10)

# Lancement
root.mainloop()
