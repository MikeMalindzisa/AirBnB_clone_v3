#!/usr/bin/python3
"""
    This starts a flask application
"""

from flask import Flask
from models import storage
from api.v1.views import app_views

# Create a variable `app`, an instance of Flask
app = Flask(__name__)

# Register the blueprint `app_views` to your Flask instance `app`
app.register_blueprint(app_views)

# Declare a method to handle `@app.teardown_appcontext` that calls `storage.close()`
@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()

# Inside if __name__ == "__main__":, run your Flask server (`app`)
if __name__ == "__main__":
    import os

    # Get host and port from environment variables, fallback to default values if not defined
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(os.environ.get('HBNB_API_PORT', 5000))

    # Run Flask server with specified host, port, and threaded=True
    app.run(host=host, port=port, threaded=True)
