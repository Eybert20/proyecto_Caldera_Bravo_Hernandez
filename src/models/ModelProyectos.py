from .entidades.Proyecto import Proyecto

class ModelProyectos():

    @classmethod
    def get(self, db):
        try: 
            cursor = db.cursor()
            sql = "SELECT * FROM proyectos"
            cursor.execute(sql)
            result = cursor.fetchall()
            if result != None:
               proyecto = [Proyecto(row[0], row[1], row[2], row[3], row[4], row[5], row[6]).to_dict() for row in result]
               return proyecto
        except Exception as e:
            raise Exception(e)
        finally:
            cursor.close()


    @classmethod
    def store(self, db, proyecto):
        try:
            cursor = db.cursor()
            sql = "INSERT INTO proyectos (categoria_id, usuario_id, titulo, descripcion, fecha_inicio, fecha_fin) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(proyecto.get('categoria_id'),proyecto.get('usuario_id'),proyecto.get('titulo'),proyecto.get('descripcion'),proyecto.get('fecha_inicio'),proyecto.get('fecha_fin'))
            cursor.execute(sql)
            db.commit()
            if cursor.rowcount == 1:
                return True
            else:
                return False
        except Exception as e:
            raise Exception(e)
        finally:
            cursor.close()



    @classmethod
    def destroy(self, db, id):
        try:
            cursor = db.cursor()
            sql = "DELETE FROM proyectos WHERE id = {}".format(id)
            cursor.execute(sql)
            db.commit()
            if cursor.rowcount == 1:
                return True
            else:
                return False
        except Exception as e:
            raise Exception(e)
        finally:
            cursor.close()        