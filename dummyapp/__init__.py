from flask import Flask

app_obj = Flask(__name__)

from . import routes
from . import rest_api
