from mongoengine import *
from flask.ext.security import UserMixin, RoleMixin

class Role(Document, RoleMixin):
    name = StringField(max_length=80, unique=True)
    description = StringField(max_length=255)

class User(Document, UserMixin):
    # Flask-Security fields
    email = StringField(max_length=255, required=True, unique=True)
    password = StringField(max_length=255)
    active = BooleanField(default=True)
    confirmed_at = DateTimeField()
    roles = ListField(ReferenceField(Role))
    last_login_at = DateTimeField()
    current_login_at = DateTimeField()
    last_login_ip = StringField(max_length=50)
    current_login_ip = StringField(max_length=50)
    login_count = IntField()

    # Service fields
    username = StringField(max_length=255)
