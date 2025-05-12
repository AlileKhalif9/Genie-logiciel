from tkinter import *
import tkintermapview
import re
import os
import sys

racine = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if racine not in sys.path:
    sys.path.insert(0, racine)

from src.dao.dao_client import Db_Client

CP_COORDS = {
    "83130": (43.135, 6.010),  # La Garde
    "75001": (48.864, 2.332),  # Paris
    "13001": (43.296, 5.369),  # Marseille
    "06000": (43.710, 7.262),  # Nice
    "83000": (43.125, 5.930),  # Toulon
}

def extraire_code_postal(adresse):
    match = re.search(r"\b(\d{5})\b", adresse)
    return match.group(1) if match else None


root = Tk()
root.title("Carte des clients")
root.geometry("900x700")

my_label = LabelFrame(root)
my_label.pack(pady=20)

# Affichage de la cartre
map_widget = tkintermapview.TkinterMapView(my_label, width=800, height=600)
map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
map_widget.set_position(43.135, 6.010)  # Centré sur La Garde
map_widget.set_zoom(7)

# Lecture adresses clients
db = Db_Client()
clients = db.get_all_clients_summary()

for client in clients:
    adresse = client['address']
    nom = f"{client['surname']} {client['name']}"
    cp = extraire_code_postal(adresse)

    if cp and cp in CP_COORDS:
        lat, lon = CP_COORDS[cp]
        map_widget.set_marker(lat, lon, text=nom, marker_color_circle="red", marker_color_outside="black")
    else:
        print(f"Code postal inconnu pour : {nom} / adresse : {adresse}")

map_widget.pack()

root.mainloop()
