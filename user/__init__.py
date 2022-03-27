from flask import Blueprint

# 创建蓝图对象
user_bp = Blueprint("user",__name__)

from . import views