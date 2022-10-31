from common.BaseClass import BaseClass
from common.SQLConnection import SQLConnection
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
    );""".format(table=Episodes.table_name))
  
  def create_table(self):
    return self._conn.local_exec( """ CREATE TABLE IF NOT EXISTS  {table_name} ( 
      id INT PRIMARY KEY,
      season_id INT NOT NULL,
      episode_num INT NOT NULL,
      status TEXT DEFAULT 'Needed',
      created_date TEXT NOT NULL, 
      modification_date TEXT NOT NULL ) WITHOUT ROWID
      ; """.format(table_name=Episodes.table_name))
