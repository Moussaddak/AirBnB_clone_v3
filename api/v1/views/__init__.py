#!/usr/bin/python3
""" Module """
from flask import Blueprint
from api.v1.views.index import *

app_views = Blueprint('app_views', __name__)
