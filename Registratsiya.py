from psycopg2 import connect
from keyboards import get_contact1
from connectDB import *
class Registration:
    host = 'localhost'
    username = 'postgres'
    password = '!1234567A@'
    # db_name = 'AutoSchool'
    db_name = 'AutoSchool'
    def __init__(self,tg_id):
        self.tg_id = tg_id
        if is_logged(tg_id):
            self.f_name, self.phone, self.viloyat, self.tuman = tuple(self.load_from_db(tg_id))
            print(self.f_name, self.phone, self.viloyat, self.tuman)
        else:
            self.record_DB()
            self.f_name, self.phone, self.viloyat, self.tuman = tuple(self.load_from_db(tg_id))

            print(self.f_name, self.phone, self.viloyat, self.tuman)
    def load_from_db(self, tg_id):
        try:
            conn = connect(host=self.host, user=self.username, password=self.password, database=self.db_name)
            cursor = conn.cursor()
            sql = f"""
            SELECT f_name, phone, viloyat, tuman FROM Tester WHERE tg_id = {tg_id}
            """
            conn.autocommit = True
            cursor.execute(sql)
            res = []
            for i in cursor.fetchall():
                res = i
            conn.close()
            return res
        except Exception as e:
            print('Error', e)

    def record_DB(self):
        try:
            conn = connect(host=self.host, user=self.username, password=self.password, database=self.db_name)
            cursor = conn.cursor()
            conn.autocommit = True
            sql = f"""
            INSERT INTO public.Tester(
                f_name, phone, viloyat, tuman, tg_id)
                VALUES (' ' , ' ' , ' ' , ' ', {self.tg_id});
                """
            cursor.execute(sql)
            conn.close()
        except Exception as e:
            print('Error', e)

    def update_reg(self, item, value):
        try:
            conn = connect(host=host, user=username, password=password, database=db_name)
            cursor = conn.cursor()
            conn.autocommit = True
            sql = f"""
            UPDATE public.Tester
            SET {item} = '{value}'
            WHERE tg_id = {self.tg_id}
                    """
            cursor.execute(sql)
            conn.close()
        except Exception as e:
            print('Error', e)


    # update_reg('f_name',"Someone",904270887)