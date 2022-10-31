from common.BaseClass import BaseClass
from models.Episodes import Episodes
from models.Seasons import Seasons
from models.TvShows import TvShows
from models.PlexSections import PlexSections
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
  Create/List data from a show view
  
  It links PlexSection, Tv Show, Seasons and Episode from a local database
"""
class ShowList():
  view_name='show_list'
  def __init__(self,bc:BaseClass,conn:SQLConnection):
    self._bc=bc
    self._conn=conn
    if self.is_created()!=1:
      self.create_view()
  """
    Check to see if the view has been created
  """
  def is_created(self):
    return self._conn.local_exec("""SELECT EXISTS (
    SELECT 
        name
    FROM 
        sqlite_schema 
    WHERE 
        type='view' AND 
        name='{view}'
    );""".format(view=ShowList.view_name))
  
  """
    Reads all records from the view
  """
  def read_list_show(self):
    return self._conn.local_exec(""" SELECT * FROM {view}; """.format(view=ShowList.view_name))
  
  """
    Creates the view if it does not exists
  """
  def create_view(self):
    self.create_base_tables()
    return self._conn.local_exec(""" CREATE VIEW IF NOT EXISTS {view_name} AS SELECT  section_name, show_name, season_num, episode_num,status
        FROM plex_sections AS P
        JOIN tv_shows AS T
          ON P.id =T.sec_id
        JOIN seasons AS S
          ON T.id = S.show_id
        JOIN episodes AS E
          ON S.id = E.season_id ; """.format(view_name=ShowList.view_name))

  """
    Creates base tables the view is made of if it doesn't exists
  """
  def create_base_tables(self): 
    section = PlexSections(self._bc,self._conn)
    if section.is_created()!=1:
      section.create_table()

    shows = TvShows(self._bc,self._conn)
    if shows.is_created()!=1:
      shows.create_table()

    seasons = Seasons(self._bc,self._conn)
    if seasons.is_created()!=1:
      seasons.create_table()

    episodes = Episodes(self._bc,self._conn)
    if episodes.is_created()!=1:
      episodes.create_table()