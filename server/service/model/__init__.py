from flask.ext.mongoengine import MongoEngine
from service import app

# MongoDB Config
DB_NAME = 'xiaozhu'
DB_NAME_PRODUCTION = DB_NAME + '_PROD'
DB_NAME_TEST = DB_NAME + '_TEST'

app.config['MONGODB_DB'] = DB_NAME_TEST if app.debug else DB_NAME_PRODUCTION
app.config['MONGODB_HOST'] = 'localhost'
app.config['MONGODB_PORT'] = 27017

db = MongoEngine(app)

from flask.ext.security import Security, MongoEngineUserDatastore
from user import User
from user import Role

# Setup Flask-Security
user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore)