from flask import Flask

API_PREFIX = "api/v1"

app_obj = Flask(__name__)

from . import routes
from . import rest_api
