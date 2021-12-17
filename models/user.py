import sqlite3

from PyQt5.QtWidgets import QMessageBox

from ui.pyUI.scenes import login, signUp
from ui.pyUI.scenes.signUp import *
from ui.pyUI.scenes.login import *

class User:
    def __init__(self,id,username,password,email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def addNewUser(self,frameName):
        conn = sqlite3.connect('C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\db\RESCSYdb.db')
        result = conn.execute('''SELECT username,email FROM users''')
        for i in result:
            if i[0] == self.username or i[1]==self.email:
                msgBox = QMessageBox.warning(frameName, "WARNING", "Username or Email is ALREADY EXIST!")
                msgBox.execute()
            else:
                conn.execute('''INSERT INTO users VALUES(?,?,?)''', (self.username, self.password, self.email))
                conn.commit()
        conn.close()

    def getUserNameById(self):
        conn = sqlite3.connect('C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\db\RESCSYdb.db')
        result = conn.execute('''SELECT username  FROM users WHERE user_id=(?)''', self.id)
        username = result.fetchall()[0][0]
        print(username)
        conn.close()
        return username


    def getUserIDByUsername(self):
        conn = sqlite3.connect('C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\db\RESCSYdb.db')
        result = conn.execute('''SELECT user_id  FROM users WHERE username=(?)''', self.username)
        username = result.fetchall()[0][0]
        print(username)
        conn.close()
        return username


    def loginCheck(self,lineEdit_Username,lineEdit_Password,loginFrame):
        print("login button clicked")
        username = lineEdit_Username.text()
        password = lineEdit_Password.text()

        connection = sqlite3.connect("C:/Users\onursercanyilmaz\Documents\GitHub\RecSy\db\RESCSYdb.db")

        result = connection.execute('''SELECT * FROM users WHERE username=? and password=?''', (username, password))

        if ((len(result.fetchall()) > 0)):
            print("USER FOUND")
            mainScene = screenManager.MainMenu()
            uik = mainScene.ui
            uik.setupUi(mainScene)
            mainScene.show()
            loginFrame.hide()
        else:
            print("USER NOT FOUND")
            msgBox = QMessageBox.warning(loginFrame, "WARNING", "Your Password INCORRECT!")
            msgBox.execute()





