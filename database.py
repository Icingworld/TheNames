import sqlite3

class Database:
    def __init__(self) -> None:
        self.__name = ""
        self.__state = False
        self.__conn = sqlite3.connect(self.__name)
        self.__cursor = self.__conn.cursor()

    def __del__(self) -> None:
        self.__conn.close()

    def setName(self, name:str) -> None:
        self.__name = name

    def connect(self) -> bool:
        self.__conn = sqlite3.connect(self.__name)
        self.__cursor = self.__conn.cursor()
        self.__state = self.__conn.in_transaction
        return self.__state

    def state(self) -> bool:
        self.__state = self.__conn.in_transaction
        return self.__state
    
    def exec(self, command:str) -> None:
        self.__cursor.execute(command)
        self.__conn.commit()

    def create(self, command:str) -> None:
        self.exec(command)

    def insert(self, command:str) -> None:
        self.exec(command)

    def update(self, command:str) -> None:
        self.exec(command)

    def delete(self, command:str) -> None:
        self.exec(command)

    def search(self, command:str) -> list:
        self.__cursor.execute(command)
        return self.__cursor.fetchall()
    
    def close(self) -> None:
        self.__del__()