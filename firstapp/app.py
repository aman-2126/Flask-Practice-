import requests
from flask import Flask, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite'
db = SQLAlchemy(app)


class users(db.Model):
    _id = db.Column('_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name


db.create_all()


@app.route("/", methods=["GET"])
def home():
    # data = request.json
    # if data == None:
    #     return jsonify({"message": "no params sent"})
    # return {"message": "success", "data_sent": data}
    users_dict = dict()
    users_list = users.query.all()
    for i in range(len(users_list)):
        users_dict[f"user {i+1}"] = users_list[i].name

    return jsonify(users_dict)


@app.route("/add", methods=["POST"])
def add_user():
    json_data = request.json
    if json_data == None:
        return jsonify({"message": "no params sent"})
    db.session.add(users(json_data["name"]))
    db.session.commit()
    return "user added"


if __name__ == "__main__":
    app.run()
