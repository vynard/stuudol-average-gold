from flask import *
from flask_mysqldb import MySQL
from click import *

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'userdata'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        submission = request.form
        firstName = submission['fname']
        lastName = submission['lname']
        userName = submission['uname']
        eMail = submission['email']
        pNumber = submission['pnumber']
        firstClass = submission['class1']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(first_name, last_name, user_name, email, phone_number) VALUES (%s, %s, %s, %s, %s)", (firstName, lastName, userName, eMail, pNumber))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('backbone.html')

if __name__ == '__main__':
    app.run()
