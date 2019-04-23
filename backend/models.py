from backend import db, ma

class Building(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    rooms = db.relationship('Room', backref='building', lazy=True)
    



class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    building_id = db.Column(db.Integer, db.ForeignKey('building.id'))
    datas = db.relationship('TelemetricData', backref='room', lazy=True)


class TelemetricData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float(64))
    pressure = db.Column(db.Float(64))
    humidity = db.Column(db.Float(64))
    IAQ = db.Column(db.Float(64))
    date = db.Column(db.DateTime())
    room_id=db.Column(db.Integer, db.ForeignKey('room.id'))
    
class TelemetricDataSchema(ma.ModelSchema):
    class Meta:
        model = TelemetricData



class BuildingSchema(ma.ModelSchema):
    class Meta:
        model = Building

class RoomSchema(ma.ModelSchema):
    class Meta:
        model = Room