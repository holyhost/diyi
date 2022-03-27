from . import user_bp
from flask import request
from ..model.user import User

@user_bp.route("/get/<int:userid>")
def getUser(userid):
    user = User.query.filter(User.id==userid).first()
    print(user)
    return user

# 添加用户
@user_bp.route("/add",methods=['POST'])
def addUser():
    data = request.get_json()
    print(type(data))
    print(data)
    print(data['name'])
    return "add user"
    
# 注册用户
@user_bp.route("/register",methods=['POST'])
def regUser():
    data = request.get_json()
    print(type(data))
    print(data)
    print(data['name'])
    return "add user"
