from .entidades.User import User


class ModelUser():

    @classmethod
    def login(self, db, user):
        try:
            cursor = db.cursor()
            sql = "SELECT * FROM users WHERE correo = '{}'".format(user.email)
            cursor.execute(sql)
            result = cursor.fetchone()
            if result != None:
                user = User(result[0], result[1], result[2], User.verify_password(result[3], user.password), result[4])
                return user


        except Exception as e:
            raise Exception(e)

    @classmethod
    def get_user_by_id(self, db, id):
        try:
            cursor = db.cursor()
            sql = "SELECT * FROM users WHERE id = '{}'".format(id)
            cursor.execute(sql)
            result = cursor.fetchone()
            if result != None:
                return User(result[0], result[1], result[2], None, None)
        except Exception as e:
            raise Exception(e)            