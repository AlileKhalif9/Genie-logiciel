import datetime

class Quote:
    quote_id = "Q000"  # Variable globale pour les identifiants uniques des devis

    def __init__(self, order, order_quantities, price_no_taxes, price):
        self.order = order
        self.order_quantities = order_quantities
        self.price_no_taxes = price_no_taxes
        self.price = price
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
    
    def upadate_status(self):
        if(self.status == False):
            self.status = True
        else:
            self.status = False

    @classmethod
    def clear_id(cls):
        cls.quote_id = "Q001"

    
