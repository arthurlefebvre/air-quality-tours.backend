from backend import app,db
from backend.models import Building, BuildingSchema, Room, RoomSchema, TelemetricData, TelemetricDataSchema
from flask import jsonify


donnees = [
            {
                'id': '1',
                'name': 'Lovelace',
                'temperature': '19',
                'pression': '15',
                'IAQ': '19',
                'img': 'https://histoireparlesfemmes.files.wordpress.com/2013/02/ada-lovelace.jpg?w=298'
            },
            {
                'id': '2',
                'name': 'Bool',
                'temperature': '18',
                'pression': '20',
                'IAQ': '30',
                'img': 'https://i.skyrock.net/1021/93931021/pics/3264129790_1_3_cW3IgKx5.jpg'
            },
            {
                'id': '3',
                'name': 'Shannon',
                'temperature': '18',
                'pression': '20',
                'IAQ': '50',
                'img':'https://upload.wikimedia.org/wikipedia/commons/9/99/ClaudeShannon_MFO3807.jpg'
            },
            {
                'id': '4',
                'name': 'TP Systèmes',
                'temperature': '18',
                'pression': '20',
                'IAQ': '50',
                'img':''
            }
        ]
room_schema = RoomSchema()
rooms_schema = RoomSchema(many=True)


# sanity check route
@app.route('/', methods=['GET'])
def home():
    rooms = Room.query.all()
    return rooms_schema.jsonify(rooms)

@app.route('/datas', methods=['GET'])
def get_datas():
    return jsonify({
        'status': 'success',
        'datas': donnees
    })

@app.route('/salle/<id>', methods=['GET'])
def get_data(id):
    for data in donnees:
        if data.get('id') == id:
            return jsonify({
                'status': 'success',
                'data': data
            })
    return jsonify({
        'status': 'error',
        'data': 'Not found'
    })


