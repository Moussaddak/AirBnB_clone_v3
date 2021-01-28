#!/usr/bin/python3
""" API Module """
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')
app.url_map.strict_slashes = False


@app.teardown_appcontext
def end_session():
    storage.close()

if __name__ == '__main__':
    app.run(host=getenv("HBNB_API_HOST"),
            port=getenv("HBNB_API_PORT"),
            threaded=True)
