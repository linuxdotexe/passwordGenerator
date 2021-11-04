from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class storePassword(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(21), nullable=False)

    def __showPass__(self):
        return '<Password %r>' % self.password

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        pass
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)