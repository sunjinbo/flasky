from flask import Blueprint

main = Blueprint('main', __name__)

# 为了避免循环导入依赖，放置在脚本的尾部
from . import views, errors
