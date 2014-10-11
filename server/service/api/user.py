from flask import *
from flask.ext.restful import Resource
from flask.ext.login import login_required
from service.model.user import *
from bson.objectid import ObjectId
import httplib

class UserApi(Resource):
    @login_required
    def get(self, uid):
        if not ObjectId.is_valid(uid):
            abort(httplib.NOT_FOUND)
        # Add .only to get partial information
        # E.g. user = User.objects(id=uid).only('email').first()
        user = User.objects(id=uid).first()
        if not user:
            abort(httplib.NOT_FOUND)
        user =  user.to_mongo().to_dict()
        # user['_id'] = str(user['_id'])
        return user