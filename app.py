from flask import Flask
from flask_migrate import Migrate
from models import db,EmployeesModel
import socket

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@db:5432/mlv'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)
migrate = Migrate(app, db)

@app.route('/employees')
def index():
    employees = EmployeesModel.query.all()
    results = [
        {
            "first_name": tr.first_name,
            "last_name": tr.last_name,
            "company_name": tr.company_name,
            "address": tr.address,
            "city": tr.city,
            "state": tr.state,
            "zip": tr.zip,
            "phone1": tr.phone1,
            "phone2": tr.phone2,
            "email": tr.email,
            "department": tr.department
        } for tr in employees]
    return {"records":len(results),"value":results}

if __name__ == '__main__':
   app.run(debug=True,host='python',port=5000)