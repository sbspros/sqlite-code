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

"""
 Episode is the local copy of the episode data
"""
class Episodes():
  table_name='episodes'
  def __init__(self,bc:BaseClass,conn:SqlConnection):
    self._conn=conn
    if self.is_create()!=1;
      self.create_table()
    
  def is_created(self,conn):
    return self._conn.local_exec"""SELECT EXISTS (
    SELECT 
        name
    FROM 
        sqlite_schema 
    WHERE 
        type='table' AND 
        name='{table}'
    );""".format(table=Episodes.table_name))
  
  def create_table(self,conn,bc:BaseClass):
    return self._conn.local_exec""" CREATE TABLE IF NOT EXISTS  {table} AS ...; """.format(table=Episodes.table_name))
