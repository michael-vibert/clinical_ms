from main import db 


class Address(db.Model):
    __tablename__ = "addresses"
    # table rows
    add_id = db.Column(db.Integer, primary_key=True)
    add_unit_no = db.Column(db.Integer, nullable=True)
    add_st_no = db.Column(db.Integer, nullable=False)
    add_st_type = db.Column(db.String, nullable=False)
    add_st_name = db.Column(db.String, nullable=False)
    add_city = db.Column(db.String, nullable=False)
    add_state = db.Column(db.String, nullable=False)
    add_post_code = db.Column(db.Integer, nullable=False)
    persons = db.relationship("Person", backref="address", cascade="all, delete")