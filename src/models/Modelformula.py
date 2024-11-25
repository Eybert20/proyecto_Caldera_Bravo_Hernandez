from .entidades.Formula import Formula

class ModelFormula():

    @classmethod
    def get(self, db):
        try: 
            cursor = db.cursor()
            sql = "SELECT * FROM formulas"
            cursor.execute(sql)
            result = cursor.fetchall()
            if result != None:
               formulas = [Formula(row[0], row[1], row[2], row[3]).to_dict() for row in result]
               return formulas
        except Exception as e:
            raise Exception(e)
        finally:
            cursor.close()

    
    @classmethod
    def show(self, db, id):
        try: 
            cursor = db.cursor()
            sql = "SELECT * FROM formulas WHERE id = '{}'".format(id)
            cursor.execute(sql)
            result = cursor.fetchall()
            if result != None:
               formulas = [Formula(row[0], row[1], row[2], row[3]).to_dict() for row in result]
               return formulas
        except Exception as e:
            raise Exception(e)
        finally:
            cursor.close()



    @classmethod
    def store(self, db, formula):
        try:
            cursor = db.cursor()
            sql = "INSERT INTO formulas (nombre, descripcion, expresion) VALUES ('{}', '{}', '{}')".format(formula.get('nombre'),formula.get('descripcion'),formula.get('expresion'),formula.get('expresion'))
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
            sql = "DELETE FROM formulas WHERE id = {}".format(id)
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