# Initialize app from backend/__init__.py
from backend import app, db
from backend.models import Building, Room, TelemetricData 

# Run the application
if __name__ == '__main__':
    app.run()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Building': Building, 'Room': Room, 'TelemetricData': TelemetricData}