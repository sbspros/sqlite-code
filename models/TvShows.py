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

class TvShows():
  table_name='tv_shows'
  def __init__(self,bc:BaseClass,conn:SqlConnection):
    self._conn=conn
    if self.is_create()!=1;
      self.create_table()
    
  def is_created(self,conn):
    sql_table_check="""SELECT EXISTS (
    SELECT 
        name
    FROM 
        sqlite_schema 
    WHERE 
        type='table' AND 
        name='{table}'
    );""".format(table=TvShows.table_name)
    try:
      create_flag=self._conn.execute(sql_table_check)
    except SQLExecError:
      raise SQLError
     except:
      bc.log.error("\t"+":"+traceback.format_exc())
      raise AppError
    final return create_flag   
  
  def create_table(self):
    create_flag=0
    sql_create_table = """ CREATE TABLE IF NOT EXISTS  {table} AS ...; """.format(table=TvShows.table_name)
    try:
      create_flag=self._conn.execute(sql_create_table)
    except SQLExecError:
      raise SQLError
     except:
      bc.log.error("\t"+":"+traceback.format_exc())
      raise AppError
    final return create_flag        