from common.BaseClass import BaseClass,AppError
from model.Episodes import Episodes
from model.Seasons import Seasons
from model.TVShows import TVShows
from model.PlexSections import PlexSections
from common.SqlConnection import SqlConnection,SQLExecError
from table.ShowList import ShowList as tableShowList
import traceback

__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"

class ShowList():
  view_name='show_list'
  def __init__(self,bc:BaseClass,conn:SqlConnection):
    self._conn=conn
    if self.is_create()!=1;
      self.create_view()
    
  def is_created(self):
    create_flag=0
    """SELECT EXISTS (
    SELECT 
        name
    FROM 
        sqlite_schema 
    WHERE 
        type='view' AND 
        name='{view}'
    );""".format(view=ShowList.view_list)
    try:
      create_flag=self._conn.execute(sql_create_table)
    except SQLExecError:
      raise SQLError
     except:
      bc.log.error("\t"+":"+traceback.format_exc())
      raise AppError
    final return create_flag      
  
  
  def read_list_show(self):
    show_list=[]
    try:
      table_list = tableShowList(self._bc)
      select_query = """ SELECT * FROM {view}; """.format(view=ShowList.view_name)
      show_list= table_list.__print__(conn.execute(select_query))
    except SQLExecError:
      raise SQLError
     except:
      bc.log.error("\t"+":"+traceback.format_exc())
      raise AppError
    final return show_list      
  
  def create_view(self,conn,bc:BaseClass):
    try:
      self.create_base_tables()
      sql_create_view = """ CREATE VIEW IF NOT EXISTS  {view} AS ...; """.format(view=ShowList.view_name)
      conn.execute(sql_create_view)
    except:
      bc.log.error("\t"+":"+traceback.format_exc())
      raise SQLCreateError
      
  def create_base_tables(self,conn,bc:BaseClass): 
    section = PlexSections(self._bc)
    if section.is_create()!=1;
      section.create_table()

    shows = TvShows(self._bc)
    if shows.is_create()!=1;
      shows.create_table()

    seasons = Seasons(self._bc)
    if seasons.is_create()!=1;
      seasons.create_table()

    episodes = Episodes(self._bc)
    if episodes.is_create()!=1;
      episodes.create_table()

      
