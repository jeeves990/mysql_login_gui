"""
    MySqlConnection.py
"""
import sys
from PyQt5 import (QtWidgets as qtw,
                   QtGui as qtg,
                   QtCore as qtc,
                   QtSql as sql, )
# import MySqlConnection_w_qt as db_conn_dlg
# import MySQLdb as mdb


class MainWindow(qtw.QDialog):
    def __init__(self):
        super().__init__()

        self.title="PyQt5 Database Connection"
        self.resize(400, 300)
        self.move(200,500)

        self.InitUi()

        self.show()

    def InitUi(self):
        button = qtw.QPushButton('Db Connection', self)
        # button.setGeometry(1278,100, 200,50)
        button.clicked.connect(self.DBConnection)
        vbox = qtw.QVBoxLayout(self)
        vbox.addWidget(button)
        self.setWindowTitle(self.title)


    def DBConnection(self):
        try:
            # self.db = sql.connect(host = "localhost", user = "root",
            #                  db="mysql", password='j33ves99',
            #                  port=3305)
            self.db = sql.QSqlDatabase.addDatabase('QMYSQL')
            self.db.setHostName('127.0.0.1')
            self.db.setDatabaseName('calendar_app')
            self.db.setUserName('root')
            self.db.setPassword('j33ves99')
            self.db.setPort(3305)
            if self.db.open(user='sherril', password='j33ves99'):
                print('success')
                qtw.QMessageBox.about(self, 'Connection', 'successful')
                return True
            else:
                raise Exception('database did not open')
        except Exception as e:
            print('Failed to Connect', str(e))
            qtw.QMessageBox.about(self, 'connection', 'Failed to Connect')
            return False

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())

