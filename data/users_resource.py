from flask_restful import reqparse, abort, Resource
from . import db_session
from .users import User
from flask import jsonify


def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    users = session.query(User).get(user_id)
    if not users:
        abort(404, message=f"Users {user_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        users = session.get(User, user_id)
        return jsonify({'users': users.to_dict(
            only=('id',
                  'surname',
                  'age',
                  'name',
                  'position',
                  'speciality',
                  'address',
                  'email',
                  'modified_date'))})

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        users = session.get(User, user_id)
        session.delete(users)
        session.commit()
        return jsonify({'success': 'OK'})


parser = reqparse.RequestParser()
parser.add_argument('surname', required=True)
parser.add_argument('age', required=True, type=int)
parser.add_argument('name', required=True)
parser.add_argument('position', required=True)
parser.add_argument('speciality', required=True)
parser.add_argument('address', required=True)
parser.add_argument('email', required=True)
parser.add_argument('hashed_password', required=True)


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('id',
                  'surname',
                  'age',
                  'name',
                  'position',
                  'speciality',
                  'address',
                  'email',
                  'modified_date')) for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        users = User()
        users.surname = args['surname']
        users.age = args['age']
        users.name = args['name']
        users.position = args['position']
        users.speciality = args['speciality']
        users.address = args['address']
        users.email = args['email']
        users.set_password(args['hashed_password'])
        session.add(users)
        session.commit()
        return jsonify({'id': users.id})