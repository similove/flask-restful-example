from flask_restful import Resource, reqparse

from src.db.database import db_session
from src.db.models import User


class CreateUser(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('email', type=str)
            parser.add_argument('name', type=str)
            parser.add_argument('password', type=str)
            args = parser.parse_args()

            user = User(args['name'], args['password'], args['email'])
            db_session.add(user)
            db_session.commit()
            return str(user)
        except Exception as e:
            return {'error': str(e)}


class ReadUser(Resource):
    def get(self, id):
        # TOOD : implement
        return "do not implement yet"


class UpdateUser(Resource):
    def put(self, id):
        # TODO : implement
        return "do not implement yet"


class DeleteUser(Resource):
    def delete(self, id):
        # TODO : implement
        return "do not implement yet"


class ReadAllUser(Resource):
    def get(self):
        return str(User.query.all())
