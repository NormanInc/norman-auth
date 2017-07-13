from flask import Blueprint, render_template
from flask import templating
from flask import request


blueprint = Blueprint('register', __name__,url_prefix='/auth/register', static_folder='../static')


@blueprint.route('/')
def planOrProduct():
    return render_template('auth/planOrChoice.html')


@blueprint.route('/preRegistration')
def preRegistration():
    option = request.args.get('option')
    if option == 'plan':
        return render_template('auth/configurePlan.html')
    return render_template('auth/planOrChoice.html')





