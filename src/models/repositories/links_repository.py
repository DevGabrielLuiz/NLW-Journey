from typing import Dict, Tuple, List
from sqlite3 import Connection

class LinksToInviteRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_link(self, link_info: dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            INSERT INTO links (id, trip_id, link)
            VALUES (?, ?, ?)
            ''',
            (
                link_info["id"],
                link_info["trip_id"],
                link_info["link"],
            )
        )
        self.__conn.commit()

        
    def find_links_from_trip(self, trip_id: str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''SELECT * FROM links WHERE trip_id = ?''', (trip_id,)
        )
        trip = cursor.fetchall() # "fetchone" pega um unico elemento, "fetchall" e "fetchmany" pegam mais de um 
        return trip
   