"""
    qt_template.py
        template for creating qt scripts
    Mastering Gui Programming with Python
    Chapter 2: rehash
"""
import sys
import os
from PyQt5 import (QtWidgets as qtw,
                   QtGui as qtg,
                   QtCore as qtc,
                   QtSql as sql,
                   uic, )

import pymysql
# import MySQLdb as mdb
# import MySQLdb.connections
from MySqlConnection_ui import Ui_MySql_connection_ui

DIRNAME = os.path.dirname(sys.argv[0])
APPNAME = 'calendar_app'
# APPNAME = os.path.basename(sys.argv[0]).split('.')[0]
COMPANY_NAME = 'MCO_Technical_Services'
APPGEOMETRY = 'App Geometry'
DB_NAME = 'event_calendar'

"""
    class MainWindow(qtw.QMainWindow, Ui_MySql_connection_ui):
    may be used as a connection facility variably based on
    -1- a connection string like 
        "'host="localhost", user="sherril", password="j33ves99", \
        server_type="MySQL", database="event_calendar", port=3305'
    -- or --
    -2- an ini file.
    
    If the ini file parameter is not passed to the constructor, there is a default
    ini file based on  os.path.join(DIRNAME, APPNAME) + ".ini".
    
    If the connection string parameter IS NOT passed, the connection string
    properties are raised from the ini file.
      
    These options passed as parameters to the MainWindow.__init__ constructor.    
"""
class MainWindow(qtw.QMainWindow, Ui_MySql_connection_ui):

    submitted = qtc.pyqtSignal(str)
    events = {}
    INI_FILENAME = os.path.join(DIRNAME, APPNAME) + ".ini"
    CLASSINIFILENAME = 'ini filename'
    CLASSGEOMETRY = APPNAME+'_geometry'
    APPVALUES = APPNAME+'_values'
    left = 800
    top = 150
    width = 300
    height = 450
    db = None
    db_conn_values = 'Database_connection_values'

    def __init__(self, connection_string = None, ini_filename = None):
        super().__init__()
        if ini_filename:
            self.INI_FILENAME = ini_filename
        else:
            self.INI_FILENAME = self.INI_FILENAME

        """  
            self.settings provides geometry and, if the connection_string is None,
            provides connection properties.
        """
        self.settings = qtc.QSettings(self.INI_FILENAME, qtc.QSettings.IniFormat)

        self.setupUi(self)
        if connection_string:
            self.connection_string = self.parse_connection_string(connection_string)
        else:
            self.read_values_from_settings()
        self.title="Calendar_app Database Connection"
        self.InitUi()
        self.restore_app_values()

        self.show()

    def InitUi(self):

        self.setWindowTitle(self.title)
        self.connect_signals()

    def connect_signals(self):
        self.action_Connect.triggered.connect(self.DBConnection)
        self.action_Disconnect.triggered.connect(self.db_disconnect)

    def save_login_state(self):
        pass

    def login_to_database(self):
        pass

    def read_state_xml(self):
        pass

    def db_disconnect(self):

        # self.action_Connect.setChecked(False)
        self.host_lbl.text=""
        self.user_edit.text=""
        self.database_edit.text=""
        self.server_type_edit.text=""
        self.password_edit.text=""
        self.port_edit.text=""
        pass

    def DBConnection(self):

        self.action_Connect.setChecked(False)

        host_ = self.host_edit.text()
        user_ = self.user_edit.text()
        db_ = self.database_edit.text()
        server_type_ = self.server_type_edit.text()
        pwd_ = self.password_edit.text()
        port_ = int(self.port_edit.text())

        txt_ = ""
        text = "{0} is a required field!"
        if not host_:
            txt_ = text.format("Host")
            self.host_lbl.setFocus()
        elif not user_:
            txt_ = text.format("User")
            self.user_lbl.setFocus()
        elif not server_type_:
            txt_ = text.format("Server")
            self.server_type_edit.setFocus()

        # if not db_:
        #     qtw.QMessageBox('Database is a required field!')
        #     self.host_lbl.setFocus()
        #     return False

        elif not pwd_:
            txt_ = text.format("Password")
            self.password_edit.setFocus()
        elif not port_:
            txt_ = text.format("Port")
            self.port_lbl.setFocus()

        if txt_:
            msgbox=qtw.QMessageBox()
            msgbox.setText(txt_)
            msgbox.setWindowTitle(txt_)
            msgbox.setStandardButtons(qtw.QMessageBox.Ok)
            msgbox.exec_()
            self.statusbar.showMessage(txt_)
            return False

        try:
            self.db = pymysql.connect( \
                host=host_, \
                database=DB_NAME, \
                user=user_, \
                port=port_, \
                passwd=pwd_)

            print(self.db.__str__())
            try:
                if self.db:
                    print('success')
                    qtw.QMessageBox.about(self, 'Connection', 'successful').exec_()
                    return True
                else:
                    raise Exception('database did not open')
            finally:
                if self.db.open:
                    self.db.close()
                else:
                    pass
                return

        # except self.db.Error as e:
        #     qtw.QMessageBox.about(self, 'connection', 'Failed to Connect')
        #     return False
        except Exception as e:
            # for arg in e.args:
            #     print(arg)
            msg = f"Failed to Connect for unknown reason.\n\t \
                Exception type is {type(e)}\n\t" \
                "Exception arguments are {1}\n\tAll of Exception is {e}"
            # msg.format(type(e), e.args, e)
            qtw.QMessageBox.critical(self, "Connection has failed!", msg)

        finally:
            if self.db:
                self.write_settings_from_values()
                try:
                    self.db.close()
                except:
                    pass


    """------------settings helper methods------------"""
    """
        def restore_app_values(self):
        uses QWidget's restoreGeometry to get the saved app
        geometry from the QSettings ini file and to restore
        the app geometry based on that.
    """
    def restore_app_values(self):
        self.kill_groups()
        self.settings.beginGroup(APPGEOMETRY)
        try:
            ara = self.settings.value(self.CLASSGEOMETRY)
            if not ara:
                self.setGeometry(self.left, self.top, self.width, self.height)
                return
            else:
                # ara = ara.toByteArray()
                self.restoreGeometry(ara)
        finally:
            self.settings.endGroup()



    """
            def closeEvent(self, _event_):
            uses QWidget's saveGeometry to save the app geometry
            to the QSettings ini file.
            -- This is a reintroduce of the parent's "closeEvent" method --
    """
    def closeEvent(self, _event_):

        reply = qtw.QMessageBox.question(
            self,
            "Exit Application",
            f"Do you wish to close the {APPNAME} application?",
            qtw.QMessageBox.Yes | qtw.QMessageBox.No,
            qtw.QMessageBox.No
        )
        if reply == qtw.QMessageBox.Yes:
            self.kill_groups()

            self.settings.beginGroup(APPGEOMETRY)
            try:
                self.settings.setValue(self.CLASSGEOMETRY, self.saveGeometry())
            finally:
                self.settings.endGroup()

            self.settings.beginGroup(self.APPVALUES)
            try:
                self.settings.setValue(self.CLASSINIFILENAME, self.INI_FILENAME)
            finally:
                self.settings.endGroup()

            _event_.accept()
        else:
            _event_.ignore()

    """
        def kill_groups(self):
        kill "all" groups "queued up" in the self.settings group list
    """
    def kill_groups(self):
        while self.settings.group():
            self.settings.endGroup()

    """----------------connection string methods----------------"""
    def parse_connection_string(self, connection_string):
        self.host = None
        self.user = None
        self.password = None
        self.server_type = None
        self.database = None
        self.port = None

        disallowed_characters = "\"  "

        for character in disallowed_characters:
            connection_string = connection_string.replace(character, '')

        list = connection_string.split(',')
        for itm in list:
            key, value = itm.split('=')
            print('key:', key, '\t\tvalue:', value)
            if key.lower().strip() == 'host':
                self.host = value.strip()
            elif key.lower().strip() == 'user':
                self.user = value.strip()
            elif key.lower().strip() == 'password':
                self.password = value.strip()
            elif key.lower().strip() == 'server_type':
                self.server_type = value.strip()
            elif key.lower().strip() == 'database':
                self.database = value.strip()
            elif key.lower().strip() == 'port':
                self.port = value.strip()
        self.populate_edits()

    def populate_edits(self):
        self.host_edit.setText(self.host)
        self.user_edit.setText(self.user)
        self.password_edit.setText(self.password)
        self.server_type_edit.setText(self.server_type)
        self.database_edit.setText(self.database)
        self.port_edit.setText(self.port)



    def read_values_from_settings(self):
        self.kill_groups()
        self.settings.beginGroup(self.db_conn_values)
        try:
            self.host = self.settings.value('Host')
            self.user = self.settings.value('User')
            self.password = self.settings.value('Password')
            self.server_type = self.settings.value('Server_type')
            self.database = self.settings.value('Database_name')
            self.port = self.settings.value('Port')
            self.populate_edits()
        finally:
            self.settings.endGroup()

    def write_settings_from_values(self):
        self.kill_groups()
        self.settings.beginGroup(self.db_conn_values)
        try:
            self.settings.setValue('Host', self.host_edit.text())
            self.settings.setValue('User', self.user_edit.text())
            self.settings.setValue('Password', self.password_edit.text())
            self.settings.setValue('Server_type', self.server_type_edit.text())
            self.settings.setValue('Database_name', self.database_edit.text())
            self.settings.setValue('Port', self.port_edit.text())
        finally:
            self.settings.endGroup()
        pass


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    conn_string = 'host="localhost", user="sherril", password="j33ves99", \
                        server_type="MySQL", database="event_calendar", port=3305'
    # conn_string = None
    # conn_string = None
    # username = input("Choose a username: ")
    # print("Your username is: " + username)
    mw = MainWindow( )
    # mw = MainWindow(connection_string = conn_string)
    sys.exit(app.exec())

d