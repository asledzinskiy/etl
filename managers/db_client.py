import psycopg2
import settings



class DbClient(object):

    def __init__(self, port):
        self.db_user = settings.DB_USER
        self.db_passwd = settings.DB_PASSWORD
        self.db_schema = settings.DB_SCHEMA
        self.db_host = settings.DB_HOST
        self.port = port
        self.create_connection()

    def create_connection(self):
        self.conn=psycopg2.connect(
            "dbname='{}' user='{}' password='{}'"
            " host='{}' port='{}'".format(self.db_schema, self.db_user,
                                          self.db_passwd, self.db_host, self.port))
        return self.conn

    def execute_query(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
