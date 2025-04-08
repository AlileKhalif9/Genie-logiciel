import datetime

class Client:
    client_id = "C001"  # Attribut de classe pour suivre l'ID des clients

    def __init__(self, name, surname, mobile_phone, email, postal_address):
        self.name = name
        self.surname = surname
        self.mobile_phone = mobile_phone
        self.email = email
        self.postal_address = postal_address
        self.__id = self.update_id()
        self.is_active = True
        

    def update_id(self):
        nb = int(Client.client_id[1:]) + 1
        new_id = "C" + str(nb).zfill(3)
        Client.client_id = new_id  # Mise à jour de l'attribut de classe
        return new_id

    def get_id(self):
        return self.__id

    @classmethod
    def clear_id(cls):
        cls.client_id = "C001"  # Réinitialise l'attribut de classe

