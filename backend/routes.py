from backend import app,db
from backend.models import Building, BuildingSchema, Room, RoomSchema, TelemetricData, TelemetricDataSchema
from flask import jsonify


room_schema = RoomSchema()
rooms_schema = RoomSchema(many=True)


# sanity check route
@app.route('/', methods=['GET'])
def home():
    rooms = Room.query.all()
    return rooms_schema.jsonify(rooms)

@app.route('/salle/<id>', methods=['GET'])
def get_data(id):
    room = Room.query.get(id)
    return room_schema.jsonify(room)

