import sqlite3
from common.BaseClass import BaseClass,AppException
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
        
class SQLExecError(Exception):
    def __init__(self):
        self.msg = 'SQL query failed to run'
        super().__init__(self.msg)

class  SQLError (Exception):
    def __init__(self):
        self.msg = 'SQL - General Error'
        super().__init__(self.msg)       
        
class SQLConnection():

    def __init__(self,bc:BaseClass,database:str):
        self._bc=bc
        try:
            ## Load the clase in
            self._conn=sqlite3.connect(database)
        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
            raise AppException

    def local_exec(self,query):
        create_flag=None
        self._bc.log.info("\t:"+query)
        try:
            cur = self._conn.cursor()
            cur.execute(query)
            create_flag = cur.fetchall()
            for row in create_flag:
                self._bc.log.info("SQL returns {value}".format(value=row[0]))

        except SQLExecError:
            self._bc.log.error("\t:"+query)
            raise SQLError
        except:
            self._bc.log.error("\t:"+query)
            self._bc.log.error("\t:"+traceback.format_exc())
            raise AppError
        finally:
            return create_flag      
            
