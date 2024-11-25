class Categoria:
    def __init__(self, id, nombre, descripcion) -> None:
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion
    }    