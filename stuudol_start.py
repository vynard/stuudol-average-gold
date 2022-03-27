from asyncio.windows_events import NULL
from flask import *
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///userdata.db'
db=SQLAlchemy(app)
#login_manager = LoginManager()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), unique=False, nullable=False)
    lastname = db.Column(db.String(20), unique=False, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phonenumber = db.Column(db.String(14), unique=True, nullable=True)
    password = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return f"User({self.firstname}',{self.lastname}','{self.username}',{self.pnumber}', '{self.email}', '{self.password}')"



class Classes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course1 = db.Column(db.String(9), unique=False, nullable=True)
    course2 = db.Column(db.String(9), unique=False, nullable=True)
    course3 = db.Column(db.String(9), unique=False, nullable=True)
    course4 = db.Column(db.String(9), unique=False, nullable=True)
    course5 = db.Column(db.String(9), unique=False, nullable=True)
    course6 = db.Column(db.String(9), unique=False, nullable=True)
    course7 = db.Column(db.String(9), unique=False, nullable=True)
    table_created = db.Column(db.String(5), unique=False, nullable=False)
    
    def __repr__(self):
        return f"Classes({self.course1}',{self.course2}','{self.course3}',{self.course4}', '{self.course5}',{self.course6}',{self.course7})"



db.create_all()
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":    
        submission = request.form
            
        fn = submission['fname']
        ln = submission['lname']
        un = submission['uname']
        eMail = submission['email']
        pNumber = submission['pnumber']
        password = submission['password']
            
        userCreation = User(username = un, lastname=ln, firstname=fn, email=eMail, phonenumber=pNumber, password=password)
        classCreation = Classes(table_created = 'true')
            
        db.session.add(userCreation)
        db.session.add(classCreation)
        db.session.commit()

        return redirect('/login')
        
    return render_template('register_page.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        submission = request.form
            
        eMail_input = submission['email']
        password_input = submission['password']
        user = User.query.filter_by(email=eMail_input).first()
        if user:
            if user.password == password_input:
                return 'success'
    return render_template('login_page.html')



@app.route('/', methods=['GET', 'POST'])
def main():


    return render_template('main_page.html')

if __name__ == '__main__':
    app.run()
