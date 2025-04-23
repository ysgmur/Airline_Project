from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from app.services.flight_service import create_flight, get_available_flights
from app.utils.jwt_helper import admin_required

flight_bp = Blueprint("flight_bp", __name__)

@flight_bp.route('/', methods=['POST'])
@jwt_required()
def add_flight():
    """
    Add a flight (JWT protected)
    ---
    tags:
      - Flights
    security:
      - Bearer: []
    parameters:
      - in: body
        name: body
        schema:
          type: object
          properties:
            date_from:
              type: string
            date_to:
              type: string
            airport_from:
              type: string
            airport_to:
              type: string
            duration:
              type: integer
            capacity:
              type: integer
    responses:
      201:
        description: Flight added
    """
    check = admin_required()
    if check:
        return check  # admin değilse 403

    data = request.get_json()
    return create_flight(data)

@flight_bp.route('/search', methods=['GET'])
def search_flights():
    """
    Search Flights (with paging)
    ---
    tags:
      - Flights
    parameters:
      - name: page
        in: query
        type: integer
      - name: page_size
        in: query
        type: integer
    responses:
      200:
        description: List of flights
    """
    page = request.args.get('page', 1, type=int)
    page_size = request.args.get('page_size', 10, type=int)
    return get_available_flights(page, page_size)
