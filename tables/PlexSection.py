
from models.PlexSection import PlexSection
from models.Tables import Tables as LocalTables

class PlexSection(LocalTables):
  database='plex_media'
  table='section'
  def __init__(self):
    self._sections=[]
    
   def create_table(self):
      self.is_create(
      sql_str=""
      self.exec_sql(sql_str)
    
   def insert(self):
      sql_str=""
      self.exec_sql(sql_str)
    
   def delete(self):
      sql_str=""
      self.exec_sql(sql_str)
     
   def update(self):
      sql_str=""
      self.exec_sql(sql_str)
    
   def current_date(self):
      sql_str=""
      self.exec_sql(sql_str)