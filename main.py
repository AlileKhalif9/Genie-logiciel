from naim.entite.user import User
from naim.entite.client import Client
from naim.entite.quote import Quote
from naim.entite.receipt import Receipt

q = Quote(["bois", "tuyaux"], [1, 2])
r = Receipt(["bois", "tuyaux"], [1, 2], 12)
print(r)
