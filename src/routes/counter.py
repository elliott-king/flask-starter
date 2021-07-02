import os

from flask import (
    Blueprint,
    render_template,
    jsonify
)

from src.models import Counter


blueprint = Blueprint('counter', __name__)

class Parse:
    """Class of utility functions to parse environment variables"""

    @staticmethod
    def bool(field):
        """Parse booleans (defaults to False)"""
        return os.getenv(field, '').lower() in ['true', '1']

    @staticmethod
    def string(field, default=None):
        """
        Parse strings - defaults to the default value provided even if the environment variable is
        set to a blank string.
        """
        return os.getenv(field) or default

@blueprint.route('/')
def index():
    counter = Counter.get_create(label='Test')
    counter.increment()
    web_domain = Parse.string('SHIPYARD_DOMAIN_WEB', default="NO WEB DOMAIN")
    api_domain = Parse.string('SHIPYARD_DOMAIN_API', default="NO API DOMAIN")
    return render_template('counter.html', counters=Counter.list(), web_domain=web_domain, api_domain=api_domain)

@blueprint.route('/json')
def json():
    return jsonify(Parse.string('SHIPYARD_DOMAIN', default="NO SHIPYARD DOMAIN")), 200