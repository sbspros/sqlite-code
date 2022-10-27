from common.BaseClass import BaseClass
from models.ShowList import ShowList
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
    shows=ShowList(bc,'db/media.db')
    if !shows.is_created():
        show.create_veiw()
        print("View has been created")
    print(shows.list_show())
