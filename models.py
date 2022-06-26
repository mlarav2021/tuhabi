from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class EmployeesModel(db.Model):
    __tablename__ = 'employees'

    id_employees = db.Column(db.String(), primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    company_name = db.Column(db.String())
    address = db.Column(db.String())
    city = db.Column(db.String())
    state = db.Column(db.String())
    zip = db.Column(db.String())
    phone1 = db.Column(db.String())
    phone2 = db.Column(db.String())
    email = db.Column(db.String())
    department = db.Column(db.String())