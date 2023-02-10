from main import db 


class Person(db.Model):
    __tablename__ = "persons"
    # table rows
    per_id = db.Column(db.Integer, primary_key=True)
    per_title = db.Column(db.String, nullable=True)
    per_fname = db.Column(db.String, nullable=False)
    per_lname = db.Column(db.String, nullable=False)
    per_email = db.Column(db.String, nullable=False)
    per_phone_no = db.Column(db.String, nullable=False)
    per_medicare_no = db.Column(db.String, nullable=True)
    per_prac = db.Column(db.Boolean, nullable = False)
    per_patient = db.Column(db.Boolean, nullable = False)    
    add_id = db.Column(db.Integer, db.ForeignKey("addresses.add_id"), nullable=False)