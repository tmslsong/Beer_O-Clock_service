from flask import Blueprint, render_template, request
from my_app.utils import main_funcs
from my_app.models import user_model
from my_app.models.user_model import User


bp = Blueprint('main', __name__)



@bp.route('/', methods=["GET"])
def index():
    return render_template('main_index.html')



@bp.route('/user')
def user_index():
    
    msg_code = request.args.get('msg_code', None)

    alert_msg = main_funcs.msg_processor(msg_code) if msg_code is not None else None

    user_list = user_model.get_users()

    return render_template('user.html', alert_msg=alert_msg, user_list=user_list)



@bp.route('/trip', methods=["GET", "POST"])
def trip_index():
    
    all_users = user_model.User.query.all()

    users = [{"username": user.username, "beer_pref": user.beer_pref} for user in all_users]



    return render_template('trip.html')


