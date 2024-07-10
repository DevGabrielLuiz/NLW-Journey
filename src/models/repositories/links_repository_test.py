import uuid
import pytest
from src.models.settings.db_connection_handler import db_connection_handler
from .links_repository import LinksToInviteRepository

db_connection_handler.connect()
trip_id = str(uuid.uuid4())


def test_registry_link():
    conn = db_connection_handler.get_connection()
    links_to_invite_repository = LinksToInviteRepository(conn)
    
    link_trips_infos = {
        "id":str(uuid.uuid4()),
        "trip_id": trip_id,
        "link": "https://devgabrielluiz.github.io/Jogo_Mario_JS/mario.html", 
    }
    links_to_invite_repository.registry_link(link_trips_infos)
 
    
def test_find_links_from_trip():
    conn = db_connection_handler.get_connection()
    links_to_invite_repository = LinksToInviteRepository(conn)
    
    links = links_to_invite_repository.find_links_from_trip(trip_id)
    print()
    print(links)