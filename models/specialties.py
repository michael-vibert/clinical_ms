from main import db


class Specialty(db.Model):
    __tablename__ = "specialties"
    
    spec_id = db.Column(db.Integer, primary_key=True, nullable=False)
    spec_type = db.Column(db.String, nullable=False)
    # prac_id = db.Column(db.Integer, db.ForgeinKey('practitioners.prac_id'), nullable=False)
    