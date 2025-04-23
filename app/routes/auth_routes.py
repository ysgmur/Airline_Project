from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.models.user_model import User
from app import db
from app.utils.jwt_helper import generate_token
auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Login to receive JWT token
    ---
    tags:
      - Auth
    parameters:
      - in: body
        name: body
        schema:
          type: object
          properties:
            username:
              type: string
            password:
              type: string
    responses:
      200:
        description: Token generated
    """
    username = request.json.get("username")
    password = request.json.get("password")
    user = User.query.filter_by(username=username, password=password).first()

    if user:
        token = generate_token(user.username, user.role)
        return jsonify(
            access_token=token,
            username=user.username,
            role=user.role
        )

    return jsonify({"msg": "Invalid credentials"}), 401

@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Register a new user (Customer)
    ---
    tags:
      - Auth
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - username
            - password
          properties:
            username:
              type: string
            password:
              type: string
    responses:
      201:
        description: User registered
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "Username already exists"}), 400

    new_user = User(username=username, password=password, role="customer")
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully"}), 201
