from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


@app.route('/', methods=['GET'])
def home():
    return jsonify(str([user for user in User.query.all()]))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return 'id: {} name: {}'.format(self.id, self.name)


def create_dummy_users():
    user_one = User(name='Zach')
    user_two = User(name='Bob')
    db.session.add(user_one)
    db.session.add(user_two)
    db.session.commit()


# Start the application
if __name__ == '__main__':
    db.create_all()
    create_dummy_users()
    app.run()
