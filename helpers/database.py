import sqlite3


class DatabaseManager():
    def __init__(self, database_file:str) -> None:
        self.database_file = database_file
        self.connection = None
        try:
            self.connection = sqlite3.connect(database_file)
        except sqlite3.Error as e:
            print(e)
        
    def create_table(self, executer: str):
        try:
            self.cursor = self.connection.cursor()
            self.cursor.execute(executer)
            self.connection.commit()
        except sqlite3.Error as e:
            print(e)
    def insert_react_value(self, guild_id: str, ammount: int):
        try:
            self.cursor = self.connection.cursor()
            base_command = """INSERT OR REPLACE INTO config_settings(guild_id, react_count)
                            VALUES(?, ?)"""
            self.cursor.execute(base_command, (guild_id, ammount))
            self.connection.commit()
        except sqlite3.Error as e:
            print(e)
