from flask import Blueprint

bp = Blueprint("errors", __name__)

# pylint: disable=wrong-import-position
from app.errors import handlers

# pylint: enable=wrong-import-position
