from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from pglib import myfunctions

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

generate = myfunctions.generate

class storePassword(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(21), nullable=False)

    @staticmethod
    def showPass(length):
        password = generate(length)
        return password

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        l = int(request.form["length"])
        password = str(storePassword.showPass(l))
        return render_template('index.html', password=password)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)