from flask import *
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)




app.config['MYSQL_HOST'] = 'localhost'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'
db=SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), unique=True, nullable=False)
    lastname = db.Column(db.String(20), unique=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phonenumber = db.Column(db.String(120), unique=True, nullable=False)
    course = db.Column(db.String(20), unique=True, nullable=False)


    def __repr__(self):


        return f"User({self.firstname}',{self.lastname}','{self.username}',{self.pnumber}', '{self.email}',{self.course}')"

db.create_all()
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        submission = request.form
        fn = submission['fname']
        ln= submission['lname']
        un = submission['uname']
        eMail = submission['email']
        pNumber = submission['pnumber']
        firstClass = submission['class1']
        cuser= User( username=un,lastname=ln,firstname=fn,email= eMail,phonenumber=pNumber,course=firstClass)
        db.session.add(cuser)
        db.session.commit()

        return 'success'
    return render_template('backbone.html')

if __name__ == '__main__':
    app.run()
