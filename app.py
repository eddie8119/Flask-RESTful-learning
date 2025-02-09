from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

user_list = []

class Helloworld(Resource):

    def get(self):
        return 'hello world'

class User(Resource):

    def get(self, username):
        for user in user_list:
            if user['username'] == username:
                return user
        return {'message': 'User not found'}, 404

    def post(self, username):
        for u in user_list:
            if u['username'] == username:
                return {'message': 'User already exists'}, 400
        user = {'username': username, 'password': request.get_json().get('password')}
        user_list.append(user)
        return user, 201

    def delete(self, username):
        user_find = None
        for user in user_list:
            if user['username'] == username:
                user_find = user
        if user_find:
            user_list.remove(user_find)
            return user_find
        else:
            return {'message': 'User not found'}, 204

    def put(self, username):
        user_find = None
        for user in user_list:
            if user['username'] == username:
                user_find = user
        if user_find:
            user_list.remove(user_find)
            user_find['password'] = request.get_json().get('password')
            user_list.append(user_find)
            return user_find
        else:
            return {'message': 'User not found'}, 404

class UserList(Resource):

    def get(self):
        return user_list       

api.add_resource(Helloworld, '/')
api.add_resource(User, '/user/<string:username>')
api.add_resource(UserList, '/users')



if __name__ == "__main__":
    app.run()