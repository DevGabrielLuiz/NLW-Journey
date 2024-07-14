from typing import Dict, Tuple, List
from sqlite3 import Connection

class ActivitiesRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_email(self, acitivity_info: dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            INSERT INTO acitivities (id, trip_id, title, occurs_at)
            VALUES (?, ?, ?, ?)
            ''',
            (
                acitivity_info["id"],
                acitivity_info["trip_id"],
                acitivity_info["title"],
                acitivity_info["occurs_at"],
            )
        )
        self.__conn.commit()

        
    def find_activities_from_trip(self, trip_id: str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''SELECT * FROM activities WHERE trip_id = ?''', (trip_id,)
        )
        activities = cursor.fetchall() # "fetchone" pega um unico elemento, "fetchall" e "fetchmany" pegam mais de um 
        return activities
   