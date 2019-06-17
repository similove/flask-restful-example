from flask import Flask
from flask_restful import Api

from src.api.user import CreateUser, ReadUser, UpdateUser, DeleteUser, ReadAllUser
from src.db.database import init_db

app = Flask(__name__)
api = Api(app)

api.add_resource(CreateUser, '/user')
api.add_resource(ReadUser, '/user/<string:id>')
api.add_resource(UpdateUser, '/user/<string:id>')
api.add_resource(DeleteUser, '/user/<string:id>')
api.add_resource(ReadAllUser, '/user')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8080, debug=True)
