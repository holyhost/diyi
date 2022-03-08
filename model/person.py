from app import db

class Person(db.Model):
    __tablename__ = "person"
    
    id = db.Column('id',db.Integer, primary_key=True, doc='主键')
    router = db.Column('router', db.String)
    createtime = db.Column('createtime', db.TIMESTAMP(True),nullable=True)
    starttime = db.Column(db.DateTime,nullable=False)
    wedding = db.Column(db.DateTime)
    certificate = db.Column(db.DateTime)
    email = db.Column(db.String)
    mobile = db.Column(db.String)
    weixin = db.Column(db.String)
    boss = db.Column(db.String)
    name = db.Column(db.String)
    status = db.Column(db.SmallInteger, default=1)
    duration = db.Column(db.SmallInteger,default=365)