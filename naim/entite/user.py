import re

class User:
    def __init__(self, name : str, surname : str, username : str, mobile_phone : str, email : str, postal_adress : str, password : str):
        self.name = name
        self.surname = surname
        self.username = username
        self.mobile_phone = mobile_phone
        self.email = self._validate_email(email)
        self.postal_adress = postal_adress
        self.__password = self._validate_password(password)

    def _validate_email(self, email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            raise ValueError("Email is not valid")
        return email

    def _validate_password(self, password):
        # Vérifie qu'il y a au moins 8 caractères, une majuscule, une minuscule et un chiffre
        if len(password) < 8 or not any(c.isupper() for c in password) or not any(c.isdigit() for c in password):
            raise ValueError("Password is not strong enough")
        return password

    def to_dict(self):
            return {
                'name': self.name,
                'surname': self.surname,
                'mobile_phone': self.mobile_phone,
                'email': self.email,
                'postal_adress': self.postal_adress
            }

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}, Phone: {self.mobile_phone}"