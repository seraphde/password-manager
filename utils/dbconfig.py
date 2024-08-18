import mysql.connector

from rich import print as printic
from rich .console import Console
console = Console()

def dbconfig ():
    try: 
         db = mysql.connector.connect(
            host= 'local',
            username= 'pm',
            passwd= 'password'
         )
    except Exception as e:
         console.print_exception(show_locals=True)
         
    return db
