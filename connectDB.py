from psycopg2 import connect

host = 'localhost'
username = 'postgres'
password = '!1234567A@'
db_name = 'AutoSchool'

def get_region():
    try:
        conn = connect(host=host, user=username, password=password, database=db_name)
        cursor = conn.cursor()
        sql = """
                SELECT region_id, region_name FROM viloyat
                ORDER BY region_id ASC
                """
        conn.autocommit = True
        cursor.execute(sql)
        res = []
        for i in cursor.fetchall():
            res.append(i)
        conn.close()
        return res

    except Exception as e:
        print('Error', e)
def tuman_write(tum_id):
    try:
        conn = connect(host=host, user=username, password=password, database=db_name)
        cursor = conn.cursor()
        sql = f"""
                SELECT viloyat_id, tuman_name FROM tuman WHERE tuman_id = {tum_id}

            """
        conn.autocommit = True
        cursor.execute(sql)
        res = []
        for i in cursor.fetchall():
            res.append(i)
        conn.close()
        return res

    except Exception as e:
        print('Error', e)

def get_link():
    try:
        conn = connect(host=host, user=username, password=password, database=db_name)
        cursor = conn.cursor()
        sql = f"""
        SELECT link FROM link_book
        """
        conn.autocommit = True
        cursor.execute(sql)
        res = []
        for i in cursor.fetchall():
            res.append(i)
        conn.close()
        return res
    except Exception as e:
        print('Error', e)

def get_link_lesson():
    try:
        conn = connect(host=host, user=username, password=password, database=db_name)
        cursor = conn.cursor()
        sql = f"""
        SELECT link_id,link FROM link_lesson
        """
        conn.autocommit = True
        cursor.execute(sql)
        res = []
        for i in cursor.fetchall():
            res.append(i)
        conn.close()
        return res
    except Exception as e:
        print('Error', e)
def is_logged(tg_id):
    try:
        conn = connect(host=host, user=username, password=password, database=db_name)
        cursor = conn.cursor()
        sql = f"""
        SELECT * FROM tester
        WHERE tg_id = {tg_id} 
        """
        conn.autocommit = True
        cursor.execute(sql)
        r = len(cursor.fetchall()) == 1
        conn.close()
        return r
    except Exception as e:
        print('Error', e)
def delete_acc(tg_id):
    try:
        conn = connect(host=host, user=username, password=password, database=db_name)
        cursor = conn.cursor()
        sql = f"""
        DELETE FROM public.tester WHERE tg_id = {tg_id};
        """
        conn.autocommit = True
        cursor.execute(sql)
        conn.close()
    except Exception as e:
        print('Error', e)
def get_acc():
    try:
        conn = connect(host=host, user=username, password=password, database=db_name)
        cursor = conn.cursor()
        sql = f"""
        SELECT j_id, f_name, phone, viloyat, tg_id FROM public.tester;
        """
        conn.autocommit = True
        cursor.execute(sql)
        res = []
        for i in cursor.fetchall():
            res.append(i)
        conn.close()
        return res
    except Exception as e:
        print('Error', e)