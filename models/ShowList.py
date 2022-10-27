from common.BaseClass import BaseClass
from model.Episodes import Episodes
from model.Seasons import Seasons
from model.TVShows import TVShows
from model.PlexSections import PlexSections


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
  def __init__(self,bc:BaseClass):
    if self.is_create()!=1;
      self.create_view()
    
  def is_created(self,conn):
    """SELECT EXISTS (
    SELECT 
        name
    FROM 
        sqlite_schema 
    WHERE 
        type='view' AND 
        name='{view}'
    );""".format(view=cls.view_name)
    return conn.execute(sql_create_table)

  @property
  def show_name(self):return self._show_name

  @property
  def season(self):return self._season

  @show_name.setter
  def show_name(self,show_name):self._show_name=show_name

  @season.setter
  def season(self,season):self._season=season

  def create_view(self,conn,bc:BaseClass):
    try:
      self.create_base_tables()
      sql_create_table = """ CREATE VIEW IF NOT EXISTS AS ...; """
      conn.execute(sql_create_table)
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

      
