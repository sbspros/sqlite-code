from common.BaseClass import BaseClass
from SqlConnection import SQLConnection
import os
import inspect

__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"
""" A ulitity to find and update plex media"""

if __name__ == '__main__':
    bc=BaseClass('config.ini')
    conn=SQLConnection(bc,'TvShows','db/media.db')
    if conn.is_created():
        print("Table has already be created")
    else:
        conn.create_table()
        print("Table has been created")
