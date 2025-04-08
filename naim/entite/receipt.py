from quote import *

class Receipt(Quote):
    receipt_id = "R001"

    def __init__(self, order, order_quantities, price_no_taxes, price, paiement_date):
        super().__init__(order, order_quantities, price_no_taxes, price)
        self.__id = self.update_id()
        self.status = False
        self.paiement_date = paiement_date

    def update_id(self):
        nb = int(Receipt.receipt_id[1:]) + 1
        new_id = "R" + str(nb).zfill(3)  
        Receipt_id = new_id  # Mise à jour de l'ID global
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
        cls.receipt_id = "R001"

    