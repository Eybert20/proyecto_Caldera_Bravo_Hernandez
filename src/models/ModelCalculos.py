from .entidades.Calculos import  Calculos

class ModelCalculos():

    @classmethod
    def get(self, db, id):
        try: 
            cursor = db.cursor()
            sql = "SELECT * FROM calculos WHERE proyecto_id = '{}'".format(id)
            cursor.execute(sql)
            result = cursor.fetchall()
            if result != None:
               calculos = [Calculos(row[0], row[1], row[2], row[3], row[4],).to_dict() for row in result]
               return calculos
        except Exception as e:
            raise Exception(e)
        finally:
            cursor.close()


    @classmethod
    def store(self, db, calculos):
        try:
            cursor = db.cursor()
            sql = "INSERT INTO calculos (proyecto_id, formula_id, resultado, parametros) VALUES ('{}', '{}','{}', '{}')".format(calculos.get('proyecto_id'),calculos.get('formula_id'),calculos.get('resultado'),calculos.get('parametros'))
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
            sql = "DELETE FROM calculo WHERE id = {}".format(id)
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