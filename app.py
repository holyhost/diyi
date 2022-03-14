from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from util.person_cache import Pcache
from util.config import SqlConfig


app = Flask(__name__)
pcache = Pcache(100)


app.config.from_object(SqlConfig)
db = SQLAlchemy(app)
keywords = ['index','index.php','index.html']

from model.person import Person


@app.route('/')
def index():
    
    return render_template('./index.html')

@app.route('/<aname>')
def home(aname):
    print(aname)
    # 1. 判断aname是否是关键字，如果是index等字眼，返回首页
    if aname in keywords:
        return render_template('./index.html')
    args = request.args
    print(args)
    # 从参数判断是否从缓存中取数据
    person = pcache.get(aname)
    isNew = 'isnew' in  request.args.keys()
    if isNew and request.args.get('isnew') == '1' :
        person = None
    
    if person is None:
        # 从person表中取出 aname相关数据
        person = Person.query.filter_by(router=aname).first()
        if person: 
            pcache.add(person)
            print("从数据库拿数据。{}".format(person.router))
    print(person)
    # 判断是否为空，有数据的话返回渲染
    if person:
        return render_template('./love.html',airen=person.name,boss=person.boss,starttime=person.starttime)
    return render_template('./index.html')


@app.route('/router/add')
def add_router():
    # person = Person(router="dlrb",starttime='2020-02-02 02:02:02',boss="周先生")
    # db.session.add(person)
    # db.session.commit()
    # return "success:{}".format(person.boss)
    pass

@app.route('/get')
def get():
    list = Person.query.all()
    print(list)
    return list[1].router