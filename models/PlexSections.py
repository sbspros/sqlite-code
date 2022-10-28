from common.BaseClass import BaseClass,AppError
from common.SqlConnection import SqlConnection,SQLExecError,SQLError
import traceback

__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"

class PlexSections():
  table_name='plex_sections'
  def __init__(self,bc:BaseClass):
    if self.is_create()!=1;
      self.create_table()
    
  def is_created(self,conn):
    return self._conn.local_exec("""SELECT EXISTS (
    SELECT 
        name
    FROM 
        sqlite_schema 
    WHERE 
        type='table' AND 
        name='{table}'
    );""".format(table=PlexSection.table_name))
  
  def create_table(self,conn,bc:BaseClass):
    return self._conn.local_exec( """ CREATE TABLE IF NOT EXISTS  {table} AS 
    	id INT PRIMARY KEY,
      section_name TEXT NOT NULL,
	    last_update INT DEFAULT 0,
      created_date TEXT NOT NULL 
      modification_date TEXT NOT NULL 
      ; """.format(table=ShowList.table_name))
