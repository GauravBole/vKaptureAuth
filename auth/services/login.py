from flask import Blueprint
# from ...config import db_cursor
from config import db_cursor
login_url_blue_print = Blueprint('login_url', __name__)


@login_url_blue_print.route('/')
def index():
    print(db_cursor.execute("select * from auth"))
    
    return "Thiss is an example app check"
