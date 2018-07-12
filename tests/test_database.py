from managers.db_container import DbContainer
from managers.db_client import DbClient


class TestDatabase(object):

    @classmethod
    def setup_class(cls):
        cls.database = DbContainer()
        cls.database.create_container()
        port = cls.database.get_port()
        print("port is " + port)
        cls.database_client = DbClient(port)
        cls.database_client.create_connection()

    def test_check_database(self):
        self.database_client.execute_query("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
        import time
        print("check database for table creation")
        time.sleep(300)

    @classmethod
    def teardown_class(cls):
        cls.database.stop_container()
        cls.database.remove_container()