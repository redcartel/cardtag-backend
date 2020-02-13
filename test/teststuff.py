from xtest.app import db, app
import objects
objects.db = db
objects.app = app
from cardtag.models.user import User
from cardtag.models.card import Card
from cardtag.models.tag import Tag

db.create_all()

def testok():
    assert True
