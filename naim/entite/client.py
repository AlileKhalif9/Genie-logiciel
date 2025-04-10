import re

class Client:
    client_id = "C000"  # Attribut de classe pour suivre l'ID des clients

    def __init__(self, name, surname, mobile_phone, email, postal_address):
        self.name = name
        self.surname = surname
        self.mobile_phone = self._validate_mobile_phone(mobile_phone)
        self.email = self._validate_email(email)
        self.postal_address = postal_address
        self.__id = self.update_id()

    def _validate_email(self, email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            raise ValueError("Invalid email format")
        return email

    def _validate_mobile_phone(self, mobile_phone):
        phone_regex = r'^\+?[1-9]\d{1,14}$'  # Format international de téléphone
        if not re.match(phone_regex, mobile_phone):
            raise ValueError("Invalid phone number")
        return mobile_phone

    def update_id(self):
        nb = int(Client.client_id[1:]) + 1
        new_id = "C" + str(nb).zfill(3)
        Client.client_id = new_id  # Mise à jour de l'attribut de classe
        return new_id

    def get_id(self):
        return self.__id

    def __str__(self):
        return f"Client ID: {self.__id}, Name: {self.name} {self.surname}, Email: {self.email}"

    @classmethod
    def reset_id_counter(cls):
        cls.client_id = "C000"  # Réinitialise l'attribut de classe

