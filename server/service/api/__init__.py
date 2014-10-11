from flask.ext import restful
from service import app

from .json import output_json

class Api(restful.Api):
    def __init__(self, *args, **kwargs):
        super(Api, self).__init__(*args, **kwargs)
        self.representations = {
            'application/json': output_json,
            #####################################
            # Disable following representations
            #
            # 'application/xml': output_xml,
            # 'text/html': output_html,
            # 'text/csv': output_csv,
        }

api = Api(app)

from .user import UserApi
from .hello_world import HelloWorld

api.add_resource(UserApi, '/users/<string:uid>')