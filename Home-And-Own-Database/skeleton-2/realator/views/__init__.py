
from flask import Blueprint

from realator.views import index
from realator.views import sale
from realator.views import rent
from realator.views import addhome
from realator.views import remove
from realator.views import status


blueprint = Blueprint('views', __name__)
index.views(blueprint)
sale.views(blueprint)
rent.views(blueprint)
addhome.views(blueprint)
remove.views(blueprint)
status.views(blueprint)

def init_app(app):
    app.register_blueprint(blueprint)
    app.add_url_rule('/', endpoint='index')

