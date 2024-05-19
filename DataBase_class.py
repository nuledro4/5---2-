from flask import Flask, request, render_template
from flask import render_template_string
from Exceptions import SearchExeption
from app import app
import sqlite3


class DataBase:
    from User_class import User

    def __init__(self, path):
        self.path = path
        self._connection = sqlite3.connect("instance/userInfo.db")
        self._cursor = self._connection.cursor()

    def addUser(self, user: User):
        res = self._checkForDif(user)
        if res != SearchExeption and not res:
            try:
                self._cursor.execute(
                    "INSERT INTO userInfo (username, mail, password, is_logined) VALUES (?, ?, ?, ?)",
                    (f"{user.name}", f"{user.mail}", f"{user.password}", True),
                )
                self._connection.commit()
                self._connection.close()
                return True
            except:
                print("Ошибка при добавлении ползователя в базу данных")
                return False
        else:
            return False

    def changeLoginedState(self, user: User):
        res = self._checkForLog(user)
        if res != SearchExeption and res:
            try:
                """ self._cursor.execute(
                    "UPDATE userInfo SET is_logined = True WHERE username = ? OR mail = ?",
                    (f"{user.name}", f"{user.mail}"),
                )
                self._connection.commit()
                self._connection.close() """
                return True
            except:
                print("При авторизации произошла ошибка")
                return False
        elif res != SearchExeption and not res:
            return False
        else:
            return SearchExeption

    def _checkForDif(self, user: User):
        try:
            self._cursor.execute(
                "SELECT username, mail FROM userInfo WHERE username = ? OR mail = ?",
                (f"{user.name}", f"{user.mail}"),
            )
            results = self._cursor.fetchall()

            if len(results) != 0:
                return True
            else:
                return False
        except:
            return SearchExeption

    def _checkForLog(self, user: User):
        import hashlib

        user.password = hashlib.md5(bytes(user.password, encoding="utf8")).hexdigest()
        try:
            self._cursor.execute(
                "SELECT username, mail FROM userInfo WHERE (username = ? OR mail = ?) AND password = ?",
                (f"{user.name}", f"{user.mail}", f"{user.password}"),
            )
            results = self._cursor.fetchall()

            if len(results) != 0:
                return True
            else:
                return False
        except:
            return SearchExeption
