from common.BaseClass import BaseClass
import traceback

__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"

class Episodes():
  table_name='episodes'
  def __init__(self,bc:BaseClass):
    if self.is_create()!=1;
      self.create_table()
    
  def is_created(self,conn):
    return conn.execute("""SELECT EXISTS (
    SELECT 
        name
    FROM 
        sqlite_schema 
    WHERE 
        type='table' AND 
        name='{table}'
    );""".format(table=Episodes.table_name))
  
  def create_table(self,conn,bc:BaseClass):
    try:
      self.create_base_tables()
      sql_create_table = """ CREATE TABLE IF NOT EXISTS  {table} AS ...; """.format(table=Episodes.table_name)
      conn.execute(sql_create_table)
    except:
      bc.log.error("\t"+":"+traceback.format_exc())
      raise SQLCreateError
      
