from objects import db

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('tags', lazy=True))
    card_id = db.Column(db.Integer, db.ForeignKey('card.id'))
    card = db.relationship('Card', backref=db.backref('tags', lazy=True))

    def __repr__(self):
        return f"<Tag {self.tag}, {self.user_id}, {self.card_id}>"
