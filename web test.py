from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('backbone.html')

if __name__ == '__main__':
    app.run()
