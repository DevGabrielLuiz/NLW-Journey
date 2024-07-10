from typing import Dict, Tuple, List
from sqlite3 import Connection

class EmailsToInviteRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_email(self, email_info: dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            INSERT INTO emails_to_invite (id, trip_id, email)
            VALUES (?, ?, ?)
            ''',
            (
                email_info["id"],
                email_info["trip_id"],
                email_info["email"],
            )
        )
        self.__conn.commit()

        
    def find_emails_from_trip(self, trip_id: str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''SELECT * FROM emails_to_invite WHERE trip_id = ?''', (trip_id,)
        )
        trip = cursor.fetchall() # "fetchone" pega um unico elemento, "fetchall" e "fetchmany" pegam mais de um 
        return trip
   