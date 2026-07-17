import psycopg2

class PgManager:
    def __init__(self, db_name, user, password, host, port=5432):
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = self.create_connection()
        self.cursor = self.connection.cursor()

    def create_connection(self):
        return psycopg2.connect(
            dbname=self.db_name,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
        )
    
    def execute_query(self, query, params=None):
        if params is None:
            params = ()

        self.cursor.execute(query, params)
        self.connection.commit()

        if self.cursor.description:
            return self.cursor.fetchall()
        return None
    
    def execute_transaction(self, queries):
        try:
            for query, params in queries:
                self.cursor.execute(query, params)

            self.connection.commit()
            return True

        except Exception as error:
            self.connection.rollback()
            print("Transaction error:", error)
            return False
    
    def close_connection(self):
        self.cursor.close()
        self.connection.close()    