from werkzeug.security import check_password_hash, generate_password_hash
class persona:
    def __init__(self,id,usuario,contraseña,nombre):
        self.id = id
        self.usuario = usuario
        self.contraseña = contraseña
        self.nombre = nombre

    @classmethod
    def check_password(self,hashed_password,password):
        return check_password_hash(hashed_password,password)



    def formato_doc(self):
        return{
            'id': self.id,
            'usuario': self.usuario,
            'contraseña': self.contraseña,
            'nombre': self.nombre
    
        }   

