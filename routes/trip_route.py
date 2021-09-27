from flask import Blueprint, request, redirect, url_for, Response
from my_app.models import user_model, trip_model

bp = Blueprint('beertrip', __name__)


@bp.route('/beertrip', methods=['POST'])
def update_trip_destination():
    
    username = request.form.get('username')
    des = request.form.get('destination')

    if not username :
        return "이름을 입력해주세요.", 400

    elif not des :
        return "Beer Trip 행선지를 입력해주세요.", 400

    elif not user_model.find_user(username):
        return "What's your Beer Style 메뉴를 먼저 실행해주세요.", 400

    else:
        trip_model.update_trip_destination(inputname=username, destination=des)
        return redirect(url_for('main.user_index', msg_code=0), code=200)