import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api_key = 'testingapikey'

##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")


# to avoid the manually typing the json data we can use dictionary convertor
def to_dict(self):
    dictionary = {}
    for column in self.__table__.columns:
        dictionary[column.name] = getattr(self, column.name)
        #getting name of column   #getting value of column
    return dictionary
    #alternate method by dictionary comprehension
    #return {column.name: getattr(self, column.name) for column in self.__table__.columns}

## HTTP GET - Read Record
@app.route('/random')
def get_random_cafe():
    cafe = db.session.query(Cafe).all()
    random_cafe = random.choice(cafe)
    # return jsonify(cafe={
    #                "name":random_cafe.name,
    #                "map_url": random_cafe.map_url,
    #                "img_url": random_cafe.img_url,
    #                "location": random_cafe.location,
    #                "amenities": {
    #                    "seats": random_cafe.seats,
    #                    "has_toilet": random_cafe.has_toilet,
    #                    "has_wifi": random_cafe.has_wifi,
    #                    "has_sockets": random_cafe.has_sockets,
    #                    "can_take_calls": random_cafe.can_take_calls,
    #                    "coffee_price": random_cafe.coffee_price,
    #                         }
    #                     })
    # Easy way
    return jsonify(cafe=to_dict(random_cafe))

@app.route('/all')
def all_cafes():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafe=[to_dict(cafe) for cafe in cafes]) #list comprehension

@app.route('/search')
def search():
    query_location = request.args.get('loc')
    cafe = db.session.query(Cafe).filter_by(location=query_location).first()
    if cafe:
        return jsonify(cafe=to_dict(cafe))
    else:
        return jsonify(error={"not found": "sorry we dont found any cafe at this location"})

## HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('name')
    if name is None:
        return jsonify(error='Name parameter is required')

    new_cafe = Cafe(
        name= request.form.get('name'),
        map_url=request.form.get('map_url'),
        img_url=request.form.get('img_url'),
        location=request.form.get('location'),
        has_sockets=bool(request.form.get('has_socket')),
        has_toilet=bool(request.form.get('has_toilet')),
        has_wifi=bool(request.form.get('has_wifi')),
        can_take_calls=bool(request.form.get('can_take_calls')),
        seats=request.form.get('seats'),
        coffee_price=request.form.get('coffee_price')
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={
        'success' : 'successfully added the new cafe'
    })

## HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    cafe.coffee_price = request.form.get('coffee_price')
    db.session.add(cafe)
    db.session.commit()
    return jsonify(response={
        'success': 'successfully updated coffee price'
    })

## HTTP DELETE - Delete Record
@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def delete(cafe_id):
    api_key_user = request.args.get('api_key')
    if api_key_user == api_key:
        cafe_to_delete = db.session.query(Cafe).get(cafe_id)
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={
                'success' : 'Successfully deleted the cafe from the database'
            }), 200
        else:
            return jsonify(error={
            'Not Found' : 'Sorry a cafe with that id not found in the database'
        }), 404
    else:
        return jsonify(error={
            'Forbidden' : 'Sorry that not allowed, Make sure u have the correct api key'
            }), 400


if __name__ == '__main__':
    app.run(debug=True)
