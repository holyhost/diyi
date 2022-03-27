from app import db

class User(db.Model):
    __tablename__ = "user"
    
    id = db.Column('id',db.Integer, primary_key=True, doc='主键')
    createtime = db.Column('creattime', db.TIMESTAMP(True),nullable=True)
    logintime = db.Column(db.TIMESTAMP(True),nullable=True)
    weixin = db.Column(db.String)
    boss = db.Column(db.String)
    name = db.Column(db.String)
    account = db.Column(db.String)
    password = db.Column(db.String)
    email = db.Column(db.String)
    mobile = db.Column(db.String)
    status = db.Column(db.SmallInteger, default=1)
    type = db.Column(db.SmallInteger, default=1)