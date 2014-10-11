from optparse import OptionParser
parser = OptionParser()
parser.add_option("-p", "--production", default=False, action="store_true",
                  help="Whether to run service in production mode.")
(options, args) = parser.parse_args()

from flask import Flask

app = Flask(__name__)

app.debug = not options.production

# Security Config
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_PASSWORD_HASH'] = 'sha512_crypt'
app.config['SECURITY_PASSWORD_SALT'] = 'fsef@f/fa0ghjs'
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_TRACKABLE'] = True
 
app.config['SESSION_COOKIE_SECURE'] = not app.debug

# Don't send emails now.
app.config['SECURITY_SEND_REGISTER_EMAIL'] = False

# MongoDB Models
import service.model

# Import all handlers
from service.handlers import *
from service import api

# FOR TESTING ONLY =====================
@app.before_first_request
def init_store_testing_data():
    from service.testing import generate_testing_data
    generate_testing_data()