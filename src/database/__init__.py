from copyreg import constructor
import sqlite3

activeDatabase = 0

class Database:
    def __init__(self, database, schema):
        self.database = database
        self.schema = schema
        self.init_connection()

    def init_schema(self):
        sql_as_string = self.schema.read()
        self.cursor.executescript(sql_as_string)
        self.connection.commit()
        global activeDatabase
        activeDatabase = "Hello"

    def init_connection(self):
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        self.init_schema()

    def execute(self, query):
        return self.cursor.execute(query)

    def create(self, table, values):
        columns = ', '.join(values.keys())
        placeholders = ', '.join('?' * len(values))
        query = f'INSERT INTO {table} ({columns}) VALUES ({placeholders})'
        list_value = [int(x) if isinstance(x, bool) else x for x in values.values()]
        self.cursor.execute(query, list_value)
        self.connection.commit()
        return self.cursor.lastrowid

    def read(self, table):
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        query = f"SELECT * FROM {table}"
        records = self.execute(query).fetchall()
        list_record = [{k: item[k] for k in item.keys()} for item in records]
        return list_record
