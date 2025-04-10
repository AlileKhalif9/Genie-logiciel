import datetime

class Quote:
    quote_id = "Q000"  # Variable globale pour les identifiants uniques des devis

    def __init__(self, order, order_quantities):
        if not isinstance(order, list) or not all(isinstance(item, str) for item in order):
            raise ValueError("Order must be a list of strings.")
        
        if not isinstance(order_quantities, list) or not all(isinstance(quantity, int) for quantity in order_quantities):
            raise ValueError("Order quantities must be a list of integers.")
        
        if len(order) != len(order_quantities):  # Vérifie que les listes ont la même longueur
            raise ValueError("Order and order_quantities must have the same length.")
        
        self.order = order
        self.order_quantities = order_quantities
        self.__id = self.update_id()
        self.date = datetime.date.today()
        self.status = False


    def update_id(self):
        nb = int(Quote.quote_id[1:]) + 1
        new_id = "Q" + str(nb).zfill(3)  
        quote_id = new_id  # Mise à jour de l'ID global
        return new_id

    def get_id(self):
        return self.__id
    
    def update_status(self):
        if(self.status == False):
            self.status = True
        else:
            self.status = False

    def __str__(self):
        order_str = ", ".join(self.order)  # Crée une liste avec les éléments de la commande
        quantities = ", ".join(map(str, self.order_quantities)) # Crée une liste avec les quantitées des éléments de la commande
        return f"Devis numéro : {self.get_id()}, date : {self.date}, commande : {order_str}, quantités : {quantities}"


    @classmethod
    def clear_id(cls):
        cls.quote_id = "Q000"

    