import sqlite3
from . import Data_Base

class Db_Inscri(Data_Base):
    def __init__(self, db_name="users.db"):
        super().__init__(db_name)

    def init_db(self):
        self.connect()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS user (
                name TEXT NOT NULL,
                surname TEXT NOT NULL,
                username TEXT NOT NULL UNIQUE,
                phone TEXT,
                email TEXT NOT NULL,
                address TEXT NOT NULL,
                password TEXT NOT NULL
            )
        """)
        self.conn.commit()
        self.disconnect()


    def add_user(self, name, surname, username, phone, email, address, password):
        self.connect()
        self.cur.execute("""
            INSERT INTO user (name, surname, username, phone, email, address, password)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (name, surname, username, phone, email, address, password))
        self.conn.commit()
        self.disconnect()


    def clear_all_users(self):
        self.connect()
        self.cur.execute("DELETE FROM user")
        self.conn.commit()
        self.disconnect()
        print("Tous les utilisateurs ont été supprimés de la base de données.\n")
