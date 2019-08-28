from flask import Flask

app = Flask(__name__)

# Set up the app with the config.py file.
app.config.from_object('app.config')


# Import the views.
from app.views import main
