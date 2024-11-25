class Proyecto:
    def __init__(self, id, categoria_id, usuario_id, titulo, descripcion, fecha_inicio, fecha_fin) -> None:
        self.id = id
        self.categoria_id = categoria_id
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        
    def to_dict(self):
        return {
            'id': self.id,
            'categoria_id': self.categoria_id,
            'usuario_id': self.usuario_id,
            'titulo': self.titulo,
            'descripcion': self.descripcion,
            'fecha_inicio': self.fecha_inicio,
            'fecha_fin': self.fecha_fin
    }    