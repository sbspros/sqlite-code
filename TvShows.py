from common.BaseClass import BaseClass
import traceback

__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"

class SQLCreateError(Exception):
    def __init__(self):
        self.msg = 'Failed to create SQL Table'
        super().__init__(self.msg)


class TvShows():

  def __init__(self,bc:BaseClass):
    self._show_name=None
    self._season=None
    self._bc=bc
    
  def is_created(self,conn):
    """SELECT EXISTS (
    SELECT 
        name
    FROM 
        sqlite_schema 
    WHERE 
        type='table' AND 
        name='Customers'
    );"""
    return False

  @property
  def show_name(self):return self._show_name

  @property
  def season(self):return self._season

  @show_name.setter
  def show_name(self,show_name):self._show_name=show_name

  @season.setter
  def season(self,season):self._season=season

  def create_table(self,conn,bc:BaseClass):
    try:
      sql_create_table = """ CREATE TABLE IF NOT EXISTS tv_show (
                                          id integer PRIMARY KEY,
                                          show_name text NOT NULL,
                                          season integer NOT NULL,
                                          complete integer DEFAULT 0
                                      )x; """
      conn.execute(sql_create_table)
    except:
      bc.log.error("\t"+":"+traceback.format_exc())
      raise SQLCreateError
