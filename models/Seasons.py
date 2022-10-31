from common.BaseClass import BaseClass,AppException
from common.SQLConnection import SQLConnection,SQLExecError,SQLError
import traceback

__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"

"""
   Seasons is the seasons information stored locally in the database 
"""

class Seasons():
  table_name='seasons'
  def __init__(self,bc:BaseClass,conn:SQLConnection):
    self._conn=conn
    if self.is_created()!=1:
      self.create_table()
    
  def is_created(self):
     return self._conn.local_exec("""SELECT EXISTS (
    SELECT 
        name
    FROM 
        sqlite_schema 
    WHERE 
        type='table' AND 
        name='{table}'
    );""".format(table=Seasons.table_name))
  
  def create_table(self):
    return self._conn.local_exec( """ CREATE TABLE IF NOT EXISTS  {table_name} ( 
      id INT PRIMARY KEY,
      show_id INT NOT NULL,
      season_num INT NOT NULL,
      active INT DEFAULT 0,
      created_date TEXT NOT NULL, 
      modification_date TEXT NOT NULL ) WITHOUT ROWID
      ; """.format(table_name=Seasons.table_name))
