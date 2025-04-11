from typing import List, Optional
from ..entite.user import User

class Factory_user:
    _instances: List[User] = []  # Liste statique pour stocker tous les utilisateurs
    
    @classmethod
    def create_user(cls, 
                  name: str, 
                  surname: str, 
                  username: str,
                  mobile_phone: str, 
                  email: str, 
                  postal_address: str, 
                  password: str) -> User:
        
        # Validation basique
        if not all([name, surname, email, username, password]):
            raise ValueError("Tous les champs sont obligatoires")
            
        # Vérification de l'unicité de l'username
        if cls.get_user_by_username(username):
            raise ValueError(f"Le username {username} existe déjà")
        
        # Vérification de l'unicité du mot de passe
        if cls.get_user_password(password):
            raise ValueError(f"Le mot de passe {password} existe déjà")
        
        # Création de l'utilisateur avec les paramètres donnés
        user = User(name, surname, username, mobile_phone, email, postal_address, password)
        cls._instances.append(user)
        return user
    
    @classmethod
    def get_user_by_username(cls, username: str) -> Optional[User]:
        """Trouve un utilisateur par son username"""
        return next((u for u in cls._instances if u.username == username), None)
    
    @classmethod
    def get_user_password(cls, password: str) -> Optional[User]:
        """Trouve un utilisateur par son mot de passe"""
        return next((u for u in cls._instances if u.get_password() == password), None)
    
    @classmethod
    def clear_all(cls):
        """Réinitialise la factory (pour les tests)"""
        cls._instances.clear()

    def __str__(self):
        """Retourne une représentation lisible de la UserFactory."""
        user_count = len(self._instances)
        if user_count == 0:
            return "UserFactory: No users created."
        users_info = ", ".join([f"{user.username} ({user.email})" for user in self._instances])
        return f"L'utilisateur a bien été crée.\nUser: {users_info}"
