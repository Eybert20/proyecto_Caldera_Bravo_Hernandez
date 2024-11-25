from .entidades.Categoria import Categoria

class ModelCategorias():

    @classmethod
    def get(self, db):
        try: 
            cursor = db.cursor()
            sql = "SELECT * FROM categorias"
            cursor.execute(sql)
            result = cursor.fetchall()
            if result != None:
               categoria = [Categoria(row[0], row[1], row[2]).to_dict() for row in result]
               return categoria
        except Exception as e:
            raise Exception(e)
        finally:
            cursor.close()


    @classmethod
    def store(self, db, categoria):
        try:
            cursor = db.cursor()
            sql = "INSERT INTO categorias (nombre, descripcion) VALUES ('{}', '{}')".format(categoria.get('nombre'),categoria.get('descripcion'))
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
            sql = "DELETE FROM categorias WHERE id = {}".format(id)
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