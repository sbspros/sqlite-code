import sqlite3
from common.BaseClass import BaseClass
import traceback

__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"


class ConnectFailed(Exception):
    def __init__(self):
        self.msg = 'Media Finder failed to initialize'
        super().__init__(self.msg)


class SQLConnection():

    def __init__(self,bc:BaseClass,business_object:str,database:str):
        self._bc=bc
        try:
            ## Load the clase in
            class_name=business_object
            bus_class = __import__(class_name, globals(), locals(), [], 0)
            self._bus_obj = getattr(bus_class, business_object)
            self._conn=sqlite3.connect(database)
        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
            raise ConnectFailed

    ## Does the table exists
    def is_created(self):
        return self._bus_obj.is_created(self._bus_obj,self._conn)

    ## Create table
    def create_table(self):
        try:
            self._bus_obj.create_table(self._bus_obj,self._conn,self._bc)
        except SQLCreateError as e:
            pass
