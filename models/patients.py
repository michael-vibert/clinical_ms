from main import db


class Patient(db.Model):
    __tablename__ = "patients"
    
    pat_id = db.Column(db.Integer, primary_key=True, nullable=False)
    pat_age = db.Column(db.Integer, nullable=False)
    pat_sex = db.Column(db.String, nullable=False)
    pat_weight = db.Column(db.Double, nullable=True)
    pat_height = db.Column(db.Double, nullable=True)
    per_id = db.Column(db.Integer, db.ForeignKey("persons.per_id"), nullable=False)