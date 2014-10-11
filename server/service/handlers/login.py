from service import app
from flask.ext.login import login_required
from flask_wtf import csrf

# Test for login required
@app.route("/")
@login_required
def hello():
    return "Test Hello World!"

@app.route('/csrf')
def csrf_token():
    return csrf.generate_csrf()