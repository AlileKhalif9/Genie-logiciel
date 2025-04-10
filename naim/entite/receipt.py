from .quote import Quote

class Receipt(Quote):
    receipt_id = "R000"

    def __init__(self, order, order_quantities, price):
        super().__init__(order, order_quantities)
        self.__id = self.update_id()
        self.status = False
        self.price = self.calculate_price()

    def calculate_price(self):
        res = 0
        for q in self.order_quantities:
            res += q
        return res

    def update_id(self):
        nb = int(Receipt.receipt_id[1:]) + 1
        new_id = "R" + str(nb).zfill(3)  
        Receipt.receipt_id = new_id  # Mise à jour de l'ID global
        return new_id

    def get_id(self):
        return self.__id
    
    def update_status(self): 
        self.status = not self.status 

    @classmethod
    def clear_id(cls):
        cls.receipt_id = "R000"

    def __str__(self):
        order_str = ", ".join(self.order) 
        quantities = ", ".join(map(str, self.order_quantities))
        return f"Facture numéro : {self.get_id()}, prix : {self.price}, liste commande : {order_str}, quantite : {quantities}"
