class Formula:
    def __init__(self, id, nombre, descripcion, expresion) -> None:
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.expresion = expresion

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'expresion': self.expresion
    }    