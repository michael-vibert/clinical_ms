from main import db


class Years(db.Model):
    __tablename__ = "years_ex"
    
    ex_id = db.Column(db.Integer, primary_key=True, nullable=False)
    spec_id = db.Column(db.Integer, db.ForeignKey("specialties.spec_id"), nullable=False)
    prac_id = db.Column(db.Integer, db.ForeignKey("practitioners.prac_id"), nullable=False)