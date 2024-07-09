from flask import jsonifys, Blueprint

trips_routes_bp = Blueprint("trip_routes",__name__)

@trips_routes_bp.route("/trips", methods=["POST"] )# deixa mais intuitivo sobre o que é cada rota
def create_trip():
    return jsonifys({'olá':'mundo'}), 200
