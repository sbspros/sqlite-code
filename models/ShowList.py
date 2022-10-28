from common.BaseClass import BaseClass
from model.Episodes import Episodes
from model.Seasons import Seasons
from model.TVShows import TVShows
from model.PlexSections import PlexSections
from common.SqlConnection import SqlConnection
from table.ShowList import ShowList as tableShowList
import traceback

__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"

"""
  Create/List data from a show view
  
  It links PlexSection, Tv Show, Seasons and Episode from a local database
"""
class ShowList():
  view_name='show_list'
  def __init__(self,bc:BaseClass,conn:SqlConnection):
    self._conn=conn
    if self.is_create()!=1;
      self.create_view()
  """
    Check to see if the view has been created
  """
  def is_created(self):
    sql_table_check="""SELECT EXISTS (
    SELECT 
        name
    FROM 
        sqlite_schema 
    WHERE 
        type='view' AND 
        name='{view}'
    );""".format(view=ShowList.view_list)
    return self._conn.local_exec(sql_table_check)
  
  """
    Reads all records from the view
  """
  def read_list_show(self):
    show_list=[]
    select_query = """ SELECT * FROM {view}; """.format(view=ShowList.view_name)
    return self._conn.local_exec(select_query)
  
  """
    Creates the view if it does not exists
  """
  def create_view(self):
    self.create_base_tables()
    sql_create_view = """ CREATE VIEW IF NOT EXISTS  {view} AS ...; """.format(view=ShowList.view_name)
    return self._conn.local_exec(sql_create_view)

  """
    Creates base tables the view is made of if it doesn't exists
  """
  def create_base_tables(self): 
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

      
