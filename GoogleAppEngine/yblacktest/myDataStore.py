
from google.appengine.ext import db

class Person(db.Model):
    name = db.StringProperty()
    area = db.StringProperty()
