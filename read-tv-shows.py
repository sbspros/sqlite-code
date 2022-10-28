from common.BaseClass import BaseClass
from common.SqlConnection import SqlConnection
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

if __name__ == '__main__':
    
    ## Start app base class with ini read and logs
    bc=BaseClass('config.ini')
    try:
        conn=SqlConnection('db/media.db')
        shows=ShowList(bc,conn)
        if not shows.is_created():
            show.create_veiw()
            print("View has been created")
        print(shows.read_list_show())
    except AppException as err:
        print('Application has stopped, please check error logs')
    except :
        bc.log.error("\t:"+traceback.format_exc())
    final:
        print('Application has ended')
    return 0
