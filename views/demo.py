from flask import Blueprint, render_template
from flask import templating
# from security import norman_security

blueprint = Blueprint('demo', __name__, static_folder='../static')


