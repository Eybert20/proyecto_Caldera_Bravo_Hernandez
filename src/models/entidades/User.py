from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, id, nombre, email, password, Rol) -> None:
        self.id = id
        self.nombre = nombre
        self.email = email
        self.password = password
        self.Rol = Rol
        
        
        

    @classmethod
    def verify_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)
    
#con geenerate_password_hash se encripta la contraseña
#print(generate_password_hash("123"))