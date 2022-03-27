from asyncio.windows_events import NULL
from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, current_user, login_required, login_user, logout_user
import pusher
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///userdata.db'
app.config['SECRET_KEY'] = 'stuudol'
db=SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
pusher_client = pusher.Pusher(app_id='1367852', key='7967f3ff921cc5e0393e', secret='d6b84267fc7e53d6d717', cluster='us2', ssl=True)


class User(UserMixin, db.Model):
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
    table_created = db.Column(db.String(5), unique=False, nullable=True)
    
    def __repr__(self):
        return f"Classes({self.course1}',{self.course2}','{self.course3}',{self.course4}', '{self.course5}',{self.course6}',{self.course7})"

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    message = db.Column(db.String(500))
db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


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
        messageCreation = Message(username = un)
            
        db.session.add(userCreation)
        db.session.add(classCreation)
        db.session.add(messageCreation)
        db.session.commit()

        return redirect('/')
        
    return render_template('register_page.html')



@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        submission = request.form
            
        eMail_input = submission['email']
        password_input = submission['password']
        user = User.query.filter_by(email=eMail_input).first()
        if user:
            if user.password == password_input:
                login_user(user)
                return redirect('/home')
    return render_template('login_page.html')



@app.route('/home', methods=['GET', 'POST'])
@login_required
def main():
    user_data = User.query.filter_by(id=current_user.id).first()
    class_data = Classes.query.filter_by(id=current_user.id).first()
    username = user_data.username
    class1 = class_data.course1
    class2 = class_data.course2
    class3 = class_data.course3
    class4 = class_data.course4
    class5 = class_data.course5
    class6 = class_data.course6
    class7 = class_data.course7
    return render_template('home_page.html', username=username, class1=class1, class2=class2, class3=class3, class4=class4, class5=class5, class6=class6, class7=class7)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route('/home/shared courses', methods=['GET', 'POST'])
@login_required
def display_shared_courses():
    current_courses = Classes.query.filter_by(id=current_user.id).first()
    shared_user = Classes.query.filter_by(course1=current_courses.course2).first()
    user = NULL

    if shared_user:
        user = User.query.filter_by(id=shared_user.id).first()
    
    if user:
        return 'found someone'
    return 'no one found'


@app.route('/addcourse1', methods=['GET', 'POST'])
@login_required
def add_course1():
    if request.method == "POST":
        submission = request.form
        classname = submission['classname']
        update_classes = Classes.query.filter_by(id=current_user.id).first()
        if(classname!=''):
            setattr(update_classes, 'course1', classname)
            db.session.commit()
            return redirect('/home')
    return render_template('add.html')

@app.route('/addcourse2', methods=['GET', 'POST'])
@login_required
def add_course2():
    if request.method == "POST":
        submission = request.form
        classname = submission['classname']
        update_classes = Classes.query.filter_by(id=current_user.id).first()
        if(classname!=''):
            setattr(update_classes, 'course2', classname)
            db.session.commit()
            return redirect('/home')
    return render_template('add.html')

@app.route('/addcourse3', methods=['GET', 'POST'])
@login_required
def add_course3():
    if request.method == "POST":
        submission = request.form
        classname = submission['classname']
        update_classes = Classes.query.filter_by(id=current_user.id).first()
        if(classname!=''):
            setattr(update_classes, 'course3', classname)
            db.session.commit()
            return redirect('/home')
    return render_template('add.html')

@app.route('/addcourse4', methods=['GET', 'POST'])
@login_required
def add_course4():
    if request.method == "POST":
        submission = request.form
        classname = submission['classname']
        update_classes = Classes.query.filter_by(id=current_user.id).first()
        if(classname!=''):
            setattr(update_classes, 'course4', classname)
            db.session.commit()
            return redirect('/home')
    return render_template('add.html')

@app.route('/addcourse5', methods=['GET', 'POST'])
@login_required
def add_course5():
    if request.method == "POST":
        submission = request.form
        classname = submission['classname']
        update_classes = Classes.query.filter_by(id=current_user.id).first()
        if(classname!=''):
            setattr(update_classes, 'course5', classname)
            db.session.commit()
            return redirect('/home')
    return render_template('add.html')

@app.route('/addcourse6', methods=['GET', 'POST'])
@login_required
def add_course6():
    if request.method == "POST":
        submission = request.form
        classname = submission['classname']
        update_classes = Classes.query.filter_by(id=current_user.id).first()
        if(classname!=''):
            setattr(update_classes, 'course6', classname)
            db.session.commit()
            return redirect('/home')
    return render_template('add.html')

@app.route('/addcourse7', methods=['GET', 'POST'])
@login_required
def add_course7():
    if request.method == "POST":
        submission = request.form
        classname = submission['classname']
        update_classes = Classes.query.filter_by(id=current_user.id).first()
        if(classname!=''):
            setattr(update_classes, 'course7', classname)
            db.session.commit()
            return redirect('/home')
    return render_template('add.html')



@app.route('/dropcourse1', methods=['GET', 'POST'])
@login_required
def drop_course1():
    update_classes = Classes.query.filter_by(id=current_user.id).first()
    setattr(update_classes, 'course1', None)
    db.session.commit()
    return redirect('/home')

@app.route('/dropcourse2', methods=['GET', 'POST'])
@login_required
def drop_course2():
    update_classes = Classes.query.filter_by(id=current_user.id).first()
    setattr(update_classes, 'course2', None)
    db.session.commit()
    return redirect('/home')

@app.route('/dropcourse3', methods=['GET', 'POST'])
@login_required
def drop_course3():
    update_classes = Classes.query.filter_by(id=current_user.id).first()
    setattr(update_classes, 'course3', None)
    db.session.commit()
    return redirect('/home')

@app.route('/dropcourse4', methods=['GET', 'POST'])
@login_required
def drop_course4():
    update_classes = Classes.query.filter_by(id=current_user.id).first()
    setattr(update_classes, 'course4', None)
    db.session.commit()
    return redirect('/home')

@app.route('/dropcourse5', methods=['GET', 'POST'])
@login_required
def drop_course5():
    update_classes = Classes.query.filter_by(id=current_user.id).first()
    setattr(update_classes, 'course5', None)
    db.session.commit()
    return redirect('/home')

@app.route('/dropcourse6', methods=['GET', 'POST'])
@login_required
def drop_course6():
    update_classes = Classes.query.filter_by(id=current_user.id).first()
    setattr(update_classes, 'course6', None)
    db.session.commit()
    return redirect('/home')

@app.route('/dropcourse7', methods=['GET', 'POST'])
@login_required
def drop_course7():
    update_classes = Classes.query.filter_by(id=current_user.id).first()
    setattr(update_classes, 'course7', None)
    db.session.commit()
    return redirect('/home')


"""
@app.route('/chat', methods=['GET', 'POST'])
@login_required
def chat():

    return render_template('message.html')
"""

@app.route('/chat')
def index():
    messages = Message.query.all()
    return render_template('message.html', messages=messages)

@app.route('/message', methods=['POST'])
def message():
    try:
        username = User.query.filter_by(id=current_user.id).first().username
        message = request.form.get('message')
        new_message = Message.query.filter_by(username=username).first()
        setattr(new_message, 'message', message)
        db.session.add(new_message)
        db.session.commit()

        pusher_client.trigger('chat-channel', 'new-message', {'username' : username, 'message': message})
        return jsonify({'result' : 'success'})
    except:
        return jsonify({'result' : 'failure'})


if __name__ == '__main__':
    app.run()
