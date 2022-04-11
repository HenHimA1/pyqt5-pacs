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
        self.connection.row_factory = sqlite3.Row
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
        query = f"SELECT * FROM {table}"
        records = self.execute(query).fetchall()
        return [{k: item[k] for k in item.keys()} for item in records]

    def browse(self, table, field, data):
        query = f"SELECT * FROM {table} WHERE {field}='{data}'"
        records = self.execute(query).fetchall()
        return [{k: item[k] for k in item.keys()} for item in records]

    def delete(self, table, field, data):
        query = f"DELETE FROM {table} WHERE {field}='{data}'"
        self.execute(query)
        self.connection.commit()
        return self.cursor.rowcount
