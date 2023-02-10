from main import db


class Practitioner(db.Model):
    __tablename__ = "practitioners"
    
    prac_id = db.Column(db.Integer, primary_key=True, nullable=False)
    per_id = db.Column(db.Integer, db.ForeignKey("persons.per_id"), nullable=False)
#     spec_id = db.relationship('Specialty', backref='practitioner', lazy=True)
    
    