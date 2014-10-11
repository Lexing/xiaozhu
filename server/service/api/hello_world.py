from flask.ext.restful import Resource
from flask.ext.restful import reqparse

class HelloWorld(Resource):
    __parser = reqparse.RequestParser()
    __parser.add_argument('rate', type=int, help='Rate to charge for this resource')

    def get(self):
        # Example URL http://localhost/helloworld?rate=2134&122=12
        args = self.__parser.parse_args()
        return args  # {"rate": 2134 }