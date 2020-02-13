from objects import db

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # fields from mtgjson.com
    colorIdentity = db.Column(db.String(256))
    # colorIndicator = db.Column(db.String(256))
    colors =  db.Column(db.String(256))
    convertedManaCost = db.Column(db.String(256))
    # edhrecRank =  db.Column(db.String(256))
    faceConvertedManaCost = db.Column(db.String(256))
    # foreignData = db.Column(db.String(256))
    # hand
    # hasNo
    isReserved = db.Column(db.String(256))
    # layout
    # leadershipSkills
    legalities = db.Column(db.String(256))
    # life
    loyalty = db.Column(db.String(256))
    manaCost = db.Column(db.String(256))
    name = db.Column(db.String(256), nullable=False)
    names =  db.Column(db.String(256))
    power =  db.Column(db.String(256))
    printings =  db.Column(db.String(256))
    rulings = db.Column(db.String(256))
    #scryfallOracleId
    oracleId = db.Column(db.String(256))
    # side
    subtypes = db.Column(db.String(256))
    supertypes = db.Column(db.String(256))
    text = db.Column(db.String(2048))
    toughness = db.Column(db.Integer)
    # type
    cardtype = db.Column(db.String(256))
    types = db.Column(db.String(256))
    uuid = db.Column(db.String(256))

    def __repr__(self):
        return f"<Card {self.oracleId} {self.name}>"

