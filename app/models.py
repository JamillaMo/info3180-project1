from . import db

class Property(db.Model):
    # __tablename__ = "user_profiles"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    #email = db.Column(db.String(120), unique=True)
    #password = db.Column(db.String(255))

    def __init__(self, title, email):
        self.title = title
        self.email = email
        #self.password = generate_password_hash(password)

    def __repr__(self):
        return '<Property %r>' % self.title