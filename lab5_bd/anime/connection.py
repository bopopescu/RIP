import pymysql
pymysql.install_as_MySQLdb()


class Connection:
    def __init__(self, user, password, db, host='localhost'):
        # Сохраняем параметры соединения
        self.user = user
        self.password = password
        self.db = db
        self.host = host
        self._connection = None

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        """
        Открытие соединения
        """
        if not self._connection:
            self._connection = pymysql.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.db
            )

    def disconnect(self):
        """
        Закрытие соединения
        """
        if self._connection:
            self._connection.close()