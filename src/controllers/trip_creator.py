from typing import Dict
import uuid

class TripCreator:
    def __init__(self, trip_repository, emails_repository) -> None:
        self.__trip_repository = trip_repository
        self.__emails_repository = emails_repository
        
    def create(self, body) ->Dict:
        emails = body.get("emails_to_invite")