from main import db
from flask import Blueprint
from main import bcrypt
from models.persons import Person
from models.address import Address
from models.patients import Patient
from models.practitioners import Practitioner
from models.specialties import Specialty
from models.years_ex import Years


db_commands = Blueprint("db", __name__)


@db_commands .cli.command("create")
def create_tables():
    db.create_all()
    print("All tables and relations have been successfully created")
    

@db_commands .cli.command("drop_tables")
def drop_tables():
    db.drop_all()
    print("All tables in db have now been dropped")


@db_commands .cli.command("seed")
def seed_tables():
    address1 = Address(
        add_unit_no = None, 
        add_st_no = 7,
        add_st_type = "Street",
        add_st_name = "Farnham",
        add_city = "Gosnells",
        add_state = "WA",
        add_post_code = 6018,
        per_id = 4
    )
    
    address2 = Address(
        add_unit_no = None, 
        add_st_no = 129,
        add_st_type = "Cove",
        add_st_name = "Golfer",
        add_city = "Armadale",
        add_state = "WA",
        add_post_code = 6023,
        per_id = 2
    )

    address3 = Address(
        add_unit_no = None, 
        add_st_no = 10,
        add_st_type = "Street",
        add_st_name = "Imagination",
        add_city = "Yungarra",
        add_state = "WA",
        add_post_code = 6026,
        per_id = 1
    )

    address4 = Address(
        add_unit_no = None, 
        add_st_no = 43,
        add_st_type = "Close",
        add_st_name = "Johns",
        add_city = "Dunsborough",
        add_state = "WA",
        add_post_code = 6082,
        per_id = 3
    )
    
    db.session.add(address1)
    db.session.add(address2)
    db.session.add(address3)
    db.session.add(address4)
    db.session.commit()
    
    person1 = Person(
        per_title = "Mr",
        per_fname = "Michael",
        per_lname = "Vibert",
        per_email = 'mike16@hotmail.com',
        per_phone_no = "0403850574",
        per_medicare_no = 'MED1234',
        per_prac = False,
        per_patient = True,
        add_id = 1
    )
    
    
    person2 = Person(
        per_title = "Ms",
        per_fname = "Katie",
        per_lname = "Webber",
        per_email = 'katiegal@hotmail.com',
        per_phone_no = "0432450555",
        per_medicare_no = 'MED5678',
        per_prac = False,
        per_patient = True,
        add_id = 2
    )
    
    person3 = Person(
        per_title = "Dr",
        per_fname = "Fred",
        per_lname = "Fredricks",
        per_email = 'dr-fred@clinic.com.au',
        per_phone_no = "0488332211",
        per_medicare_no = 'MED9684',
        per_prac = True,
        per_patient = False,
        add_id = 3
    )
    
    person4 = Person(
        per_title = "Dr",
        per_fname = "Sally",
        per_lname = "Bologna",
        per_email = 'dr-sallyB@clinic.com.au',
        per_phone_no = "0426638553",
        per_medicare_no = 'MED7351',
        per_prac = True,
        per_patient = False,
        add_id = 4
    )
    
    db.session.add(person1)
    db.session.add(person2)
    db.session.add(person3)
    db.session.add(person4)
    db.session.commit()
    
    # patient1 = Patient(
    #     per_id = 2,
    #     pat_age = 15,
    #     pat_sex = "F",
    #     pat_weight = 45.3,
    #     pat_height = 147
    # )
    
    # patient2 = Patient(
    #     per_id = 1,
    #     pat_age = 43,
    #     pat_sex = "M",
    #     pat_weight = 75.2,
    #     pat_height = 181
    # )
    
    # db.session.add(patient1)
    # db.session.add(patient2)
    # db.session.commit()
    
    # spec1 = Specialty(
    #     spec_type = "General Practice"
    # )
    
    # spec2 = Specialty(
    #     spec_type = "Haematology"
    # )
    
    # db.session.add(spec1)
    # db.session.add(spec2)
    # db.session.commit()
    
    # prac1 = Practitioner(
    #     per_id = 3,
    #     spec_id = 2
    # )
    
    # prac2 = Practitioner(
    #     per_id = 4,
    #     spec_id = 1
    # )
    
    # db.session.add(prac1)
    # db.session.add(prac2)
    # db.session.commit()
    
    # ex1 = Years(
    #     spec_id = 2,
    #     prac_id = 1
    # )
    
    # ex2 = Years(
    #     spec_id = 1,
    #     prac_id = 2
    # )

    # db.session.add(ex1)
    # db.session.add(ex2)
    # db.session.commit()
    
    print("Tables seeded!")