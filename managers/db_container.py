import docker
import settings
import time




class DbContainer(object):


    def __init__(self):
        self.db_user = settings.DB_USER
        self.db_passwd = settings.DB_PASSWORD
        self.db_schema = settings.DB_SCHEMA
        self.initialize_client()

    def initialize_client(self):
        self.client = docker.from_env()

    def create_container(self):
        self.db_container =\
            self.client.containers.run("postgres:latest",
                                       environment={"POSTGRES_USER": self.db_user,
                                                    "POSTGRES_PASSWORD": self.db_passwd,
                                                    "POSTGRES_DB": self.db_schema},
                                       ports={"5432/tcp": None}, detach=True)
        time.sleep(15)
        self.db_container.reload()
        self.db_container.exec_run(
            cmd="psql -v ON_ERROR_STOP=1 --username {} -c 'GRANT ALL PRIVILEGES"
                " ON DATABASE {} TO PUBLIC'".format(self.db_user, self.db_schema))
        return self.db_container

    def get_port(self):
        return self.db_container.attrs['NetworkSettings']['Ports']['5432/tcp'][0]['HostPort']

    def stop_container(self):
        self.db_container.stop()

    def remove_container(self):
        self.db_container.remove()